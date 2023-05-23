import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from spacy import displacy

# Load job offers from file into pandas dataframe
with open('./Assets/dummy.txt', encoding='utf-8') as f:
    contents = f.readlines()
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Job description to summarize
delimiter = ''
jobs_string = delimiter.join(contents)

# separated_jobs = []
# all_jobs = []
# if jobs_string.__contains__("-----"):
#     jobs_string = re.sub(r'[?]', ':', jobs_string)
#     jobs_string = re.sub(r'[$-]', ',', jobs_string)
#     separated_jobs = re.split(r"-----", jobs_string)
#     job_count = 0
#     for job in separated_jobs:
#         if job != "":
#             job_count = job_count + 1
#             pattern = r"^(.*?):\s*(.*)$"
#             matches = re.findall(pattern, job, re.MULTILINE)
#             filtered_jobs = [{"job": job_count}]
#             for key, value in matches:
#                 if key.__contains__('Job Description') or key.__contains__('Requirements') or key.__contains__('What you bring'):
#                     job = {key: value}
#                     filtered_jobs.append(job)
#             all_jobs.append(filtered_jobs)
#
# for each_job in all_jobs:
#     print(each_job)


separated_jobs = []
all_jobs = []
if jobs_string.__contains__("-----"):
    separated_jobs = re.split(r"-----", jobs_string)
    job_count = 0
    for job in separated_jobs:
        if job != "":
            lines = job.strip().split('\n')
            result = {}
            current_key = None
            for line in lines:
                if ':' in line:
                    current_key, value = line.split(':', 1)
                    result[current_key.strip()] = value.strip()
                else:
                    result[current_key] += ' ' + line.strip()
            job_count = job_count + 1
            filtered_jobs = [{"job": job_count}]
            for key, value in result.items():
                if key.__contains__('Job Description') or key.__contains__('Basic knowledge') or key.__contains__(
                        'What you bring') or key.__contains__('Advanced knowledge') or key.__contains__('Expert knowledge') or key.__contains__('Requirement') or key.__contains__('requirements'):
                    # print(f'{key}: {value}')
                    job = {key: value}
                    filtered_jobs.append(job)
            all_jobs.append(filtered_jobs)

for each_job in all_jobs:
    print(each_job)