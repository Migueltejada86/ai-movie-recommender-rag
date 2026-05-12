from services.tmdb_client import get_popular_movies

from services.embedding_service import (
    get_embedding,
    cosine_similarity
)

query = input("¿Qué tipo de película buscás?: ")

query_embedding = get_embedding(query)

movies = get_popular_movies()

results = []

for movie in movies:

    title = movie.get("title", "")

    overview = movie.get("overview", "")

    if not overview:
        continue

    movie_embedding = get_embedding(overview)

    similarity = cosine_similarity(
        query_embedding,
        movie_embedding
    )

    results.append({
        "title": title,
        "similarity": similarity
    })

results = sorted(
    results,
    key=lambda x: x["similarity"],
    reverse=True
)

print("\n🎬 Mejores matches:\n")

for movie in results[:5]:

    print(
        f"{movie['title']} "
        f"({movie['similarity']:.2f})"
    )