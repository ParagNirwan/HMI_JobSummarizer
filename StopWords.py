import DataCleaning
import spacy
import string
from nltk import ngrams
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


separated_jobs = DataCleaning.dataCleaning()

nlp = spacy.load("en_core_web_sm")

def remove_stopwords(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and token.text not in string.punctuation]
    return " ".join(tokens)

# Remove stop words from each string in the list
separated_jobs = [remove_stopwords(job) for job in separated_jobs]

# Print the updated list
for job in separated_jobs:
    print(job)
