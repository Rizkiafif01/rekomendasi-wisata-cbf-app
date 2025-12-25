# Sistem Rekomendasi Wisata Indonesia (Content-Based Filtering)

Aplikasi ini adalah sistem rekomendasi destinasi wisata di Indonesia yang dibangun menggunakan metode **Content-Based Filtering (CBF)**. Sistem ini membantu pengguna menemukan destinasi wisata yang relevan berdasarkan kemiripan konten atau karakteristik dari tempat wisata tersebut.

## 🌟 Fitur Utama
* **Project Overview**: Penjelasan umum mengenai sistem rekomendasi dan metode yang digunakan.
* **Business Understanding**: Dokumentasi mengenai latar belakang, permasalahan, dan tujuan proyek.
* **Keyword-Based Recommendation**: Memberikan rekomendasi destinasi wisata berdasarkan input kata kunci dari pengguna (misalnya: "pantai", "budaya", "sunset").
* **Cosine Similarity Analysis**: Mengukur tingkat kemiripan antar destinasi menggunakan TF-IDF Vectorizer dan perhitungan Cosine Similarity.

## 🛠️ Teknologi yang Digunakan
Proyek ini dikembangkan dengan teknologi berikut:
* **Python**: Bahasa pemrograman utama.
* **Streamlit**: Framework untuk membangun antarmuka web interaktif.
* **Pandas & Numpy**: Library untuk manipulasi dan analisis data.
* **Scikit-Learn**: Digunakan untuk ekstraksi fitur (TF-IDF) dan perhitungan kemiripan.
* **Sastrawi**: Library untuk proses stemming teks bahasa Indonesia.

## 📂 Susunan Proyek
```text
.
├── app.py                      # File utama aplikasi Streamlit
├── requirements.txt            # Daftar dependensi library
├── data/
│   ├── destinasi-wisata-indonesia.csv      # Dataset mentah
│   └── destinasi-wisata-preprocessed.csv   # Dataset hasil preprocessing
├── models/
│   └── model.py                # Logika model TF-IDF dan Cosine Similarity
├── pages/                      # Halaman-halaman aplikasi Streamlit
│   ├── 01_Business_Understanding.py
│   ├── 02_Data_Understanding.py
│   ├── 03_Data_Preparation.py
│   ├── 04_Recommend.py
│   └── 05_Evaluate.py
└── utils/
    └── preprocessing.py        # Skrip pembantu untuk pengolahan teks

```

## 🚀 Prasyarat Instalasi

1. **Clone repositori ini:**
```bash
git clone [https://github.com/username/rekomendasi-wisata-cbf-app.git](https://github.com/username/rekomendasi-wisata-cbf-app.git)
cd rekomendasi-wisata-cbf-app

```


2. **Buat virtual environment (opsional):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

```


3. **Instal dependensi:**
```bash
pip install -r requirements.txt

```



## 💻 Contoh Penggunaan

1. **Jalankan aplikasi Streamlit:**
```bash
streamlit run app.py

```


2. **Navigasi ke menu Rekomendasi**: Masukkan kata kunci pencarian Anda pada kolom yang tersedia (contoh: "pantai, indah, sunset").
3. **Hasil**: Sistem akan menghitung skor kemiripan dan menampilkan destinasi terbaik yang sesuai dengan kata kunci Anda berdasarkan deskripsi (`clean_text`).

## 🤝 Kontribusi

Kontribusi terbuka bagi siapa saja. Silakan lakukan *fork* pada repositori ini dan ajukan *pull request* jika ingin menambahkan fitur atau memperbaiki bug.
