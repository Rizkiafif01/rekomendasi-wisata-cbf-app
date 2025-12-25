import streamlit as st
import pandas as pd
from models.model import load_model
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Evaluasi Top-K Recommender",
    layout="centered"
)

@st.cache_resource
def get_model():
    return load_model()

df, vectorizer, tfidf_matrix = get_model()

st.title("📊 Evaluasi Top-K Sistem Rekomendasi Wisata")
st.write(
    """
    Evaluasi dilakukan menggunakan **Top-K Recommendation Evaluation**
    dengan pendekatan **pseudo-query berbasis keyword**.
    
    Relevansi ditentukan berdasarkan **kategori atau kota yang sama**.
    """
)

k = st.selectbox("Pilih nilai K", options=[30,60,90], index=1)
sample_size = 100


def evaluate_top_k_keyword(df, tfidf_matrix, vectorizer, k, sample_size):
    precisions = []
    recalls = []

    test_samples = df.sample(sample_size, random_state=42)

    for _, row in test_samples.iterrows():
        # Pseudo-query dari data
        query_text = f"{row['Category']} {row['City']}"
        query_vector = vectorizer.transform([query_text])

        similarity_scores = cosine_similarity(
            query_vector,
            tfidf_matrix
        )[0]

        ranked_indices = similarity_scores.argsort()[::-1][:k]

        # Item relevan: kategori atau kota sama
        relevant_items = df[
            (df['Category'] == row['Category']) |
            (df['City'] == row['City'])
        ].index.tolist()

        if not relevant_items:
            continue

        hits = len(set(ranked_indices) & set(relevant_items))

        precision = hits / k
        recall = hits / len(relevant_items)

        precisions.append(precision)
        recalls.append(recall)

    return (
        round(sum(precisions) / len(precisions), 4),
        round(sum(recalls) / len(recalls), 4),
        len(precisions)
    )


if st.button("▶️ Jalankan Evaluasi"):
    with st.spinner("Melakukan evaluasi Top-K berbasis keyword..."):
        mean_precision, mean_recall, valid_samples = evaluate_top_k_keyword(
            df,
            tfidf_matrix,
            vectorizer,
            k,
            sample_size
        )

    st.success("Evaluasi selesai")

    col1, col2, col3 = st.columns(3)
    col1.metric("Precision@K", mean_precision)
    col2.metric("Recall@K", mean_recall)
    col3.metric("Jumlah Sampel Valid", valid_samples)

st.markdown(
    """
    ### 🧠 Interpretasi Hasil
    - **Precision@K** menunjukkan proporsi rekomendasi yang relevan terhadap query keyword.
    - **Recall@K** menunjukkan kemampuan sistem menemukan item relevan dari seluruh kandidat.
    - Evaluasi ini menggunakan **pseudo ground truth**, karena dataset tidak memiliki label relevansi eksplisit.
    """
)
