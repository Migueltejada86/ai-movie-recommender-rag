from services.chroma_service import search_movies

results = search_movies(
    "plomero"
)

print(results)