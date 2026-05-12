import json
import os

MEMORY_FILE = "memory.json"


def load_memory():

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    return {
        "favorite_movies": []
    }


def save_memory(memory):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:

        json.dump(memory, f, indent=2, ensure_ascii=False)


def add_favorite_movie(movie_title):

    memory = load_memory()

    if movie_title not in memory["favorite_movies"]:

        memory["favorite_movies"].append(movie_title)

    save_memory(memory)