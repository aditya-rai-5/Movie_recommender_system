import streamlit as st
import pickle
import pandas as pd
import requests
import time

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }

        body {
            background-color:white  !important;
            color: white !important;
        }

        .stButton>button {
            background-color: #ff5733;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #ff2e00;
            transform: scale(1.05);
        }

        .recommendation-card {
            display: flex;
            align-items: flex-start;
            margin-bottom: 20px;
            background: rgba(255, 255, 220, 0.5);
            border-radius: 10px;
            padding: 10px;
            border-color: rgba(240,233,254,0.7);
            animation: fadeIn 0.5s ease-in-out;
        }

        .recommendation-card:hover {
            transform: scale(1.05);
        }

        .movie-poster {
            border-radius: 10px;
            margin-right: 20px;
            width: 120px;
        }

        .movie-poster:hover{
            transform: scale(1.40);
        }

        .movie-info {
            display: flex;
            flex-direction: column;
        }

        .movie-title {
            font-size: 24px;
            font-style: serif;
            font-weight: 600;
            margin: 0;
        }

        .movie-rating {
            font-size: 18px;
            font-weight: 400;
            margin: 5px 0;
            color: #ffb400;
        }

        .movie-overview {
            font-size: 14px;
            font-weight: 300;
            color: light;
            line-height: 1.5;
        }

        [theme]
        base="dark"


        .movie-homepage {
            margin-top: 15px;
            color: #1db954;
            text-decoration: none;
            font-weight: bold;
            font-size: 18px;
            transition: color 0.3s ease-in-out, transform 0.2s ease-in-out;
            display: inline-block;
        }

        .movie-homepage:hover {
            color: #17a34a;
            transform: scale(1.05);
            text-decoration: underline;
        }

        .movie-homepage:active {
            color: #147a3a;
        }


        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 0.2;
                transform: translateY(10px);
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDb API key
TMDB_API_KEY = "029020e5a5e075338d1029cb7fc7a862"

def get_movie_details(movie_id):
    """Fetch movie poster, overview, main characters, and homepage URL from TMDb API."""
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}"
    
    movie_response = requests.get(movie_url)
    credits_response = requests.get(credits_url)

    if movie_response.status_code == 200 and credits_response.status_code == 200:
        movie_data = movie_response.json()
        credits_data = credits_response.json()

        poster_path = movie_data.get("poster_path")
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

        overview = movie_data.get("overview", "Overview not available.")
        homepage = movie_data.get("homepage", None)
        cast = credits_data.get("cast", [])
        main_characters = [actor["name"] for actor in cast[:3]] if cast else ["Cast not available"]

        return poster_url, overview, main_characters, homepage
    return None, "Overview not available.", ["Cast not available"], None

def content_based_recommendations(movie, k=30):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:k+1]
    return pd.DataFrame([{ 
        'title': movies.iloc[i[0]].title, 
        'movie_id': movies.iloc[i[0]].movie_id, 
        'vote_average': movies.iloc[i[0]].vote_average, 
        'vote_count': movies.iloc[i[0]].vote_count 
    } for i in movies_list])

def collaborative_recommendations(movie, k=20):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_cluster = movies.loc[movie_index, 'cluster']
    cluster_movies = movies[movies['cluster'] == movie_cluster]
    cluster_movies = cluster_movies.sort_values(by='score', ascending=False)
    cluster_movies = cluster_movies[cluster_movies['title'] != movie]
    return cluster_movies[['title', 'movie_id', 'vote_average', 'vote_count']].head(k)

def recommendations(movie, k_content=30, k_collaborative=20):
    content_recs = content_based_recommendations(movie).head(k_content)
    collaborative_recs = collaborative_recommendations(movie, k=k_collaborative)
    combined_recs = pd.concat([content_recs, collaborative_recs]).drop_duplicates(subset=['movie_id'])
    return combined_recs[['title', 'movie_id', 'vote_average', 'vote_count']].head(k_content + k_collaborative)


st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        time.sleep(2)
    
    recommended_movies = recommendations(selected_movie_name)
    
    for i in range(len(recommended_movies)):
        row = recommended_movies.iloc[i]
        poster_url, overview, main_characters, homepage = get_movie_details(row['movie_id'])
        homepage_link = f'<a href="{homepage}" class="movie-homepage" target="_blank">🔗 Official Homepage</a>' if homepage else ''
        st.markdown(
            f"""
            <div class="recommendation-card">
                <img src="{poster_url}" alt="{row['title']}" class="movie-poster">
                <div class="movie-info">
                    <h3 class="movie-title">{row['title']}</h3>
                    <p class="movie-rating">⭐ {row['vote_average']} ({row['vote_count']} votes)</p>
                    <p class="movie-overview">{overview}</p>
                    <p class='homepage'>{homepage_link}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
