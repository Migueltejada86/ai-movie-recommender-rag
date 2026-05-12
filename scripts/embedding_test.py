from services.embedding_service import (
    get_embedding,
    cosine_similarity
)

text1 = "película espacial filosófica"

text2 = "viajes espaciales existenciales"

text3 = "comedia romántica divertida"

embedding1 = get_embedding(text1)

embedding2 = get_embedding(text2)

embedding3 = get_embedding(text3)

similarity_1_2 = cosine_similarity(
    embedding1,
    embedding2
)

similarity_1_3 = cosine_similarity(
    embedding1,
    embedding3
)

print("\nSimilitud 1-2:")
print(similarity_1_2)

print("\nSimilitud 1-3:")
print(similarity_1_3)