import os
import glob
import uuid
import numpy as np
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import openai
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
import warnings

# Ignorar avisos de deprecación debido a rápidos cambios de langchain
warnings.simplefilter("ignore", DeprecationWarning)

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar la API key de OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada. Por favor, configúrala con tu clave de OpenAI.")

# Configurar Qdrant utilizando las variables de entorno
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")  # API key para Qdrant Cloud, si procede
QDRANT_ENDPOINT = os.environ.get("QDRANT_ENDPOINT")  # URL de Qdrant
client = QdrantClient(
    url=QDRANT_ENDPOINT,
    api_key=QDRANT_API_KEY
)

# Definir el nombre de la colección y la dimensión del vector
collection_name = "rag_introductorio"
vector_size = 1536  # Dimensión del embedding generado por text-embedding-ada-002

def generate_embeddings(texts):
    """
    Genera embeddings para una lista de textos utilizando el modelo text-embedding-ada-002 de OpenAI.
    
    Parámetros:
      texts (list): Lista de cadenas de texto.
    
    Retorna:
      list: Lista de arrays numpy (float32) con los embeddings generados.
    """
    response = openai.Embedding.create(
        input=texts,
        model="text-embedding-ada-002"
    )
    embeddings = [np.array(item["embedding"], dtype="float32") for item in response["data"]]
    return embeddings

def ingest_documents(directory="temario/introductorio", files=None):
    """
    Carga archivos Markdown, los procesa y los inserta en la colección de Qdrant.
    
    Parámetros:
      directory (str): Directorio donde se encuentran los archivos Markdown.
      files (list o None): Si se especifica, procesa solo esos archivos; si es None, se buscan todos los .md en el directorio.
    """
    documents = []
    if files is None:
        files = glob.glob(os.path.join(directory, "*.md"))
    if not files:
        raise ValueError(f"No se encontraron archivos Markdown en el directorio '{directory}'.")
    
    for md_file in files:
        loader = UnstructuredMarkdownLoader(md_file)
        docs = loader.load()
        for doc in docs:
            # Agregar el nombre del archivo como metadata 'source'
            doc.metadata["source"] = os.path.basename(md_file)
            documents.append(doc)
    
    print(f"Se han cargado {len(documents)} documentos desde {len(files)} archivos.")
    
    # Dividir documentos en fragmentos para facilitar el procesamiento
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    print(f"Se han obtenido {len(chunks)} fragmentos tras dividir los documentos.")
    
    # Generar embeddings para cada fragmento
    chunk_texts = [chunk.page_content for chunk in chunks]
    embeddings = generate_embeddings(chunk_texts)
    
    # Preparar los puntos a insertar en Qdrant
    points = []
    for i, emb in enumerate(embeddings):
        source = chunks[i].metadata.get("source", "desconocido")
        point = PointStruct(
            id=str(uuid.uuid4()),  # Generar un ID único para cada punto
            vector=emb.tolist(),   # Convertir el array de numpy a lista
            payload={
                "text": chunk_texts[i],
                "source": source
            }
        )
        points.append(point)
    
    # Insertar (upsert) los puntos en la colección de Qdrant
    client.upsert(
        collection_name=collection_name,
        points=points
    )
    print(f"Se han insertado {len(points)} puntos en la colección '{collection_name}'.")

def get_processed_files():
    """
    Recupera los nombres de los archivos (valor de 'source') que ya han sido insertados en la base de datos.
    
    Retorna:
      set: Conjunto de nombres de archivos ya procesados.
    """
    processed_files = set()
    # Usamos scroll para obtener todos los puntos
    points, _ = client.scroll(collection_name=collection_name, limit=1000, with_payload=True)
    for point in points:
        source = point.payload.get("source")
        if source:
            processed_files.add(source)
    return processed_files

def update_database_if_new_files(directory="temario/introductorio"):
    """
    Verifica si la colección está vacía o si hay archivos nuevos en el directorio.
    
    - Si la colección está vacía, ingiere todos los archivos.
    - Si ya hay contenido, compara los archivos del directorio con los ya procesados
      e ingiere únicamente aquellos que sean nuevos.
    """
    # Verificar si la colección está vacía
    count_result = client.count(collection_name=collection_name)
    if count_result.count == 0:
        print("La base de datos está vacía. Ingestando todos los archivos.")
        ingest_documents(directory)
        return
    
    # Obtener nombres de archivos ya procesados
    processed_files = get_processed_files()
    all_files = glob.glob(os.path.join(directory, "*.md"))
    # Filtrar archivos nuevos (comparamos por el nombre del archivo)
    new_files = [f for f in all_files if os.path.basename(f) not in processed_files]
    
    if new_files:
        print(f"Se han detectado {len(new_files)} archivos nuevos. Ingestando nuevos archivos.")
        ingest_documents(directory, files=new_files)
    else:
        print("No se han detectado nuevos archivos. La base de datos ya contiene todo el contenido.")
