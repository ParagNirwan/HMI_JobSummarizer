import DataCleaning
import visualization

sectors = {
    "Information Technology":
        {
            'Software Developer': [
                'Python',
                'Java',
                'C++',
                'JavaScript',
                'HTML',
                'CSS',
                'SQL',
                'Git',
                'Problem-solving',
                'Object-oriented programming',
                'Web development',
                'Data structures',
                'Algorithms',
                'Debugging',
                'Testing',
                'Agile methodologies',
                'Version control',
                'API integration',
                'UI/UX design',
                'Teamwork'
            ],
            'Data Analyst': [
                'Python',
                'R',
                'SQL',
                'Data manipulation',
                'Data visualization',
                'Statistical analysis',
                'Data cleaning',
                'Data modeling',
                'Data mining',
                'Excel',
                'Tableau',
                'Power BI',
                'Critical thinking',
                'Problem-solving',
                'Communication',
                'Data-driven decision making',
                'Predictive modeling',
                'Data interpretation',
                'Data presentation',
                'Report generation'
            ],
            'Network Administrator': [
                'Network protocols',
                'Network troubleshooting',
                'Cisco',
                'Firewalls',
                'Routing and switching',
                'Network security',
                'TCP/IP',
                'DNS',
                'VPN',
                'Wireless networks',
                'LAN/WAN',
                'Network monitoring',
                'Network hardware',
                'Network configuration',
                'Problem-solving',
                'Documentation',
                'Communication',
                'Analytical thinking',
                'Collaboration',
                'Time management'
            ],
            'Cybersecurity Engineer': [
                'Network security',
                'Firewalls',
                'Intrusion detection/prevention',
                'Vulnerability assessment',
                'Penetration testing',
                'Encryption',
                'Security audits',
                'Risk management',
                'Incident response',
                'Malware analysis',
                'SIEM',
                'Security frameworks (NIST, ISO)',
                'Identity and access management',
                'Forensics',
                'Ethical hacking',
                'Security policies',
                'Web application security',
                'Linux',
                'Scripting (Python, Bash)',
                'Problem-solving'
            ],
            'Cloud Architect': [
                'AWS',
                'Azure',
                'Google Cloud',
                'Cloud infrastructure',
                'Virtualization',
                'Containerization',
                'Networking',
                'Security',
                'Storage systems',
                'Scalability',
                'High availability',
                'Disaster recovery',
                'Automation (Terraform, CloudFormation)',
                'DevOps',
                'Monitoring',
                'Cost optimization',
                'Microservices',
                'Serverless architecture',
                'Load balancing',
                'Troubleshooting'
            ],
            'AI/ML Engineer': [
                'Machine learning',
                'Deep learning',
                'Python',
                'TensorFlow',
                'PyTorch',
                'Data preprocessing',
                'Feature engineering',
                'Model development',
                'Model evaluation',
                'Natural Language Processing',
                'Computer Vision',
                'Algorithm development',
                'Statistical analysis',
                'Data visualization',
                'Data analysis',
                'Problem-solving',
                'Debugging',
                'Collaboration',
                'Communication',
                'Research skills'
            ],
            'UI/UX Designer': [
                'User research',
                'Wireframing',
                'Prototyping',
                'Interaction design',
                'Usability testing',
                'Visual design',
                'Graphic design',
                'Typography',
                'Color theory',
                'Responsive design',
                'User-centered design',
                'Design thinking',
                'Adobe Creative Suite',
                'Sketch',
                'InVision',
                'Figma',
                'HTML',
                'CSS',
                'JavaScript',
                'Collaboration'
            ],
            'DevOps Engineer': [
                'Linux',
                'Scripting (Python, Bash)',
                'Containerization (Docker)',
                'Orchestration (Kubernetes)',
                'CI/CD (Jenkins, GitLab)',
                'Infrastructure as Code (Terraform, Ansible)',
                'Cloud platforms (AWS, Azure, GCP)',
                'Monitoring and log management (ELK, Prometheus)',
                'Networking',
                'Security',
                'Version control (Git)',
                'Agile methodologies',
                'Collaboration',
                'Problem-solving',
                'Automation',
                'Troubleshooting',
                'Release management',
                'Performance optimization',
                'Scalability'
            ],
            'Full Stack Developer': [
                'HTML',
                'CSS',
                'JavaScript',
                'Python',
                'Node.js',
                'React',
                'Angular',
                'RESTful APIs',
                'Databases (SQL, MongoDB)',
                'Backend frameworks (Flask, Django, Express)',
                'Frontend frameworks (React, Angular, Vue)',
                'Version control (Git)',
                'UI/UX design',
                'Testing',
                'Agile methodologies',
                'Problem-solving',
                'Debugging',
                'Collaboration',
                'Communication',
                'Time management'
            ],
            'IT Project Manager': [
                'Project management',
                'Agile methodologies',
                'Scrum',
                'Stakeholder management',
                'Risk management',
                'Budgeting',
                'Resource allocation',
                'Communication',
                'Team management',
                'Problem-solving',
                'Strategic planning',
                'Quality assurance',
                'Negotiation',
                'Leadership',
                'Time management',
                'Documentation',
                'Presentation skills',
                'Change management',
                'Conflict resolution',
                'Critical thinking'
            ]
        }
    ,

    "Healthcare":
        {
            'Registered Nurse': [
                'Patient care',
                'Medical terminology',
                'Medication administration',
                'Wound care',
                'Vital signs monitoring',
                'Intravenous therapy',
                'Patient assessment',
                'Documentation',
                'Infection control',
                'Communication skills',
                'Critical thinking',
                'Problem-solving',
                'Empathy',
                'Teamwork',
                'Time management',
                'Patient education',
                'Emergency response',
                'Ethics',
                'Cultural sensitivity',
                'Adaptability'
            ],
            'Medical Laboratory Technician': [
                'Laboratory testing',
                'Specimen collection',
                'Microscopy',
                'Quality control',
                'Lab equipment operation',
                'Data analysis',
                'Sample processing',
                'Documentation',
                'Troubleshooting',
                'Infection control',
                'Communication skills',
                'Attention to detail',
                'Critical thinking',
                'Time management',
                'Technical skills',
                'Analytical skills',
                'Problem-solving',
                'Safety procedures',
                'Medical terminology',
                'Teamwork'
            ],
            'Physical Therapist': [
                'Patient assessment',
                'Treatment planning',
                'Therapeutic exercises',
                'Manual therapy techniques',
                'Gait training',
                'Pain management',
                'Patient education',
                'Functional mobility',
                'Injury prevention',
                'Rehabilitation',
                'Documentation',
                'Communication skills',
                'Interpersonal skills',
                'Critical thinking',
                'Problem-solving',
                'Empathy',
                'Adaptability',
                'Teamwork',
                'Professional ethics',
                'Research skills'
            ],
            'Pharmacist': [
                'Medication dispensing',
                'Prescription review',
                'Pharmaceutical calculations',
                'Drug interactions',
                'Patient counseling',
                'Medication therapy management',
                'Pharmacy operations',
                'Inventory management',
                'Adverse event monitoring',
                'Pharmacokinetics',
                'Documentation',
                'Communication skills',
                'Attention to detail',
                'Problem-solving',
                'Critical thinking',
                'Ethics',
                'Time management',
                'Patient safety',
                'Drug information resources',
                'Teamwork'
            ],
            'Medical Coder': [
                'ICD-10-CM coding',
                'CPT coding',
                'Medical terminology',
                'Healthcare billing systems',
                'Anatomy and physiology',
                'Medical record analysis',
                'Documentation',
                'Coding guidelines',
                'Auditing',
                'Compliance',
                'Attention to detail',
                'Critical thinking',
                'Problem-solving',
                'Analytical skills',
                'Communication skills',
                'Time management',
                'Ethics',
                'Adaptability',
                'Teamwork',
                'Technical skills'
            ],
            'Radiologic Technologist': [
                'Diagnostic imaging',
                'Radiation safety',
                'Patient positioning',
                'Image quality assessment',
                'Equipment operation',
                'Anatomy knowledge',
                'Patient care',
                'Medical terminology',
                'Emergency procedures',
                'Documentation',
                'Communication skills',
                'Critical thinking',
                'Problem-solving',
                'Attention to detail',
                'Adaptability',
                'Teamwork',
                'Ethics',
                'Quality assurance',
                'Time management',
                'Interpersonal skills'
            ],
            'Occupational Therapist': [
                'Patient assessment',
                'Treatment planning',
                'Functional assessments',
                'Therapeutic activities',
                'Adaptive equipment',
                'Splinting',
                'Patient education',
                'Home modifications',
                'Workplace ergonomics',
                'Documentation',
                'Communication skills',
                'Interpersonal skills',
                'Critical thinking',
                'Problem-solving',
                'Empathy',
                'Teamwork',
                'Time management',
                'Adaptability',
                'Professional ethics',
                'Research skills'
            ],
            'Medical Transcriptionist': [
                'Medical terminology',
                'Transcription software',
                'Typing speed',
                'Grammar and punctuation',
                'Attention to detail',
                'Medical record analysis',
                'Editing and proofreading',
                'HIPAA regulations',
                'Communication skills',
                'Time management',
                'Critical thinking',
                'Problem-solving',
                'Adaptability',
                'Teamwork',
                'Computer skills',
                'Ethics',
                'Research skills',
                'Medical knowledge',
                'Listening skills',
                'Interpersonal skills'
            ],
            'Dental Hygienist': [
                'Oral prophylaxis',
                'Periodontal assessment',
                'Radiography',
                'Scaling and root planing',
                'Patient education',
                'Oral health assessment',
                'Infection control',
                'Anesthesia administration',
                'Dental charting',
                'Documentation',
                'Communication skills',
                'Attention to detail',
                'Critical thinking',
                'Problem-solving',
                'Adaptability',
                'Teamwork',
                'Time management',
                'Ethics',
                'Patient care',
                'Instrument sterilization'
            ],
            'Healthcare Administrator': [
                'Healthcare management',
                'Financial management',
                'Healthcare regulations',
                'Strategic planning',
                'Budgeting',
                'Human resources',
                'Healthcare policies',
                'Data analysis',
                'Project management',
                'Communication skills',
                'Problem-solving',
                'Leadership',
                'Teamwork',
                'Ethics',
                'Critical thinking',
                'Decision-making',
                'Organizational skills',
                'Interpersonal skills',
                'Time management',
                'Negotiation'
            ]
        }
}


