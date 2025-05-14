<!--
╔══════════════════════════════════════════════════════════╗
║           AI Movie Recommender 🎥 — README               ║
╚══════════════════════════════════════════════════════════╝
-->

# 🎥 AI Movie Recommender

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Project-Active-brightgreen.svg)](#)

> **A smart AI-powered movie recommender system** combining collaborative & content-based filtering with real-time **voice search** and **query parameter-based navigation**. Elegant dark UI, OMDB integration, and genre filters included.

---

## 🚀 Live Demo

🎬 Watch the demo below:

<video src="./demo.mp4" controls autoplay loop muted style="max-width:100%; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.3)"></video>

---

## 📸 Screenshots

| Home Page | Movie Cards |
|:---------:|:-----------:|
| <img src="app_interface.png" width="400" alt="Home UI" /> | <img src="screenshot_2005-04-14_091222.png" width="400" alt="Recommendations" /> |

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
