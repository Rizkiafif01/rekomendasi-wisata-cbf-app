import streamlit as st

st.set_page_config(
    page_title="Business Understanding",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Business Understanding")

st.write(
    "Halaman ini menjelaskan pemahaman awal terkait sistem rekomendasi wisata "
    "yang dikembangkan menggunakan metode Content-Based Filtering (CBF)."
)

st.divider()

# =========================
# 1. Pengertian Sistem Rekomendasi CBF
# =========================
with st.container(border=True):
    st.subheader("1. Pengertian Sistem Rekomendasi Menggunakan Content-Based Filtering (CBF)")
    st.write(
        """
        Sistem rekomendasi berbasis **Content-Based Filtering (CBF)** merupakan pendekatan
        yang memberikan rekomendasi berdasarkan **kesesuaian karakteristik atau konten**
        suatu item dengan preferensi pengguna. Dalam metode ini, sistem menganalisis
        atribut atau deskripsi item yang pernah dipilih atau diminati oleh pengguna,
        kemudian merekomendasikan item lain yang memiliki tingkat kemiripan tertinggi.

        Pada konteks rekomendasi wisata, CBF bekerja dengan membandingkan informasi
        destinasi wisata seperti deskripsi, kategori, dan fasilitas untuk menemukan
        destinasi yang relevan dengan pilihan pengguna sebelumnya.
        """
    )

# =========================
# 2. Latar Belakang
# =========================
with st.container(border=True):
    st.subheader("2. Latar Belakang")
    st.write(
        """
        Indonesia memiliki beragam destinasi wisata dengan karakteristik yang berbeda-beda.
        Banyaknya pilihan destinasi sering kali membuat wisatawan mengalami kesulitan
        dalam menentukan tujuan wisata yang sesuai dengan minat dan preferensi mereka.

        Oleh karena itu, diperlukan sebuah sistem rekomendasi yang mampu membantu
        pengguna dalam menemukan destinasi wisata yang relevan secara personal.
        Metode Content-Based Filtering dipilih karena mampu memberikan rekomendasi
        berdasarkan kesamaan konten destinasi tanpa bergantung pada data pengguna lain.
        """
    )

# =========================
# 3. Permasalahan
# =========================
with st.container(border=True):
    st.subheader("3. Permasalahan")
    st.write(
        """
        Permasalahan yang dihadapi dalam pemilihan destinasi wisata antara lain:
        - Banyaknya pilihan destinasi wisata dengan informasi yang beragam  
        - Sulitnya menemukan destinasi yang sesuai dengan minat pengguna  
        - Kurangnya sistem yang mampu memberikan rekomendasi secara personal  
        - Informasi destinasi wisata yang tersebar dan tidak terstruktur  
        """
    )

# =========================
# 4. Tujuan
# =========================
with st.container(border=True):
    st.subheader("4. Tujuan")
    st.write(
        """
        Tujuan dari pengembangan sistem rekomendasi wisata ini adalah:
        - Mengembangkan sistem rekomendasi wisata berbasis Content-Based Filtering  
        - Membantu pengguna menemukan destinasi wisata yang sesuai dengan preferensi  
        - Memanfaatkan informasi konten destinasi wisata secara optimal  
        - Meningkatkan pengalaman pengguna dalam menentukan tujuan wisata  
        """
    )
