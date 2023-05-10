import nltk
from textblob.classifiers import NaiveBayesClassifier

# Define the job categories
categories = [
    ('Data Scientist', ['Machine learning', 'statistics', 'programming', 'data analysis', 'data visualization']),
    ('Web Developer', ['HTML', 'CSS', 'JavaScript', 'PHP', 'responsive design']),
    ('Marketing Coordinator', ['Social media', 'email marketing', 'content creation', 'market research', 'analytics']),
    ('Project Manager', ['Budgeting', 'scheduling', 'risk management', 'leadership', 'communication']),
    ('Sales Representative', ['Customer service', 'negotiation', 'lead generation', 'product knowledge', 'closing deals']),
    ('Human Resources Generalist',
     ['Recruitment', 'onboarding', 'employee relations', 'performance management', 'compliance']),
    ('Financial Analyst', ['Financial modeling', 'forecasting', 'budgeting', 'variance analysis', 'data analysis']),
    ('Software Engineer',
     ['Object-oriented programming', 'algorithms', 'debugging', 'software development lifecycle', 'testing']),
    ('Accountant', ['Taxation', 'financial reporting', 'audit', 'accounting software', 'bookkeeping']),
    ('Copywriter', ['SEO', 'content marketing', 'persuasive writing', 'editing', 'proofreading']),
    ('UX Designer', ['User research', 'wireframing', 'prototyping', 'user testing', 'interaction design']),
    ('Customer Service Representative',
     ['Conflict resolution', 'empathy', 'active listening', 'product knowledge', 'ticket management']),
    ('IT Support Specialist',
     ['Troubleshooting', 'hardware and software installation', 'network administration', 'remote support',
      'customer service']),
    ('Supply Chain Analyst',
     ['Inventory management', 'demand forecasting', 'logistics', 'procurement', 'data analysis']),
    ('Social Media Manager',
     ['Community management', 'social listening', 'influencer marketing', 'content strategy', 'analytics']),
    ('Business Analyst',
     ['Requirements gathering', 'process modeling', 'data mapping', 'stakeholder management', 'business intelligence']),
    ('Executive Assistant',
     ['Calendar management', 'travel arrangements', 'event planning', 'correspondence', 'discretion']),
    ('Mechanical Engineer', ['CAD', 'prototyping', 'material science', 'thermodynamics', 'manufacturing']),
    ('Healthcare',
     ['Patient assessment', 'medication administration', 'clinical skills', 'patient education', 'care coordination']),
    ('Graphic Designer', ['Typography', 'branding', 'print design', 'visual identity', 'color theory']),
    ('sales', ['sales', 'salesperson', 'sales associate, sales manager']),
    ('marketing', ['marketing', 'marketing manager', 'marketing coordinator']),
    ('finance', ['finance', 'financial analyst', 'accounting']),
    ('engineering', ['engineering', 'software engineer', 'mechanical engineer, software developer, Java, Oracle']),
    ('Content Strategist', ['Content creation', 'SEO', 'Analytics', 'Marketing', 'Social media']),
    ('Mobile App Developer', ['iOS', 'Android', 'Java', 'Swift', 'Mobile UI']),
    ('Data Engineer', ['ETL', 'Data pipelines', 'Databases', 'Data warehousing', 'Python']),
    ('Administrative Assistant',
     ['Calendar management', 'Meeting coordination', 'Travel arrangements', 'Filing', 'Office management']),
    ('Video Producer', ['Video editing', 'Storyboarding', 'Cinematography', 'Post-production', 'Audio mixing']),
    ('Software Architect',
     ['Software design patterns', 'Microservices', 'Scalability', 'System architecture', 'Programming languages']),
    ('Digital Marketing Manager', ['Email marketing', 'SEO', 'Social media', 'Content marketing', 'Analytics']),
    ('Human Resources Manager',
     ['Employee relations', 'Performance management', 'Training and development', 'Compensation and benefits',
      'Recruiting']),
    ('Data Entry Clerk', ['Data entry', 'Microsoft Excel', 'Database management', 'Keyboarding', 'Attention to detail']),
    ('Cloud Solutions Architect', ['Cloud computing', 'Virtualization', 'Networking', 'Security', 'DevOps']),
    ('Technical Writer', ['Technical documentation', 'Writing', 'Editing', 'Research', 'Subject matter expertise']),
    ('Business Intelligence Analyst',
     ['Data analysis', 'Reporting', 'Data visualization', 'SQL', 'Business intelligence tools']),
    ('Customer Success Manager', ['Customer service', 'Account management', 'Onboarding', 'Retention', 'Upselling']),
    ('Back-end Developer', ['Java', 'Python', 'API development', 'Web servers', 'Database management']),
    ('UI/UX Developer', ['User interface design', 'User experience design', 'Responsive design', 'HTML', 'CSS']),
    ('Product Manager', ['Product development', 'Market research', 'Project management', 'Strategy', 'Communication']),
    ('Technical Support Engineer', ['Troubleshooting', 'Customer service', 'Networks', 'Hardware', 'Software']),
    ('Sales Manager', ['Sales', 'Marketing', 'Team management', 'Negotiation', 'Customer relationship management']),
    ('SEO Specialist', ['SEO', 'Keyword research', 'Analytics', 'Link building', 'Content creation']),
    ('Operations Manager', ['Budgeting', 'Inventory management', 'Logistics', 'Team management', 'Process improvement'])
]

# Create training data
train_data = []
for category, keywords in categories:
    for keyword in keywords:
        train_data.append((keyword, category))
print(train_data)
# Train the classifier
classifier = NaiveBayesClassifier(train_data)

# Test the classifier
test_data = [
    'We need a developer with experience in Java, Spring framework and debugging',
    'Person  needed for developing new marketing strategy',
    'In search of a person with experience in making deals and good negotiation skills',
    'Required person who coordinate and take care of patient, their medication',
]
for job_title in test_data:
    category = classifier.classify(job_title)
    print(f"{job_title} is in the : {category} category.")
