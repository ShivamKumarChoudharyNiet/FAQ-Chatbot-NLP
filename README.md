# AI FAQ Chatbot Engine 🤖

An interactive, NLP-driven FAQ Chatbot built as part of the **CodeAlpha Software Development Internship** (Task 2). The system processes user input using custom tokenization and scores intents using text similarity math algorithms.

## ✨ Features
- **NLP Preprocessing:** Custom text cleaning, punctuation removal, tokenization, and stopword filtering.
- **Intent Matching Engine:** Uses Vectorization and Cosine Similarity algorithms to find the closest matching query.
- **Interactive UI:** A modern chat interface styled with Tailwind CSS for seamless user interaction.
- **Smart Fallback:** Fallback response system when user queries do not meet the minimum similarity threshold.

## 🛠️ Tech Stack & Concepts
- **Backend:** Python, Flask Framework
- **Core Algorithms:** Vectorization, Dot Product, Cosine Similarity, Text Normalization
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)

## 📦 Local Installation & Setup
1. Clone the repository or download the source code.
2. Open terminal in the directory and install Flask:
   ```bash
   pip install flask
