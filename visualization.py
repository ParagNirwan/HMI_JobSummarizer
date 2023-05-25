import matplotlib.pyplot as plt

def visualize_job_requirements(job_requirements):
    skills = job_requirements.keys()
    skill_counts = job_requirements.values()

    plt.bar(skills, skill_counts)
    plt.xlabel('Skills')
    plt.ylabel('Count')
    plt.title('Job Requirements')

    # Rotate x-axis labels if needed
    plt.xticks(rotation=45)

    plt.show()

# Example job requirements
job_requirements = {
    'Python': 5,
    'Data Analysis': 7,
    'Machine Learning': 4,
    'Communication': 6,
    'Problem Solving': 8
}

visualize_job_requirements(job_requirements)
