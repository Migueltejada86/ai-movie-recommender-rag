import json
import numpy as np
import faiss

from services.tmdb_client import get_popular_movies
from services.embedding_service import get_embedding

movies = get_popular_movies()

movie_data = []
embeddings = []

print("Generando embeddings...\n")

for movie in movies:

    title = movie.get("title", "")

    overview = movie.get("overview", "")

    if not overview:
        continue

    print(f"Procesando: {title}")

    embedding = get_embedding(overview)

    embeddings.append(embedding)

    movie_data.append({
    "title": title,
    "overview": overview,
    "poster_path": movie.get("poster_path"),
    "rating": movie.get("vote_average"),
    "release_date": movie.get("release_date")
})

embeddings_np = np.array(
    embeddings,
    dtype="float32"
)

dimension = embeddings_np.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings_np)

faiss.write_index(
    index,
    "data/faiss.index"
)

np.save(
    "data/movie_embeddings.npy",
    embeddings_np
)

with open(
    "data/movies.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        movie_data,
        f,
        ensure_ascii=False,
        indent=2
    )

print("\n✅ Vector store creado.")