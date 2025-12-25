import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_model():
    df = pd.read_csv('data/destinasi-wisata-preprocessed.csv')

    required_cols = ['Place_Name', 'Category', 'City', 'clean_text']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Kolom '{col}' tidak ditemukan di dataset.")

    df[required_cols] = df[required_cols].fillna('')

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['clean_text'])

    return df, vectorizer, tfidf_matrix


def recommend_by_keywords(keyword_input, model, n=5):
    df, vectorizer, tfidf_matrix = model

    # keyword: "pantai, indah, sunset" → "pantai indah sunset"
    keywords = keyword_input.lower().replace(',', ' ')

    keyword_vector = vectorizer.transform([keywords])

    similarity_scores = cosine_similarity(keyword_vector, tfidf_matrix)[0]

    ranked_indices = similarity_scores.argsort()[::-1][:n]

    return [
        {
            "name": df.iloc[i]['Place_Name'],
            "category": df.iloc[i]['Category'],
            "city": df.iloc[i]['City'],
            "score": round(float(similarity_scores[i]), 3)
        }
        for i in ranked_indices
    ]
