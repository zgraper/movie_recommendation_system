import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder
from gensim.models import KeyedVectors
from movies_data import movies  # Import the movie dataset

# Load GloVe vectors into Gensim-compatible format
def load_glove_model(glove_file):
    print("Loading GloVe model...")
    glove_vectors = {}
    with open(glove_file, "r", encoding="utf-8") as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.array(values[1:], dtype=np.float32)
            glove_vectors[word] = vector
    print("GloVe model loaded successfully!")
    return glove_vectors

# Define path to GloVe file
glove_path = r"C:\Users\zgrap\MSAI631\recommendation\glove.6B.50d.txt"
glove_model = load_glove_model(glove_path)
vector_size = 50  # Since we're using glove.6B.50d.txt

# Function to compute similarity scores
def compute_similarity(movie1, movie2):
    # Compute GloVe similarity (synopsis-based)
    def get_avg_embedding(text):
        words = text.lower().split()
        vectors = [glove_model[word] for word in words if word in glove_model]
        return np.mean(vectors, axis=0) if vectors else np.zeros(vector_size)

    vector1 = get_avg_embedding(movie1["synopsis"])
    vector2 = get_avg_embedding(movie2["synopsis"])
    text_sim = cosine_similarity([vector1], [vector2])[0][0]

    # Ensure genres are lists and not empty
    genre1 = movie1.get("genre", [])  # Update to match "genre" key
    genre2 = movie2.get("genre", [])

    # Convert genres to a proper 2D array
    genres_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    genres_encoded = genres_encoder.fit_transform([[",".join(genre1)], [",".join(genre2)]])  # Convert to strings
    
    genre_sim = cosine_similarity([genres_encoded[0]], [genres_encoded[1]])[0][0]

    # Compute Director Similarity
    director_sim = 1 if movie1["director"] == movie2["director"] else 0

    # Compute Cast Similarity
    cast_sim = len(set(movie1["cast"]).intersection(set(movie2["cast"]))) / len(set(movie1["cast"]).union(set(movie2["cast"])))

    # Compute Year Similarity (Scaled)
    year_sim = 1 - (abs(movie1["year"] - movie2["year"]) / 100)

    # Weighted Similarity Score
    total_similarity = (text_sim * 0.5) + (genre_sim * 0.2) + (director_sim * 0.15) + (cast_sim * 0.1) + (year_sim * 0.05)
    
    return total_similarity

# Get movie recommendations
def get_recommendations(selected_movie_title):
    try:
        selected_movie = next(movie for movie in movies if movie["title"] == selected_movie_title)

        # Compute similarity scores for all movies
        similarities = [(movie["title"], compute_similarity(selected_movie, movie)) for movie in movies if movie != selected_movie]

        # Sort by highest similarity
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Get top 5 recommendations
        recommendations = [title for title, _ in similarities[:5]]
        return recommendations
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return []

# Function to display recommendations
def show_recommendations():
    selected_movie = movie_dropdown.get()
    if not selected_movie:
        messagebox.showwarning("Warning", "Please select a movie!")
        return

    recommendations = get_recommendations(selected_movie)
    result_text.set("\n".join(recommendations))

# ------------------- Tkinter GUI -------------------
root = tk.Tk()
root.title("Movie Recommendation System (GloVe + Feature Weighting)")
root.geometry("500x400")

# Dropdown menu for movie selection
ttk.Label(root, text="Select a Movie:", font=("Arial", 12)).pack(pady=10)
movie_dropdown = ttk.Combobox(root, values=[movie["title"] for movie in movies], width=40)
movie_dropdown.pack(pady=5)

# Recommend button
ttk.Button(root, text="Get Recommendations", command=show_recommendations).pack(pady=10)

# Results display
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=("Arial", 12), foreground="blue")
result_label.pack(pady=10)

# Run GUI
root.mainloop()