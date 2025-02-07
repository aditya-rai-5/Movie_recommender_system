

import streamlit as st
import pickle
import pandas as pd
import requests

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDb API key (Replace 'YOUR_TMDB_API_KEY' with your actual API key)

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

        # Extract poster path
        poster_path = movie_data.get("poster_path")
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

        # Extract overview
        overview = movie_data.get("overview", "Overview not available.")

        # Extract homepage URL
        homepage = movie_data.get("homepage", None)

        # Extract top 3 cast members
        cast = credits_data.get("cast", [])
        main_characters = [actor["name"] for actor in cast[:3]] if cast else ["Cast not available"]

        return poster_url, overview, main_characters, homepage
    return None, "Overview not available.", ["Cast not available"], None

def content_based_recommendations(movie, k=5):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:k+1]
    return pd.DataFrame([{ 
        'title': movies.iloc[i[0]].title, 
        'movie_id': movies.iloc[i[0]].movie_id, 
        'vote_average': movies.iloc[i[0]].vote_average, 
        'vote_count': movies.iloc[i[0]].vote_count 
    } for i in movies_list])

def collaborative_recommendations(movie, k=5):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_cluster = movies.loc[movie_index, 'cluster']
    cluster_movies = movies[movies['cluster'] == movie_cluster]
    cluster_movies = cluster_movies.sort_values(by='score', ascending=False)
    cluster_movies = cluster_movies[cluster_movies['title'] != movie]
    return cluster_movies[['title', 'movie_id', 'vote_average', 'vote_count']].head(k)

def recommendations(movie, k_content=3, k_collaborative=3):
    content_recs = content_based_recommendations(movie).head(k_content)
    collaborative_recs = collaborative_recommendations(movie, k=k_collaborative)
    combined_recs = pd.concat([content_recs, collaborative_recs]).drop_duplicates(subset=['movie_id'])
    return combined_recs[['title', 'movie_id', 'vote_average', 'vote_count']].head(k_content + k_collaborative)

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:', movies['title'].values
)

if st.button('Recommend'):
    recommended_movies = recommendations(selected_movie_name)

    for index, row in recommended_movies.iterrows():
        poster_url, overview, main_characters, homepage = get_movie_details(row['movie_id'])

        col1, col2 = st.columns([1, 3])  # Layout for poster and details
        with col1:
            if poster_url:
                st.image(poster_url, width=150)  # Show movie poster
            else:
                st.write("No poster available")
        
        with col2:
            st.subheader(row['title'])
            st.write(f"⭐ **Rating:** {row['vote_average']} ({row['vote_count']} votes)")
            st.write(f"🎭 **Main Characters:** {', '.join(main_characters)}")  # Display top 3 actors
            st.write(f"📖 **Overview:** {overview}")  # Display movie overview
            
            # Display the homepage link if available
            if homepage:
                st.markdown(f"[🔗 Official Homepage]({homepage})", unsafe_allow_html=True)
