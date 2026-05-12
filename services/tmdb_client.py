import os
import requests

from dotenv import load_dotenv

# cargar variables .env
load_dotenv()

# obtener API key
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# URL base de TMDB
BASE_URL = "https://api.themoviedb.org/3"


def search_movie(movie_name):

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_name,
        "language": "es-ES"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data

def get_movie_recommendations(movie_id):

    url = f"{BASE_URL}/movie/{movie_id}/recommendations"

    params = {
        "api_key": TMDB_API_KEY,
        "language": "es-ES"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data

def get_popular_movies(pages=10):

    all_movies = []

    for page in range(1, pages + 1):

        url = f"{BASE_URL}/movie/popular"

        params = {
            "api_key": TMDB_API_KEY,
            "language": "es-ES",
            "page": page
        }

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        movies = data.get("results", [])

        all_movies.extend(movies)

    return all_movies