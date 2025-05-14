<!--
╔══════════════════════════════════════════════════════════╗
║           AI Movie Recommender 🎥 — README               ║
╚══════════════════════════════════════════════════════════╝
-->

# 🎥 AI Movie Recommender

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-%F0%9F%8C%8D-orange)](https://streamlit.io/)  
[![Demo Video](https://img.shields.io/badge/Demo%20Video-Local-green)](./demo.mp4)

> A **hybrid AI** movie recommender—combining content‑based & collaborative filtering—with a sleek dark UI and **voice‑activated** search interface.  

---

## 🚀 Live Demo

<video src="./demo.mp4" controls autoplay loop muted style="max-width:100%; border-radius:8px; box-shadow:0 4px 12px rgba(0,0,0,0.3)"></video>

---

## 📸 Screenshots

| App Interface | Recommendation Cards |
|:----------------------:|:--------------------:|
| <img src="screenshots/voice_search.png" alt="Voice Search" width="400" /> | <img src="screenshots/recommendation_cards.png" alt="Recommendation Cards" width="400" /> |

---

## 🔥 Features

- **🎯 Hybrid Recommendations** – leverages both content‑based (genres, cast, popularity) and collaborative filtering via KNN + SVD :contentReference[oaicite:0]{index=0}  
- **🎤 Voice Search** – speak the movie title; powered by SpeechRecognition & PyAudio :contentReference[oaicite:1]{index=1}  
- **🌑 Dark Theme** – custom CSS for a modern, immersive UI :contentReference[oaicite:2]{index=2}  
- **📊 Dynamic OMDB Integration** – real‑time poster, overview, cast, and IMDb links fetched via OMDB API  
- **🎛️ Genre Filtering** – refine suggestions through multi‑select sidebar filters  

---

## 🛠️ Tech Stack & Skills

| Layer                 | Technologies & Skills                                          |
|-----------------------|----------------------------------------------------------------|
| Frontend & UI         | Streamlit, HTML/CSS, custom theming                            |
| Recommender Engine    | scikit‑learn (StandardScaler, TruncatedSVD, NearestNeighbors)  |
| Data Handling         | pandas, pickle, CSV                                            |
| API Integration       | OMDB API, requests                                             |
| Deployment & Tools    | Git, GitHub                               |

---

## 📦 Installation

```bash
git clone https://github.com/aditya-rai-5/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
