from services.retriever_service import retrieve_movies

query = "robots filosóficos"

results = retrieve_movies(query)

print(f"Resultados encontrados: {len(results)}")

if not results:
    print("No se encontraron documentos")

for doc in results:

    print(doc.page_content)

    print(doc.metadata)

    print("-" * 50)