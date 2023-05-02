import numpy as np
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from spacy.lang.en.stop_words import STOP_WORDS
import re
from spacy.language import Language
from spacy.lang.en import Language
import TopicModelling

# Load job offers from file into pandas dataframe
with open('./Assets/dummy.txt', encoding='utf-8') as f:
    contents = f.readlines()

nlp = spacy.load('en_core_web_sm')

delimiter = ''
jobs_string = delimiter.join(contents)
jobs_string = jobs_string.replace("\n", " ")
separated_jobs = re.split(r"-----", jobs_string)
separated_jobs = separated_jobs[1:-1]

# Removing Empty Entries
Separated_jobs = [element for element in separated_jobs if element != ""]

y = 1
for x in separated_jobs:
    print(y, ". " + x)
    y = y + 1
    print("-" * 469)

#Topic Modelling and Stop Words removal
processed_jobs = []
for job in separated_jobs:
    doc = nlp(job)
    processed_job = " ".join(token.text for token in doc if not token.is_punct and not token.is_stop)
    processed_jobs.append(processed_job)
print("Cleaned List \n")
for x in processed_jobs:
    print(x)
TopicModelling.TM(processed_jobs)


# Define a function to preprocess each job description
def preprocess(text):
    # Remove stopwords and empty spaces, lemmatize, and tokenize using Spacy
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_space]
    return ' '.join(tokens)


# Preprocess each job description
data = []
processed_jobs_description = [preprocess(text) for text in separated_jobs]
for each_data in processed_jobs_description:
    lines = each_data.splitlines()
    # Initialize an empty list to store the dictionaries
    # Loop through each line and split it into key-value pairs
    for i in range(0, len(lines)):
        if (lines[i] != ""):
            parts = lines[i].split(':')
            key = parts[0]
            if (len(parts) > 1):
                values = parts[1]
            else:
                j = i + 1
                if (j < len(lines)):
                    values = lines[j]
                # values = [v.strip() for v in values]

        # Create a new dictionary and add the key-value pairs
        d = {}
        d[key] = values

        # Append the new dictionary to the list
        data.append(d)
# Print the resulting data
print(data)
# Convert the preprocessed job descriptions to a DataFrame
# df = pd.DataFrame({'job_description': preprocessed_job_descriptions})

# Define a vectorizer to convert the preprocessed job descriptions to a feature matrix
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(df['job_description'])

# Cluster the job offers using KMeans
# kmeans = KMeans(n_clusters=10, random_state=42)
# kmeans.fit(X)

# Add the cluster labels to the DataFrame
# df['cluster'] = kmeans.labels_

# Summarize each cluster
# for i in range(kmeans.n_clusters):
#     cluster_df = df[df['cluster'] == i]
#     cluster_size = len(cluster_df)
#     print(f'Cluster {i}: {cluster_size} job offers')
#     print('-' * 40)
#     for j, row in cluster_df.sample(min(5, cluster_size)).iterrows():
#         print(row['job_description'])
#     print('\n')
