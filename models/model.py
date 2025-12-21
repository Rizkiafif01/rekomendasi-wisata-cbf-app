import pandas as pd
import difflib
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Load Data
df = pd.read_csv('../data/destinasi-wisata-indonesia.csv')
print(df.head)

# Fitur yg digunakan
selected_features = ['Place_Name','Description','Category','City']
for feature in selected_features:
   df[feature] = df[feature].fillna('')

# Text Preprocessing
stopword_factory = StopWordRemoverFactory()
stopwords = set(stopword_factory.get_stop_words())

stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)  # hapus angka & simbol
    tokens = text.split()
    tokens = [t for t in tokens if t not in stopwords]
    tokens = [stemmer.stem(t) for t in tokens]
    return ' '.join(tokens)

df['combined_features'] = (
    df['Place_Name'] + ' ' +
    df['Description'] + ' ' +
    df['Category'] + ' ' +
    df['City']
)

df['combined_features'] = df['combined_features'].apply(preprocess_text)

print(df[['Place_Name', 'combined_features']].head())

# Vectorization
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),   # bigram → hasil lebih bagus
    max_df=0.9,
    min_df=2
)

feature_vectors = vectorizer.fit_transform(df['combined_features'])


# Similarity
similarity = cosine_similarity(feature_vectors)

# Rekomendasi Fungsi
def recommend(place_name, n=5):
    place_name = place_name.strip()

    list_of_places = df['Place_Name'].tolist()
    close_match = difflib.get_close_matches(
        place_name, list_of_places, n=1, cutoff=0.6
    )

    if not close_match:
        return ["Nama tempat tidak ditemukan di dataset."]

    index = df[df['Place_Name'] == close_match[0]].index[0]
    similarity_scores = list(enumerate(similarity[index]))

    sorted_places = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )[1:n+1]

    results = []
    for i, (idx, score) in enumerate(sorted_places, start=1):
        results.append(
            f"{i}. {df.iloc[idx]['Place_Name']} "
            f"({df.iloc[idx]['Category']} - {df.iloc[idx]['City']})"
        )

    return results