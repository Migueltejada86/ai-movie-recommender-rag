from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector_store = Chroma(
    persist_directory="chroma_db",
    collection_name="movies",
    embedding_function=embedding_model
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

def retrieve_movies(query):

    docs = retriever.invoke(query)

    return docs