import DataCleaning
import regex


# def job_details_separated():
#     all_jobs = []
#     separated_jobs = DataCleaning.dataCleaning()
#     job_count = 0
#     for job in separated_jobs:
#         if job != "":
#             lines = job.strip().split('\n')
#             result = {}
#             current_key = None
#             for line in lines:
#                 if ':' in line:
#                     current_key, value = line.split(':', 1)
#                     result[current_key.strip()] = value.strip()
#                 else:
#                     result[current_key.strip()] += ' ' + line.strip()
#             job_count = job_count + 1
#             filtered_jobs = [{"job": job_count}]
#             for key, value in result.items():
#                 if key.__contains__('Job Description') or key.__contains__('Basic knowledge') or key.__contains__(
#                         'What you bring') \
#                         or key.__contains__('tasks include') or key.__contains__(
#                     'Advanced knowledge') or key.__contains__('Expert knowledge') \
#                         or key.__contains__('Requirement') or key.__contains__('requirements') or key.__contains__(
#                     'she expects'):
#                     # print(f'{key}: {value}')
#                     job = {key: value}
#                     filtered_jobs.append(job)
#             all_jobs.append(filtered_jobs)


# for each_job in all_jobs:
#     for job_desc in each_job:
#         if job_desc.get("Requirements for Applicant") != "":
#             print(job_desc)
#     print("-"*200)

all_jobs = []
separated_jobs = DataCleaning.dataCleaning()
# job_count = 0
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
                result[current_key.strip()] += ' ' + line.strip()
        # job_count = job_count + 1
        job_string = ''
        for key, value in result.items():
            if key.__contains__('Job Description') or key.__contains__('Job requirement') or key.__contains__('Basic knowledge') or key.__contains__(
                    'What you bring') \
                    or key.__contains__('tasks include') or key.__contains__(
                'Advanced knowledge') or key.__contains__('Expert knowledge') \
                    or key.__contains__('Requirement') or key.__contains__('requirements') or key.__contains__(
                'she expects') or key.__contains__('out'):
                job_string = job_string + key.strip() + ": " + value.strip() + "\n"
        all_jobs.append(job_string)

for job in all_jobs:
    print(job)