def get_sector(job_description):
    job_description = job_description.lower()
    count = {key: 0 for key in sectors}
    for sector, keywords in sectors.items():
        for keyword in keywords:
            if keyword in job_description:
                count[sector] = count[sector] + 1
    distribution = [cat + " : " + str(count[cat]) for cat in count if count[cat] > 0]
    print("----list of sectors with matching keywords-----")
    print(distribution)
    max_sect = max(count, key=count.get)
    print("Job Category: ", max_sect, "(", count[max_sect], ")")
    return max_sect


def get_job(job_description):
    job_description = job_description.lower()
    sector_count = {key: 0 for key in sectors}
    job_count = {}
    for sector, jobs in sectors.items():
        for job, skills in jobs.items():
            for skill in skills:
                if skill.lower() in job_description.split():
                    sector_count[sector] = sector_count[sector] + 1
    sect_dist = [cat + " : " + str(sector_count[cat]) for cat in sector_count if sector_count[cat] > 0]
    print("----list of sectors with matching keywords-----")
    print(sect_dist)
    max_sect = max(sector_count, key=sector_count.get)

    job_sect = sectors[max_sect]
    for job,skills in job_sect.items():
        job_count[job] = 0
        for skill in skills:
            print("check skill",skill)
            if skill.lower() in job_description.split():
                print("matched skill",skill)
                job_count[job] = job_count[job] + 1

    job_dist = [job + " : " + str(job_count[job]) for job in job_count if job_count[job] > 0]
    print("----list of jobs in -----",max_sect)
    print(job_dist)
    max_job = max(job_count, key=job_count.get)
    print("Job: ", max_job, "(", job_count[max_job], ")")
    return max_sect


