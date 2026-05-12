from pathlib import Path
import chromadb

from services.embedding_service import (
    get_embedding
)

from services.tmdb_client import (
    get_popular_movies
)

# ==========================
# PATH ABSOLUTO
# ==========================

BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

CHROMA_PATH = (
    BASE_DIR / "chroma_db"
)

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.get_or_create_collection(
    name="movies"
)


# ==========================
# BUILD DB
# ==========================

def build_chroma_collection():

    movies = get_popular_movies()

    for movie in movies:

        movie_id = str(movie["id"])

        # Evita duplicados
        exists = collection.get(
            ids=[movie_id]
        )

        if exists["ids"]:
            continue

        title = movie.get(
            "title",
            ""
        )

        print(
            f"Guardando: {title}"
        )

        overview = movie.get(
            "overview",
            ""
        )

        if not overview:
            continue

        poster_path = movie.get(
            "poster_path"
        )

        rating = movie.get(
            "vote_average"
        )

        release_date = movie.get(
            "release_date"
        )

        text = (
            f"{title}. "
            f"{overview}"
        )

        embedding = get_embedding(
            text
        )

        collection.add(
            ids=[movie_id],
            embeddings=[embedding],
            documents=[overview],
            metadatas=[{
                "title": title,
                "poster_path": poster_path,
                "rating": rating,
                "release_date": release_date
            }]
        )

    print("✅ ChromaDB creada")


# ==========================
# SEARCH
# ==========================

def search_movies(
    query,
    n_results=5
):

    # Si está vacía,
    # la construye sola
    count = collection.count()

    embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    print(results)

    return results



"""
    if count == 0:

        print(
            "⚠️ Chroma vacía. "
            "Creando colección..."
        )

        build_chroma_collection()

    embedding = get_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[
            embedding
        ],
        n_results=n_results
    )

    return results"""