import gensim
from gensim import corpora

# create a list of all jobs
def TM(jobs):


    # define the number of topics
    num_topics = 3

    # create a list to store the topics for each job
    job_topics = []

    # loop through each job
    for job in jobs:
        # create a list of words for the current job
        job_words = job.split()

        # create a dictionary from the job words
        job_dict = corpora.Dictionary([job_words])

        # create a bag-of-words representation of the job
        job_bow = job_dict.doc2bow(job_words)

        # create a LDA model from the bag-of-words representation
        lda_model = gensim.models.LdaModel([job_bow], num_topics=num_topics, id2word=job_dict)

        # get the top topics for the current job
        top_topics = lda_model.show_topics(num_topics=num_topics)

        # add the top topics to the job_topics list
        job_topics.append(top_topics)

    # print the top topics for each job
    for i, job in enumerate(jobs):
        print(f"Job {i+1} Topics: {job_topics[i]}")
