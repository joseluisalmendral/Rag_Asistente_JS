# 📖 Sistema RAG para Soporte de Alumnos en JavaScript

## 📌 Descripción
Este proyecto implementa un **sistema RAG (Retrieval-Augmented Generation)** diseñado para brindar soporte a alumnos mediante la recuperación de fragmentos de un temario de **JavaScript** y la generación de respuestas con inteligencia artificial.

El sistema permite a los alumnos realizar consultas sobre el temario y recibir respuestas basadas en contenido relevante previamente indexado en una base de datos vectorial.

## 🚀 Tecnologías Utilizadas
### 1️⃣ **LangChain**
- **¿Qué es?** Un framework para construir aplicaciones de IA con capacidad de razonamiento y recuperación de información.
- **Ventajas:**
  - Facilita la carga y procesamiento de documentos en distintos formatos.
  - Permite dividir el contenido en fragmentos óptimos para la búsqueda y generación de respuestas.

### 2️⃣ **Qdrant** (Base de Datos Vectorial)
- **¿Qué es?** Un motor de búsqueda vectorial para almacenar y recuperar embeddings de manera eficiente.
- **Ventajas:**
  - Altamente optimizado para búsquedas semánticas.
  - Soporta indexación eficiente de grandes volúmenes de datos.
  - Compatible con múltiples modelos de embeddings.

### 3️⃣ **OpenAI GPT-4o**
- **¿Qué es?** Un modelo de lenguaje avanzado de OpenAI utilizado para generar respuestas basadas en la consulta del usuario.
- **Ventajas:**
  - Capacidad de generar respuestas precisas y contextualizadas.
  - Se puede ajustar su temperatura para controlar la creatividad de las respuestas.


## 📂 Estructura del Proyecto
```
📁 proyecto-rag
│── .env                # Variables de entorno (API Keys)
│── main.py             # Archivo principal (consulta e interacción con el usuario)
│── db_ingestion.py     # Ingestión de documentos y almacenamiento en Qdrant
│── temario/            # Carpeta con documentos Markdown del temario de JavaScript
│── requirements.txt    # Dependencias del proyecto
```

## 🎯 Propósito del Código
### 📌 **1. Procesamiento de Documentos Markdown** (`db_ingestion.py`)
- Extrae contenido de los archivos `.md` del temario.
- Divide los documentos en fragmentos óptimos para su búsqueda.
- Genera embeddings para cada fragmento utilizando el modelo `text-embedding-ada-002` de OpenAI.
- Almacena los fragmentos en **Qdrant** junto con sus embeddings.
- Detecta nuevos archivos y actualiza la base de datos automáticamente.

### 📌 **2. Consulta y Generación de Respuestas** (`main.py`)
- Toma la consulta del usuario.
- Genera el embedding de la consulta.
- Busca fragmentos relevantes en la base de datos de **Qdrant**.
- Pasa el contenido relevante al modelo **GPT-4o** para generar una respuesta estructurada.
- Devuelve la respuesta al usuario.

## ⚙️ Instalación y Configuración
### 🔹 **1. Clonar el repositorio**
```bash
git clone https://github.com/usuario/proyecto-rag.git
cd proyecto-rag
```

### 🔹 **2. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 🔹 **3. Configurar Variables de Entorno**
Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
```env
OPENAI_API_KEY=tu_clave_openai
QDRANT_API_KEY=tu_clave_qdrant
QDRANT_ENDPOINT=tu_endpoint_qdrant
```

### 🔹 **4. Ingestar los documentos**
```bash
python main.py
```
Si el sistema detecta nuevos documentos en `temario/`, los procesará automáticamente.

### 🔹 **5. Realizar Consultas**
Al ejecutar `main.py`, el sistema estará listo para recibir consultas desde la terminal.
```bash
USER --> ¿Cómo funciona el hoisting en JavaScript?
CHAT --> En JavaScript, el hoisting es un comportamiento donde las declaraciones de variables y funciones se mueven al principio de su contexto de ejecución...
```

## 🛠 Posibles Mejoras
✅ Implementar un frontend con **React** para hacer consultas vía web.
✅ Incluir soporte para otros lenguajes de programación en el temario.
✅ Agregar más modelos de embeddings para mejorar la precisión de las respuestas.



