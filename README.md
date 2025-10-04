# Fake News Detection System

## Overview
This project is a **web-based Fake News Detection System** that allows users to check whether a news article is **real or fake**. It uses **machine learning** for text classification, a **Flask backend** for API handling, and a **modern HTML/CSS/JS frontend** for user interaction.

---

## Features
- **Detect Page:** Users can paste news text and get real-time predictions.
- **Responsive Frontend:** Modern and clean UI with Home, About, Detect, and Contact pages.
- **Backend API:** Flask API powered by a pre-trained ML model.
- **Machine Learning Model:** Uses vectorization (TF-IDF or CountVectorizer) and classification (like Logistic Regression or similar) to predict news authenticity.
- **CORS Enabled:** Frontend and backend communicate smoothly.
- **Error Handling:** Handles invalid inputs and backend errors gracefully.

---

## Technology Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask, Flask-CORS  
- **Machine Learning:** scikit-learn, joblib  
- **Model Storage:** `.pkl` files for vectorizer and classifier

---

## Project Structure

d:\fakeNewsDetection
├── backend
│ ├── app.py # Flask API
│ ├── fake_news_model.pkl # Trained ML model
│ └── vectorizer.pkl # Text vectorizer
├── frontend
│ ├── index.html # Home page
│ ├── about.html # About page
│ ├── detect.html # Detect page
│ ├── contact.html # Contact page
│ ├── css\style.css # Styles
│ └── js\script.js # Frontend JS
└── README.md # Project documentation


