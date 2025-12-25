import streamlit as st
from models.model import load_model, recommend_by_keywords

st.set_page_config(
    page_title="Rekomendasi Wisata",
    layout="wide"
)

@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# Header
st.title("🎯 Sistem Rekomendasi Wisata Indonesia")
st.write(
    "Masukkan kata kunci wisata (dipisahkan dengan koma), "
    "misalnya: `pantai, indah, sunset`."
)

# Input keyword
keyword_input = st.text_input(
    "🔑 Masukkan Keyword Wisata",
    placeholder="contoh: pantai, alam, tenang"
)

# Jumlah rekomendasi
top_k = 5

# Tombol rekomendasi
if st.button("🔍 Find Recommendation"):
    if not keyword_input.strip():
        st.warning("Silakan masukkan minimal satu keyword.")
    else:
        with st.spinner("Mencari rekomendasi terbaik..."):
            results = recommend_by_keywords(
                keyword_input,
                model,
                n=top_k
            )

        if not results:
            st.error("Rekomendasi tidak ditemukan.")
        else:
            st.subheader("✨ Rekomendasi Tempat Wisata")

            for i, r in enumerate(results, start=1):
                st.markdown(
                    f"""
                    **{i}. {r['name']}**  
                    Kategori: `{r['category']}`  
                    Kota: `{r['city']}`  
                    Similarity Score: `{r['score']}`
                    ---
                    """
                )
