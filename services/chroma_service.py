import chromadb

from services.embedding_service import get_embedding
from services.tmdb_client import get_popular_movies

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_PATH = BASE_DIR / "chroma_db"

client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.get_or_create_collection(
    name="movies"
)


def build_chroma_collection():

    movies = get_popular_movies()

    for movie in movies:

        title = movie.get("title", "")

        overview = movie.get("overview", "")

        if not overview:
            continue

        poster_path = movie.get("poster_path")
        rating = movie.get("vote_average")
        release_date = movie.get("release_date")

        text = f"{title}. {overview}"

        embedding = get_embedding(text)

        try:

            collection.add(
                ids=[str(movie["id"])],
                embeddings=[embedding],
                documents=[overview],
                metadatas=[{
                    "title": title,
                    "poster_path": poster_path,
                    "rating": rating,
                    "release_date": release_date,
                    "overview": overview
                }]
            )

        except Exception:
            pass

    print("✅ ChromaDB creada")


# ========= AUTO BUILD =========

count = collection.count()

print(f"Películas en Chroma: {count}")

if count == 0:
    print("⚠️ Chroma vacía. Construyendo...")
    build_chroma_collection()


def search_movies(query, n_results=5):

    embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results