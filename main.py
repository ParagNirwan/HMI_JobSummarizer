import numpy as np
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from spacy.lang.en.stop_words import STOP_WORDS
import re

# Load job offers from file into pandas dataframe
with open('./Assets/eures_job_desc_en.txt', encoding='utf-8') as f:
    contents = f.readlines()

nlp = spacy.load('en_core_web_sm')


# Define a function to preprocess each job description
def preprocess(text):
    # Remove stopwords and empty spaces, lemmatize, and tokenize using Spacy
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_space]
    return ' '.join(tokens)


# Preprocess each job description
preprocessed_job_descriptions = [preprocess(text) for text in contents]

# Convert the preprocessed job descriptions to a DataFrame
df = pd.DataFrame({'job_description': preprocessed_job_descriptions})

# Define a vectorizer to convert the preprocessed job descriptions to a feature matrix
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['job_description'])

# Cluster the job offers using KMeans
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(X)

# Add the cluster labels to the DataFrame
df['cluster'] = kmeans.labels_

# Summarize each cluster
for i in range(kmeans.n_clusters):
    cluster_df = df[df['cluster'] == i]
    cluster_size = len(cluster_df)
    print(f'Cluster {i}: {cluster_size} job offers')
    print('-' * 40)
    for j, row in cluster_df.sample(min(5, cluster_size)).iterrows():
        print(row['job_description'])
    print('\n')
