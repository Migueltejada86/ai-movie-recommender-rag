"""
from tmdb_client import search_movie

movie = input("Película: ")

results = search_movie(movie)

print(results)
"""
""" v2
from tmdb_client import search_movie

movie = input("Película: ")

results = search_movie(movie)

movies = results.get("results", [])

print("\nResultados:\n")

for index, movie_data in enumerate(movies[:5], start=1):

    title = movie_data.get("title", "Sin título")

    release_date = movie_data.get("release_date", "Fecha desconocida")

    year = release_date[:4] if release_date else "????"

    print(f"{index}. {title} ({year})")
"""
""" v3


from tmdb_client import search_movie

movie = input("Película: ")

results = search_movie(movie)

movies = results.get("results", [])

print("\nResultados:\n")

for index, movie_data in enumerate(movies[:5], start=1):

    title = movie_data.get("title", "Sin título")

    release_date = movie_data.get("release_date", "")

    year = release_date[:4] if release_date else "????"

    overview = movie_data.get("overview", "Sin descripción")

    rating = movie_data.get("vote_average", "N/A")

    print(f"{index}. {title} ({year})")
    print(f"⭐ Rating: {rating}")
    print(f"📝 {overview}\n")

    ###
    """

from services.tmdb_client import search_movie
from services.llm_service import ask_movie_expert

user_question = input("Preguntá sobre películas: ")

results = search_movie(user_question)

movies = results.get("results", [])

movie_text = ""

for movie in movies[:5]:

    title = movie.get("title", "Sin título")

    release_date = movie.get("release_date", "")

    year = release_date[:4] if release_date else "????"

    overview = movie.get("overview", "Sin descripción")

    rating = movie.get("vote_average", "N/A")

    movie_text += f"""
    Título: {title}
    Año: {year}
    Rating: {rating}
    Descripción: {overview}

    """

response = ask_movie_expert(user_question, movie_text)

print("\n🤖 Respuesta AI:\n")
print(response)