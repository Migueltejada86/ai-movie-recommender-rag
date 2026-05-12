
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


def get_secret(key):

    try:
        return st.secrets[key]

    except Exception:
        return os.getenv(key)


TMDB_API_KEY = get_secret(
    "TMDB_API_KEY"
)

OPENAI_API_KEY = get_secret(
    "OPENAI_API_KEY"
)
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


from services.rag_service import rag_movie_search
from services.agent_service import ask_agent


from services.tmdb_client import (
    search_movie,
    get_movie_recommendations
)

from services.llm_service import ask_movie_expert

from services.memory_manager import (
    add_favorite_movie,
    load_memory
)

from services.chroma_service import search_movies

# =========== CSS ===========
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

html, body, [class*="css"]  {
    background-color: #141414;
    color: white;
}

h1, h2, h3 {
    font-family: 'Bebas Neue', sans-serif;
    color: #E50914;
    letter-spacing: 2px;
}

.stButton>button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

.stTextInput>div>div>input {
    background-color: #222222;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========== APP ===========
st.title("🎬 Migue AI Movie Assistant")

# =========================================
# RECOMENDACIONES CLÁSICAS
# =========================================

movie_name = st.text_input(
    "Escribí una película"
)

if st.button("Buscar recomendaciones"):

    search_results = search_movie(movie_name)

    movies = search_results.get(
        "results",
        []
    )

    if not movies:

        st.error(
            "No encontré películas."
        )

    else:

        selected_movie = movies[0]

        movie_title = selected_movie.get(
            "title"
        )

        movie_id = selected_movie.get(
            "id"
        )

        st.subheader(
            f"🎥 {movie_title}"
        )

        add_favorite_movie(movie_title)

        recommendation_results = (
            get_movie_recommendations(
                movie_id
            )
        )

        recommendations = (
            recommendation_results.get(
                "results",
                []
            )
        )

        recommendation_text = ""

        for movie in recommendations[:5]:

            title = movie.get(
                "title",
                "Sin título"
            )

            poster_path = movie.get(
                "poster_path"
            )

            release_date = movie.get(
                "release_date",
                ""
            )

            year = (
                release_date[:4]
                if release_date
                else "????"
            )

            overview = movie.get(
                "overview",
                "Sin descripción"
            )

            rating = movie.get(
                "vote_average",
                "N/A"
            )

            st.markdown(
                f"### {title} ({year})"
            )

            st.write(
                f"⭐ Rating: {rating}"
            )

            st.write(overview)

            if poster_path:

                poster_url = (
                    f"https://image.tmdb.org/t/p/w500"
                    f"{poster_path}"
                )

                st.image(
                    poster_url,
                    width=200
                )

            recommendation_text += f"""
            {title}
            {overview}
            """

        memory = load_memory()

        favorite_movies = memory.get(
            "favorite_movies",
            []
        )

        prompt = f"""
        El usuario disfruta:

        {favorite_movies}

        Película actual:
        {movie_title}

        Recomendaciones:
        {recommendation_text}

        Recomendá películas similares.
        """

        ai_response = ask_movie_expert(
            prompt,
            recommendation_text
        )

        st.subheader(
            "🤖 Recomendación AI"
        )

        st.write(ai_response)

# =========================================
# BÚSQUEDA SEMÁNTICA
# =========================================

st.markdown("---")

st.header("🧠 Búsqueda Semántica AI")

semantic_query = st.text_input(
    "Describe una película o sensación"
)

if st.button("Buscar semánticamente"):

    results = search_movies(
        semantic_query
    )
    
    st.subheader(
        "🎬 Resultados"
    )

    movies = results["metadatas"][0]

    for movie in movies:

        title = movie.get("title")

        rating = movie.get("rating")

        release_date = movie.get(
            "release_date",
            ""
        )

        year = (
            release_date[:4]
            if release_date
            else "????"
        )

        poster_path = movie.get(
            "poster_path"
        )

        overview = movie.get(
            "overview",
            ""
        )

        st.markdown(
            f"### {title} ({year})"
        )

        st.write(
            f"⭐ Rating: {rating}"
        )

        st.write(overview)

        if poster_path:

            poster_url = (
                f"https://image.tmdb.org/t/p/w500"
                f"{poster_path}"
            )

            st.image(
                poster_url,
                width=200
            )

# =========================================
# RAG AI MOVIE ASSISTANT
# =========================================

st.markdown("---")

st.header("🤖 AI Movie Expert")

rag_query = st.text_input(
    "Preguntale algo a la IA"
)

if st.button("Consultar AI"):

    with st.spinner("Pensando..."):

        response = rag_movie_search(
            rag_query
        )

    st.subheader("🎬 Respuesta AI")

    st.write(response)

st.markdown("---")

st.header("🤖 AI Movie Agent")

agent_query = st.text_input(
    "Preguntale cualquier cosa al agente y continua charlando con él"
)

if st.button("Consultar agente"):

    with st.spinner("El agente está pensando..."):

        response = ask_agent(agent_query)

    st.subheader("🎬 Respuesta del Agente")

    st.write(response)


st.markdown("---")

st.caption(
    "Este producto utiliza la API de TMDB "
    "pero no está respaldado "
    "ni certificado por TMDB."
)