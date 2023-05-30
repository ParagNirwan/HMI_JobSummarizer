import DataCleaning
import visualization

sectors = {
        "Information Technology": [
            "software", "developer", "programmer", "coding", "web development",
            "data analyst", "data scientist", "machine learning", "artificial intelligence",
            "cybersecurity", "networking", "cloud computing", "database",
            "front-end", "back-end", "full stack", "mobile app", "UI/UX",
            "agile", "scrum", "devops", "testing", "automation",
            "python", "java", "javascript", "c#", "c++",
            "php", "ruby", "html", "css", "sql",
            "linux", "unix", "windows", "git", "docker",
            "aws", "azure", "big data", "data mining", "data visualization",
            "iot", "blockchain", "virtual reality", "augmented reality", "web security",
            "software architecture", "system administration", "network administration", "server management", "algorithm", "it skills",",ms office"
        ],

        "Healthcare": [
            "nurse", "doctor", "physician", "surgeon", "pharmacist",
            "medical", "dental", "healthcare", "hospital", "clinic", "patient care",
            "pharmacy", "medical research", "clinical trials", "diagnostics", "vaccine",
            "epidemiology", "public health", "genetics", "bioinformatics", "biotechnology",
            "pharmaceutical", "pharmacology", "anatomy", "physiology", "pathology",
            "radiology", "oncology", "neurology", "cardiology", "pediatrics",
            "geriatrics", "nursing", "midwifery", "dentistry", "optometry",
            "allied health", "medical device", "health informatics", "telemedicine", "healthcare management",
            "clinical data management", "drug discovery", "medical writing", "regulatory affairs", "quality assurance",
            "patient advocacy", "medical coding", "healthcare consulting", "rehabilitation", "emergency medicine"
        ],

        "Engineering": [
            "engineer", "mechanical", "electrical", "civil", "chemical",
            "aerospace", "structural", "industrial", "automotive", "robotics",
            "manufacturing", "materials", "mechatronics", "process", "design",
            "CAD", "simulation", "project management", "energy", "environmental",
            "quality control", "automation", "control systems", "instrumentation", "maintenance",
            "power systems", "renewable energy", "nanotechnology", "biomedical", "telecommunications",
            "building services", "structural analysis", "geotechnical", "water resources", "transportation",
            "computer engineering", "software engineering", "data engineering", "systems engineering", "electronics",
            "mechanics", "thermodynamics", "fluid dynamics", "optics", "mathematics",
            "programming", "algorithms", "problem-solving", "technical drawing", "innovation"
        ],

        "Financial": [
            "finance", "banking", "investment", "financial services", "wealth management",
            "financial analysis", "risk management", "asset management", "portfolio management", "financial planning",
            "investment banking", "trading", "derivatives", "equities", "fixed income",
            "insurance", "actuarial", "taxation", "audit", "accounting",
            "financial reporting", "financial modeling", "valuation", "mergers and acquisitions", "private equity",
            "hedge funds", "compliance", "regulatory", "treasury", "capital markets",
            "commercial banking", "retail banking", "credit analysis", "financial technology", "fintech",
            "payment systems", "cryptocurrency", "blockchain", "financial risk", "credit risk",
            "derivatives trading", "quantitative analysis", "financial markets", "investment management",
            "fund management",
            "corporate finance", "economic analysis", "financial consulting", "financial advisory", "wealth advisor"
        ],

        "Education": [
            "education", "teaching", "learning", "instruction", "curriculum",
            "school", "college", "university", "academic", "student",
            "research", "e-learning", "online learning", "educational technology", "pedagogy",
            "classroom", "lesson planning", "assessment", "special education", "early childhood education",
            "secondary education", "higher education", "adult education", "education policy", "educational leadership",
            "educational psychology", "education administration", "educational research", "academic writing",
            "literacy",
            "numeracy", "educational assessment", "classroom management", "educational consulting",
            "education technology",
            "distance learning", "instructional design", "educational resources", "teacher training",
            "educational programs",
            "education reform", "educational equity", "educational psychology", "inclusive education",
            "multicultural education",
            "STEM education", "language education", "physical education", "art education", "music education"
        ],

        "Manufacturing": [
            "manufacturing", "production", "assembly", "operations", "supply chain",
            "quality control", "lean manufacturing", "six sigma", "process improvement", "continuous improvement",
            "automation", "robotics", "machining", "fabrication", "logistics",
            "inventory management", "material handling", "product development", "product design",
            "industrial engineering",
            "manufacturing engineering", "maintenance", "safety", "occupational health", "sustainability",
            "efficiency", "cost reduction", "manufacturing systems", "production planning", "workforce management",
            "standardization", "root cause analysis", "value stream mapping", "equipment maintenance",
            "supply chain management",
            "lean principles", "quality assurance", "regulatory compliance", "packaging", "warehouse management",
            "lean tools", "process optimization", "facility management", "continuous manufacturing",
            "supply chain optimization",
            "inventory control", "manufacturing technology", "product lifecycle management", "engineering drawings",
            "CAD/CAM"
        ],

        "Retail": [
            "retail", "e-commerce", "online shopping", "brick and mortar", "customer service",
            "visual merchandising", "inventory management", "store operations", "point of sale", "omnichannel",
            "supply chain", "logistics", "warehouse management", "order fulfillment", "inventory control",
            "product management", "category management", "pricing strategy", "promotions", "consumer behavior",
            "market research", "sales analysis", "data analytics", "customer experience", "loyalty programs",
            "social media marketing", "digital marketing", "website optimization", "SEO", "paid advertising",
            "customer relationship management", "retail analytics", "retail technology", "payment processing",
            "fraud prevention",
            "retail operations", "retail merchandising", "store layout", "retail trends", "inventory planning",
            "retail strategy", "e-commerce platforms", "online marketplaces", "mobile commerce", "personalization",
            "fulfillment centers", "last-mile delivery", "returns management", "order tracking",
            "cross-border e-commerce"
        ],

        "Consulting": [
            "consulting", "management consulting", "strategy consulting", "business consulting", "advisory services",
            "strategic planning", "problem-solving", "organizational development", "process improvement",
            "change management",
            "business analysis", "market research", "data analysis", "financial consulting",
            "human resources consulting",
            "technology consulting", "IT consulting", "digital transformation", "project management", "risk management",
            "performance management", "business development", "client relations", "industry analysis",
            "competitive analysis",
            "market entry", "business planning", "market strategy", "operations consulting", "supply chain consulting",
            "marketing consulting", "sales consulting", "financial analysis", "cost optimization", "outsourcing",
            "leadership development", "talent management", "training and development", "customer experience consulting",
            "CRM consulting",
            "strategic partnerships", "sustainability consulting", "process optimization", "governance and compliance",
            "business intelligence",
            "knowledge management", "stakeholder management", "public sector consulting", "healthcare consulting",
            "energy consulting"
        ],

        "Media": [
            "media", "entertainment", "film", "television", "music",
            "broadcasting", "digital media", "content creation", "content production", "streaming",
            "journalism", "reporting", "editing", "screenwriting", "cinematography",
            "animation", "visual effects", "video production", "sound production", "post-production",
            "marketing", "advertising", "public relations", "social media", "branding",
            "event management", "live production", "artistic direction", "talent management", "casting",
            "music production", "music composition", "music performance", "radio", "podcasting",
            "gaming", "interactive media", "photography", "graphic design", "web design",
            "media planning", "media buying", "film festivals", "content distribution", "audience engagement",
            "creative writing", "storytelling", "celebrity management", "fashion", "sports media"
        ],

        "Telecommunications": [
            "telecommunications", "networking", "telecom infrastructure", "wireless communication", "telephony",
            "mobile networks", "fixed-line networks", "broadband", "fiber optics", "satellite communication",
            "5G", "4G", "LTE", "VoIP", "Internet of Things",
            "telecom equipment", "network security", "data centers", "cloud computing", "virtualization",
            "network architecture", "network management", "network monitoring", "network optimization",
            "bandwidth management",
            "telecom protocols", "telecom software", "telecom standards", "voice services", "data services",
            "telecom operations", "telecom engineering", "telecom projects", "telecom planning", "telecom consulting",
            "telecom regulatory", "telecom policy", "telecom licensing", "telecom vendors", "telecom solutions",
            "telecom service providers", "telecom integration", "telecom testing", "telecom maintenance",
            "telecom support",
            "telecom billing", "telecom customer care", "telecom sales", "telecom marketing", "telecom strategy"
        ],

        "Government public admin": [
            "government", "public administration", "public policy", "public sector", "public service",
            "policy analysis", "legislation", "regulation", "governance", "public finance",
            "public management", "public affairs", "public administration reform", "government programs",
            "government operations",
            "public budgeting", "public procurement", "public sector consulting", "policy development",
            "public administration ethics",
            "political science", "public administration theory", "public administration research",
            "public administration leadership", "government relations",
            "public sector economics", "public sector finance", "public sector accountability",
            "public sector innovation", "public sector performance",
            "public sector planning", "public sector evaluation", "government policy analysis", "public sector reform",
            "public sector management",
            "public sector decision-making", "public sector governance", "public sector ethics", "public sector law",
            "public sector leadership",
            "public sector strategy", "public sector communication", "public sector marketing",
            "public sector human resources", "public sector information technology",
            "public sector project management", "public sector risk management", "public sector security",
            "public sector transparency", "public sector sustainability"
        ],

        "Renewable energy": [
            "renewable energy", "solar power", "wind energy", "hydropower", "biomass",
            "geothermal energy", "tidal energy", "energy storage", "energy efficiency", "sustainable energy",
            "clean energy", "renewable power generation", "renewable energy technologies", "renewable energy projects",
            "renewable energy systems",
            "renewable energy policy", "renewable energy financing", "renewable energy markets",
            "renewable energy integration", "renewable energy infrastructure",
            "renewable energy planning", "renewable energy consulting", "renewable energy research",
            "renewable energy development", "renewable energy deployment",
            "renewable energy innovation", "renewable energy investments", "renewable energy regulations",
            "renewable energy incentives", "renewable energy economics",
            "renewable energy assessment", "renewable energy analysis", "renewable energy monitoring",
            "renewable energy maintenance", "renewable energy operations",
            "renewable energy grid integration", "renewable energy storage systems",
            "renewable energy project management", "renewable energy technology evaluation",
            "renewable energy market trends",
            "renewable energy solutions", "renewable energy consulting", "renewable energy policy-making",
            "renewable energy advocacy", "renewable energy education",
            "renewable energy workforce", "renewable energy certifications", "renewable energy training",
            "renewable energy awareness", "renewable energy impact assessment"
        ],

        "Transportation logistics": [
            "transportation", "logistics", "supply chain", "freight", "shipping",
            "transportation management", "warehouse management", "inventory management", "distribution",
            "fleet management",
            "supply chain management", "demand planning", "procurement", "order fulfillment", "last-mile delivery",
            "international logistics", "customs clearance", "cross-border transportation",
            "transportation infrastructure", "transportation technology",
            "freight forwarding", "cargo transportation", "air freight", "ocean freight", "rail transportation",
            "road transportation", "intermodal transportation", "express delivery", "third-party logistics", "3PL",
            "inventory optimization", "route optimization", "load optimization", "reverse logistics",
            "cold chain logistics",
            "e-commerce logistics", "logistics consulting", "transportation planning", "transportation analytics",
            "transportation security",
            "logistics automation", "supply chain visibility", "inventory tracking", "order management",
            "warehouse automation",
            "logistics network design", "risk management", "sustainability in logistics", "transportation regulations",
            "logistics performance measurement"
        ],

        "Hospitality tourism": [
            "hospitality", "tourism", "hotel", "resort", "restaurant",
            "travel", "accommodation", "hospitality management", "customer service", "guest relations",
            "event management", "food and beverage", "catering", "front desk", "housekeeping",
            "tourism industry", "tourism marketing", "tourism development", "tourism planning", "tourism promotion",
            "travel agency", "tour operator", "destination management", "revenue management", "sales and marketing",
            "hospitality operations", "hotel management", "restaurant management", "hospitality finance",
            "hospitality technology",
            "hospitality consulting", "hospitality training", "hospitality trends", "hospitality customer experience",
            "hospitality branding",
            "hotel reservations", "guest services", "hospitality recruitment", "hospitality events", "cruise industry",
            "tourist attractions", "hospitality entrepreneurship", "sustainable tourism", "ecotourism",
            "hospitality analytics",
            "hospitality innovation", "hospitality leadership", "hospitality quality management",
            "hospitality operations management", "hospitality risk management"
        ],

        "Automotive": [
            "automotive", "automobile", "vehicle", "car", "automotive industry",
            "automotive engineering", "automotive design", "automotive manufacturing", "automotive technology",
            "automotive components",
            "automotive systems", "automotive electronics", "automotive software", "automotive testing",
            "vehicle development",
            "vehicle production", "vehicle maintenance", "vehicle safety", "vehicle performance", "automotive research",
            "automotive innovation", "autonomous vehicles", "electric vehicles", "hybrid vehicles", "connected cars",
            "automotive supply chain", "automotive logistics", "automotive sales", "automotive marketing",
            "automotive aftermarket",
            "automotive dealership", "automotive service", "automotive repair", "automotive customization",
            "automotive accessories",
            "automotive financing", "automotive insurance", "automotive leasing", "automotive fleet management",
            "automotive regulations",
            "automotive emissions", "automotive sustainability", "automotive quality control",
            "automotive manufacturing processes", "automotive assembly",
            "automotive paint", "automotive materials", "automotive ergonomics", "automotive interior design",
            "automotive exterior design"
        ],

        "Real estate": [
            "real estate", "property", "residential", "commercial", "real estate market",
            "real estate investment", "real estate development", "real estate finance", "property management",
            "real estate brokerage",
            "real estate sales", "real estate leasing", "real estate consulting", "real estate valuation",
            "real estate transactions",
            "real estate law", "real estate regulations", "real estate appraisal", "real estate marketing",
            "real estate investment trust",
            "real estate portfolio", "real estate analysis", "real estate trends", "real estate economics",
            "real estate asset management",
            "real estate construction", "real estate project management", "real estate negotiations",
            "real estate investment strategies", "real estate software",
            "real estate technology", "real estate data analysis", "real estate market research",
            "residential properties", "commercial properties",
            "real estate rental", "real estate listings", "real estate agents", "real estate brokers",
            "real estate professionals",
            "real estate investment opportunities", "real estate networking", "real estate financing",
            "real estate insurance", "real estate inspections",
            "real estate regulations", "real estate compliance", "real estate sustainability",
            "real estate industry news", "real estate conferences"
        ],

        "Food and beverages": [
            "food",
            "food service",
            "restaurant management",
            "culinary arts",
            "hospitality",
            "bartending",
            "barista",
            "waitstaff",
            "sommelier",
            "catering",
            "banquet",
            "chef",
            "cook",
            "line cook",
            "sous chef",
            "executive chef",
            "pastry chef",
            "baker",
            "catering manager",
            "restaurant manager",
            "food and beverage manager",
            "general manager",
            "kitchen manager",
            "front of house manager",
            "bar manager",
            "wine steward",
            "restaurant server",
            "bartender",
            "barista",
            "waiter",
            "waitress",
            "hostess",
            "busser",
            "dishwasher",
            "food runner",
            "sommelier",
            "banquet server",
            "catering assistant",
            "food and beverage director",
            "event coordinator",
            "food scientist",
            "food technologist",
            "quality control",
            "food safety",
            "nutritionist",
            "menu planner",
            "food writer",
            "food photographer",
            "restaurant critic",
            "food stylist",
            "dietary manager",
            "food service supervisor",
            "food production",
            "inventory management"
        ],

        "Fashion and apparel": [
            "fashion design",
            "fashion merchandising",
            "apparel production",
            "garment manufacturing",
            "textile design",
            "fashion marketing",
            "fashion buyer",
            "fashion stylist",
            "fashion coordinator",
            "fashion photographer",
            "fashion blogger",
            "fashion journalist",
            "fashion illustrator",
            "fashion model",
            "pattern making",
            "fashion showroom",
            "fashion retail",
            "visual merchandising",
            "fashion branding",
            "fashion pr",
            "fashion event",
            "fashion consultant",
            "fashion editor",
            "fashion stylist",
            "fashion assistant",
            "fashion designer",
            "fashion illustrator",
            "fashion photographer",
            "fashion stylist",
            "fashion coordinator",
            "fashion buyer",
            "fashion merchandiser",
            "fashion marketer",
            "fashion trend analyst",
            "fashion publicist",
            "fashion blogger",
            "fashion influencer",
            "fashion retail manager",
            "fashion sales associate",
            "fashion store manager",
            "fashion store assistant",
            "fashion production manager",
            "textile technologist",
            "apparel quality control",
            "fashion pattern maker",
            "fashion production coordinator",
            "fashion sourcing",
            "fashion warehouse",
            "fashion supply chain",
            "fashion logistics",
            "fashion e-commerce",
            "fashion brand manager"
        ],

        "Construction": [
            "construction",
            "architecture",
            "civil engineering",
            "building",
            "contractor",
            "project management",
            "blueprints",
            "structural engineering",
            "construction management",
            "site supervisor",
            "construction worker",
            "construction site",
            "construction equipment",
            "construction materials",
            "construction safety",
            "excavation",
            "concrete",
            "masonry",
            "roofing",
            "carpentry",
            "electrical",
            "plumbing",
            "hvac",
            "mechanical engineering",
            "interior design",
            "landscaping",
            "surveying",
            "estimating",
            "scheduling",
            "budgeting",
            "quality control",
            "building codes",
            "permits",
            "construction technology",
            "green building",
            "sustainable construction",
            "renovation",
            "remodeling",
            "demolition",
            "foundation",
            "structural steel",
            "formwork",
            "building systems",
            "safety regulations",
            "construction inspection",
            "construction drawings",
            "site development",
            "construction planning",
            "construction contracts",
            "construction documentation"
        ],

        "Gaming and Esports": [
            "gaming", "esports", "video games", "game development", "game design",
            "game programming", "game testing", "game art", "game audio", "game marketing",
            "game publishing", "game monetization", "game community", "game streaming", "game tournaments",
            "esports events", "esports teams", "esports tournaments", "esports broadcasting", "esports sponsorship",
            "esports marketing", "esports management", "gaming industry", "gaming platforms", "gaming consoles",
            "PC gaming", "mobile gaming", "online gaming", "virtual reality gaming", "augmented reality gaming",
            "game analytics", "game user experience", "game localization", "game community management", "game economy",
            "game storytelling", "game narrative", "game graphics", "game animation", "game mechanics",
            "game balancing", "game servers", "game networking", "game security", "game testing tools",
            "gaming content creation", "gaming influencers", "gaming livestreaming", "gaming social media",
            "gaming merchandise"
        ],

        "Law Enforcement": [
            "communication",
            "critical thinking",
            "attention to detail",
            "problem solving",
            "conflict resolution",
            "legal knowledge",
            "investigation",
            "physical fitness",
            "emotional resilience",
            "analytical skills",
            "forensic knowledge",
            "photography skills",
            "detective agency",
            "organizational skills",
            "report writing",
            "patrol service",
            "law",
            "evidence collection",
            "crime scene investigation",
            "scientific knowledge",
            "laboratory skills",
            "data analysis",
            "observation skills",
            "surveillance",
            "emergency response",
            "risk assessment",
            "customer service",
        ]

    }


