<!--
╔══════════════════════════════════════════════════════════╗
║           AI Movie Recommender 🎥 — README               ║
╚══════════════════════════════════════════════════════════╝
-->

# 🎥 AI Movie Recommender

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Enabled-purple?logo=scikit-learn)](#)
[![Entertainment](https://img.shields.io/badge/Category-Entertainment-yellow?logo=popos)](#)
[![Status](https://img.shields.io/badge/Project-Active-brightgreen.svg)](#)


> **A smart AI-powered movie recommender system** combining collaborative & content-based filtering. Elegant dark UI, OMDB integration, and genre filters included.

---


## 📸 Screenshots

| Home Page | Movie Cards |
|:---------:|:-----------:|
| <img src="./APP_interface.png" width="450" alt="Home UI" /> | <img src="./movie_box.png" width="450" alt="Recommendations" /> |

---

## 🔥 Features

- 🎯 **Hybrid Recommendation Engine**  
  Combines:
  - *Content-based filtering* (genres, cast, overview)
  - *Collaborative filtering* using KNN + Truncated SVD

- 🔗 **OMDB Integration**  
  Dynamically fetches posters, IMDb links, ratings & cast using OMDB API

- 🎛️ **Genre Filtering**  
  Sidebar filter to narrow down results based on genre(s)

- 🌌 **Dark Mode UI**  
  Custom CSS for an immersive experience

- 🔗 **Smart Query URLs**  
  Search state preserved via `?movie=` query parameters

---

## 🛠️ Tech Stack & Skills Used

| Layer                    | Technologies & Tools                                       |
|--------------------------|------------------------------------------------------------|
| **Frontend & UI**        | Streamlit, HTML/CSS, Dark theme CSS                        |
| **Recommendation Engine**| Scikit-learn: KNN, TruncatedSVD, cosine similarity         |
| **Data Handling**        | pandas, pickle, CSV                                        |
| **External APIs**        | OMDB API, requests                                         |
| **Deployment & DevOps**  | Git, GitHub, Streamlit CLI                                 |

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/aditya-rai-5/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
