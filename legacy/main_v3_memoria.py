from services.tmdb_client import search_movie, get_movie_recommendations
from services.memory_manager import add_favorite_movie, load_memory
from services.llm_service import ask_movie_expert

movie_name = input("Película que te gustó: ")

search_results = search_movie(movie_name)

movies = search_results.get("results", [])

if not movies:
    print("No encontré películas.")
    exit()

# tomar primera película encontrada
selected_movie = movies[0]

movie_id = selected_movie.get("id")

movie_title = selected_movie.get("title")

add_favorite_movie(movie_title)

print(f"\n🎬 Película encontrada: {movie_title}")

# buscar recomendaciones
recommendation_results = get_movie_recommendations(movie_id)

recommendations = recommendation_results.get("results", [])

recommendation_text = ""

for movie in recommendations[:5]:

    title = movie.get("title", "Sin título")

    release_date = movie.get("release_date", "")

    year = release_date[:4] if release_date else "????"

    overview = movie.get("overview", "Sin descripción")

    rating = movie.get("vote_average", "N/A")

    recommendation_text += f"""
    Título: {title}
    Año: {year}
    Rating: {rating}
    Descripción: {overview}

    """

memory = load_memory()

favorite_movies = memory.get("favorite_movies", [])

prompt = f"""
El usuario tiene estas películas favoritas: {', '.join(favorite_movies)}

la pelicula actual es: {movie_title}

estas recomendaciones similares:
{recommendation_text}
Recomendale películas de forma amigable y explicá brevemente por qué podrían gustarle.
"""

response = ask_movie_expert(prompt, recommendation_text)

print("\n🤖 Recomendaciones AI:\n")
print(response)