def categorize_job_ad(job_description):
    job_description = job_description.lower()
    count = {key: 0 for key in sectors}
    for sector, keywords in sectors.items():
        for keyword in keywords:
            if keyword in job_description:
                count[sector] = count[sector] + 1

    max_sect = max(count, key=count.get)
    print(max_sect, ":", count[max_sect])
    print("----job categorisation distribution over all the sectors-----")
    result = [cat+" : "+str(count[cat]) for cat in count if count[cat] > 0]
    print(result)
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
                result[current_key.strip()] += ' ' + line.strip()
        # job_count = job_count + 1
        job_string = ''
        for key, value in result.items():
            if key.__contains__('Job Description') or key.__contains__('requirement profile') or key.__contains__('Job requirement') or key.__contains__('Basic knowledge') or key.__contains__(
                    'What you bring') \
                    or key.__contains__('tasks include') or key.__contains__(
                'Advanced knowledge') or key.__contains__('Expert knowledge') \
                    or key.__contains__('Requirement') or key.__contains__('requirements') or key.__contains__(
                'she expects') or key.__contains__('out'):
                job_string = job_string + key.strip() + ": " + value.strip() + "\n"
        filtered_jobs.append(job_string)


all_sect = {key: 0 for key in sectors}
for job in filtered_jobs:
    category = categorize_job_ad(job)
    all_sect[category] = all_sect[category] + 1
    print(f"{job}")
    print(f"Job Category: {category}")
    print("----------------------")

print("Each sector and its number of jobs to be clustered")
print(all_sect)

sum_of_all = 0
for each_sect in all_sect:
    sum_of_all = sum_of_all + all_sect.get(each_sect)
print("Total categorized:", sum_of_all)

vsn_of_jobs = "visualisation of first "+str(sum_of_all)+" jobs"
visualization.visualize_jobs(all_sect, "Sectors", "No of jobs", vsn_of_jobs)


