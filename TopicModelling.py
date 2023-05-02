import gensim
from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess


def TModelling(text_corpus):
    tokenized_corpus = [simple_preprocess(text) for text in text_corpus]
    dictionary = corpora.Dictionary(tokenized_corpus)

    # Create a corpus object, which is a bag of words representation of the text corpus
    corpus = [dictionary.doc2bow(text) for text in tokenized_corpus]

    # Build the LDA model
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=2, passes=10)

    # Print the topics and their associated words
    for topic in lda_model.print_topics():
        print(topic)
