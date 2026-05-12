from services.rag_service import rag_movie_search

response = rag_movie_search(
    "superhéroes oscuros y tecnología"
)

print(response)