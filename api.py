from fastapi import FastAPI
from services.tmdb_client import search_movie

from services.rag_service import rag_movie_search

app = FastAPI()

# =========================
# Ruta inicial
# =========================

@app.get("/")
def home():

    return {
        "message": "Migue AI Movie API funcionando 🚀"
    }

# =========================
# Buscar película
# =========================

@app.get("/movie/{movie_name}")
def get_movie(movie_name: str):

    results = search_movie(movie_name)

    return results

# =========================
# Preguntas AI
# =========================

@app.get("/ask")
def ask_ai(query: str):

    response = rag_movie_search(query)

    return {
        "query": query,
        "response": response
    }