import os
import openai
from dotenv import load_dotenv
from db_ingestion import update_database_if_new_files, generate_embeddings, client, collection_name

# Cargar variables de entorno (por si se necesitan en el main)
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada. Por favor, configúrala.")

def query_rag(query, limit=5):
    """
    Realiza una consulta en la colección de Qdrant utilizando el embedding de la consulta,
    recupera fragmentos relevantes y genera una respuesta utilizando GPT-4 de OpenAI.
    
    Parámetros:
      query (str): Consulta realizada por el usuario.
      limit (int): Número de fragmentos a recuperar.
    
    Retorna:
      str: Respuesta generada por GPT-4.
    """
    # Generar el embedding para la consulta
    query_embedding = generate_embeddings([query])[0]
    
    # Realizar la búsqueda en Qdrant utilizando el embedding de la consulta
    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_embedding.tolist(),
        limit=limit,
        with_payload=True
    )
    
    # Concatenar el texto de los fragmentos recuperados para formar el contexto
    retrieved_texts = [point.payload["text"] for point in search_result]
    context = "\n\n".join(retrieved_texts)
    
    # Construir el prompt para GPT-4, incluyendo el contexto y la consulta
    prompt = f"""
Contexto: {context}

Pregunta: {query}
Respuesta:"""
    response_llm = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system", 
                "content": "Eres un asistente experto en el temario introductorio de la escuela. Responde en texto plano y SOLO a temas relacionados con dicho temario. Para cualquier otra consulta, responde: 'Lo siento, no puedo ayudarte con eso.'"
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.10
    )
    
    return response_llm.choices[0].message.content

if __name__ == "__main__":
    # Actualizar (o crear) la base de datos solo si hay nuevos archivos o está vacía
    update_database_if_new_files("temario/introductorio")
    
    print("\nSistema RAG listo. Ingresa tus consultas (escribe 'salir' para terminar).")
    
    # Bucle interactivo para recibir consultas desde el terminal
    while True:
        user_query = input("\nUSER --> ")
        if user_query.lower() in ["salir", "exit", "quit"]:
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break
        
        respuesta = query_rag(user_query)
        print(f"\nCHAT --> {respuesta} \n")