import streamlit as st
import pickle
import pandas as pd
import requests
import time
import streamlit.components.v1 as components
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.pipeline import Pipeline
from sklearn.decomposition import TruncatedSVD

# ─── Page Configuration 
st.set_page_config(page_title="🎥 AI Movie Recommender", layout="wide")

# ─── Load Custom CSS 
def load_local_css(fname):
    with open(fname, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_local_css("style.css")

# ─── Data Loading & Preprocessing 
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies       = pd.DataFrame(movies_dict)
data         = pd.read_csv('movie.csv')
similarity   = pickle.load(open('similarity.pkl', 'rb'))
data['genres'] = data['genres'].apply(eval)
data['cast']   = data['cast'].apply(eval)

# ─── Sidebar: Genre Filter 
st.sidebar.header("🎯 Filter Options")
selected_genres = st.sidebar.multiselect(
    "🎬 Genres", sorted({g for sub in data['genres'] for g in sub})
)
filtered = data.copy()
if selected_genres:
    filtered = filtered[
        filtered['genres'].apply(lambda gl: any(g in gl for g in selected_genres))
    ]

# ─── Build Recommendation Pipeline 
features = movies[['popularity', 'vote_average', 'vote_count']]
knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svd', TruncatedSVD(n_components=2)),
    ('knn', NearestNeighbors(n_neighbors=15, metric='cosine'))
])
knn_pipeline.fit(features)

OMDB_API_KEY = "Your API Key"
def get_movie_details(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    res = requests.get(url).json()
    poster   = res.get('Poster')
    overview = res.get('Plot', 'Overview not available.')
    cast     = res.get('Actors', 'Cast not available').split(', ')[:3]
    homepage = f"https://www.imdb.com/title/{res.get('imdbID')}/" if res.get('imdbID') else None
    return poster, overview, cast, homepage

def content_based(idx, cands):
    sims = list(enumerate(similarity[idx]))
    c   = [i for i, _ in sims if i in cands]
    return sorted(c, key=lambda i: similarity[idx][i], reverse=True)[:15]

def collaborative(idx, cands):
    feat = features.iloc[idx].values.reshape(1, -1)
    tf   = knn_pipeline.named_steps['svd'].transform(
             knn_pipeline.named_steps['scaler'].transform(feat))
    _, inds = knn_pipeline.named_steps['knn'].kneighbors(tf)
    return [i for i in inds.flatten() if i in cands][:10]

def get_recommendations(title):
    idx   = movies[movies['title'] == title].index[0]
    cands = filtered.index.tolist()
    cb    = content_based(idx, cands)
    col   = collaborative(idx, cands)
    recs, i, j = [], 0, 0
    while len(recs) < 25 and (i < len(cb) or j < len(col)):
        recs.extend(cb[i:i+3]); i += 3
        recs.extend(col[j:j+2]); j += 2
    return [movies.iloc[k] for k in recs if k != idx]

# ─── Header 
st.markdown("""
<div class="header">
  <img src="https://cdn-icons-png.flaticon.com/512/1179/1179069.png" alt="Logo">
  <h1>AI Movie Recommender</h1>
  <p>Your smart, hybrid movie suggestion engine</p>
</div>
""", unsafe_allow_html=True)

# ─── Movie Selector (All Movies) 
st.subheader("🎞️ Select a Movie")
selected_movie = st.selectbox('📽️ Movie Title:', movies['title'].values)

# ─── Show Recommendations 
def show_recs():
    with st.spinner("Finding top picks..."):
        time.sleep(1)
    recs = get_recommendations(selected_movie)
    st.subheader("✨ Recommended For You")
    for row in recs:
        poster, overview, cast, homepage = get_movie_details(row['title'])
        st.markdown(f"""
            <div class="recommendation-card">
              <img src="{poster}" class="movie-poster">
              <div class="movie-info">
                <h3 class="movie-title">{row['title']}</h3>
                <p class="movie-rating">⭐ {row['vote_average']} ({row['vote_count']} votes)</p>
                <p class="movie-cast"><strong>Cast:</strong> {', '.join(cast)}</p>
                <p class="movie-overview">{overview}</p>
                {f'<a href="{homepage}" class="movie-homepage" target="_blank">🔗 IMDb Page</a>' if homepage else ''}
              </div>
            </div>
        """, unsafe_allow_html=True)

if st.button('🚀 Get Recommendations'):
    show_recs()
