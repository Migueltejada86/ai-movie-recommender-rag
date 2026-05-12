from services.retriever_service import retrieve_movies

from services.llm_service import ask_movie_expert

def rag_movie_search(query):

    docs = retrieve_movies(query)

    context = ""

    for doc in docs:

        context += f"""
        {doc.page_content}

        Metadata:
        {doc.metadata}
        """

    prompt = f"""
    El usuario busca:

    {query}

    Estas películas fueron encontradas:

    {context}

    Recomendá películas y explicá
    por qué coinciden con lo pedido.
    """

    response = ask_movie_expert(
        prompt,
        context
    )

    return response