# 🎬 Movie Recommendation System (GloVe + Feature Weighting)

This project is a movie recommendation system with a graphical interface built using **Tkinter**. It uses **GloVe word embeddings** to evaluate semantic similarity between movie synopses, along with structured metadata like genres, directors, cast, and release years to enhance recommendation accuracy.

## 🚀 Features

- GUI for selecting a movie and displaying recommendations
- Semantic similarity using pre-trained GloVe vectors
- Metadata weighting for genres, director, cast, and release year
- Top 5 similar movie recommendations shown in real-time
- Expandable dataset via `movies_data.py`

## 🧠 How It Works

1. **Semantic Similarity**: The model uses GloVe vectors to compute average embeddings of movie synopses.
2. **Feature-Based Weighting**:
   - **Genres**: One-hot encoded and compared with cosine similarity
   - **Director**: Binary similarity (exact match)
   - **Cast**: Jaccard similarity on the cast list
   - **Year**: Scaled similarity based on time difference
3. All features are combined into a weighted similarity score to produce final rankings.

## 📁 Project Structure

```
├── movie_recommendation_gui.py # Main GUI application logic
├── movies_data.py # Movie metadata used for recommendation
├── glove.6B.50d.txt # Pre-trained GloVe file (50-dimensional, not included)
```

## 💾 Requirements

- Python 3.x
- `numpy`
- `scikit-learn`
- `gensim`
- `tkinter` (comes with standard Python installations)

Install dependencies via pip:

```bash
pip install numpy scikit-learn gensim
```

  Note: This project uses the `glove.6B.50d.txt` file, which can be downloaded from the GloVe website. Place the file in the appropriate path specified in `movie_recommendation_gui.py`.

## 🖥️ Running the App

1. Download and place the GloVe file in the correct path (edit `glove_path` if needed).
2. Run the GUI:

```bash
python movie_recommendation_gui.py
```

3. Select a movie from the dropdown and click "Get Recommendations" to view the top 5 similar titles.

## 🔧 Customization

You can easily expand the dataset by editing `movies_data.py` to add new titles, genres, synopses, and metadata. Just follow the existing dictionary structure.

## 📜 License

This project is open for educational and experimental purposes. Attribution is appreciated if you use or modify it.

---

Enjoy discovering similar movies with the power of word embeddings and classic film metadata!

```vbnet
Let me know if you'd like a version with badges, contribution guidelines, or GitHub Pages support.
```