# Categorize job ads
filtered_jobs = []
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
                if current_key is not None:
                    result[current_key.strip()] += ' ' + line.strip()

        # job_count = job_count + 1
        job_string = ''
        for key, value in result.items():
            if key.__contains__('Job Description') or key.__contains__('about us') or key.__contains__(
                    'requirement profile') or key.__contains__('Job requirement') or key.__contains__(
                'Basic knowledge') or key.__contains__(
                'What you bring') \
                    or key.__contains__('tasks include') or key.__contains__(
                'Advanced knowledge') or key.__contains__('Expert knowledge') \
                    or key.__contains__('Requirement') or key.__contains__('requirements') or key.__contains__(
                'she expects') or key.__contains__('out'):
                job_string = job_string + key.strip() + ": " + value.strip() + "\n"
        filtered_jobs.append(job_string)

all_sect = {key: 0 for key in sectors}
for job in filtered_jobs:
    print(f"{job}")
    category = get_job(job)
    all_sect[category] = all_sect[category] + 1
    print("-" * 200)

print("Each sector and its number of jobs to be clustered")
print(all_sect)

sum_of_all = 0
for each_sect in all_sect:
    sum_of_all = sum_of_all + all_sect.get(each_sect)
print("Total categorized:", sum_of_all)

vsn_of_jobs = "visualisation of " + str(sum_of_all) + " jobs"
visualization.visualize_jobs(all_sect, "Sectors", "No of jobs", vsn_of_jobs)
