import chromadb

from services.embedding_service import get_embedding
from services.tmdb_client import get_popular_movies

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="movies"
)


def build_chroma_collection():

    movies = get_popular_movies()

    for movie in movies:

        title = movie.get("title", "")

        print(f"Guardando: {title}")

        overview = movie.get("overview", "")
        if not overview:
            continue
        poster_path = movie.get("poster_path")

        rating = movie.get("vote_average")

        release_date = movie.get("release_date")

        text = f"{title}. {overview}"

        embedding = get_embedding(text)

        collection.add(
            ids=[str(movie["id"])],
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


def search_movies(query, n_results=5):

    embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results