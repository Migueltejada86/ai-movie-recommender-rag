import numpy as np

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def get_embedding(text):
    # obtener embedding de un texto, conviertendolo en un vector numérico
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def cosine_similarity(vec1, vec2):
    # mide la similitud entre dos vectores, devuelve un valor entre -1 y 1
    # cuanto más cerca de 1, más similares son los vectores
    vec1 = np.array(vec1)

    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )