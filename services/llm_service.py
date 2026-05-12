from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

chat = ChatOpenAI(model="gpt-4o-mini")


def ask_movie_expert(user_question, movies):

    prompt = f"""
    Sos un experto en cine.

    El usuario preguntó:
    {user_question}

    Estas son algunas películas encontradas:

    {movies}

    Respondé de forma clara y útil.
    """

    response = chat.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content