# 🎬 Migue AI Movie Assistant

Sistema inteligente de recomendación de películas usando IA.

El proyecto combina:

- API de TMDB
- Embeddings
- ChromaDB
- RAG (Retrieval-Augmented Generation)
- LangChain
- Agentes de IA
- Búsqueda semántica

---

## 🌐 Demo Online

Probalo acá:

🚀 https://ai-movie-recommender-rag-migue.streamlit.app

No requiere instalación local.

---

## 🚀 Funcionalidades

✅ Búsqueda exacta de películas usando TMDB

✅ Recomendaciones automáticas

✅ Búsqueda semántica por ideas o emociones

Ejemplos:

- "películas filosóficas"
- "robots existenciales"
- "historias de superación"
- "algo parecido a Batman"

✅ RAG con embeddings

El sistema recupera películas relevantes desde una base vectorial usando IA.

✅ Agente inteligente de cine

Puede:

- recomendar películas
- encontrar películas similares
- analizar películas
- sugerir por emoción o concepto
- combinar géneros e ideas

✅ Seguridad básica implementada

- sanitización de input
- protección básica contra prompt injection
- rate limiting
- protección contra inputs maliciosos

---

## 🧠 Tecnologías utilizadas

- Python
- Streamlit
- LangChain
- LangGraph
- ChromaDB
- OpenAI API
- FastAPI
- Embeddings

---

## 📂 Arquitectura del proyecto

```txt
TMDB API
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retriever
    ↓
RAG
    ↓
AI Agent
```

## ⚙️ Instalación local

Clonar repositorio:

```bash
git clone URL_DEL_REPO
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear archivo `.env`

```env
OPENAI_API_KEY=tu_api_key
TMDB_API_KEY=tu_api_key
```

Ejecutar aplicación:

```bash
streamlit run app/streamlit_app.py
```

---

## 🎯 Objetivo del proyecto

Proyecto de práctica para aprender:

- AI Engineering
- RAG
- agentes de IA
- vector databases
- búsqueda semántica
- arquitectura de aplicaciones LLM
- seguridad básica para aplicaciones con IA

---

## 🔥 Próximas versiones

- [x] V1 API TMDB
- [x] V2 recomendaciones
- [x] V3 memoria
- [x] V4 Streamlit
- [x] V5 embeddings
- [x] V5.5 FAISS
- [x] V5.7 ChromaDB
- [x] V6 FastAPI
- [x] V7 AI Agent
- [x] V7.5 Seguridad básica
- [ ] V8 memoria persistente
- [ ] V9 autenticación JWT
- [ ] V10 multi-agent
- [ ] V11 workflows autónomos
- [ ] V12 cloud deployment AWS

---

## 💡 Ejemplos de prompts

```txt
algo triste
películas sobre hackers
quiero algo como Interstellar pero más oscuro
una película filosófica
robots existenciales
algo alegre para ver hoy
```

## ✍️ Autor
GitHub: @Migueltejada86