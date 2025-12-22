import streamlit as st
from models.model import load_model, recommend, get_places_by_category

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
st.write("Pilih kategori wisata, lalu pilih nama tempat untuk mendapatkan rekomendasi serupa.")

# Dropdown Kategori
kategori_options = [
    "Budaya",
    "Bahari",
    "Cagar Alam",
    "Tempat Ibadah",
    "Taman Hiburan",
    "Pusat Perbelanjaan"]

selected_category = st.selectbox(
    "Pilih Kategori Wisata",
    options=["-- Pilih Kategori --"] + kategori_options
)

# Memunculkan nama tempat
place_name = None

if selected_category != "-- Pilih Kategori --":
    place_list = get_places_by_category(model, selected_category)

    if place_list:
        place_name = st.selectbox(
            "Pilih Nama Tempat Wisata",
            options=["-- Pilih Tempat Wisata --"] + place_list
        )
    else:
        st.warning("Tidak ada tempat wisata untuk kategori ini.")
# tombol rekomendasi
if st.button("🔍 Find Recommendation"):
    if not place_name or place_name == "-- Pilih Tempat Wisata --":
        st.warning("Silakan pilih nama tempat wisata.")
    else:
        with st.spinner("Mencari rekomendasi terbaik..."):
            results = recommend(place_name, model, n=5)

        if not results:
            st.error("Rekomendasi tidak ditemukan.")
        else:
            st.subheader("✨ Rekomendasi Tempat Wisata Serupa")

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
