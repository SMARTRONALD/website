from flask import Flask, render_template

app = Flask(__name__)

# Reusable variable
email = "smartronald86@gmail.com"

@app.route('/')
def home():
    return render_template('index.html',
                         name="Smart Ronald",
                         location="Kampala, Uganda",
                         phone="+256787224723 / +256757516846",
                         email="smartronald86@gmail.com",
                         linkedin="https://linkedin.com/in/smart-ronald-95183b127",
                         github="https://github.com/SMARTRONALD",
                         professional_summary="Results-driven Data Scientist, Business Intelligence Analyst, and Data Analyst with expertise in machine learning, data visualization, and business intelligence solutions. Adept at transforming complex datasets into actionable insights that drive strategic business decisions. Proficient in Python, SQL, Power BI, Tableau, and statistical analysis, with a strong track record of optimizing processes, improving reporting efficiencies, and enhancing decision-making capabilities. Passionate about leveraging data-driven strategies to foster innovation and business growth.")

@app.route('/experience')
def experience():
    experiences = [
        {
            "company": "BrighterMonday Uganda",
            "position": "Business Intelligence Analyst",
            "duration": "Jan 2024 – Present",
            "responsibilities": [
                "Provide analysis and insights to business stakeholders to support data-driven decision-making.",
                "Develop, maintain, and optimize BI assets, including Git repositories, Python codebase, databases, and servers.",
                "Design and maintain Power BI dashboards and reports to ensure stakeholders have real-time access to key business metrics.",
                "Collaborate with cross-functional teams to drive data quality initiatives and enhance data governance.",
                "Own and manage CRM systems through customization, maintenance, and optimization for data gathering and reporting.",
                "Generate and present monthly, quarterly, and weekly reports on business performance, identifying key trends and opportunities."
            ]
        },
        {
            "company": "Csquared Limited",
            "position": "Network Operations Engineer",
            "duration": "Jan 2019 – Dec 2022",
            "responsibilities": [
                "Monitored optical fiber and wireless networks using tools like Nokia 5520 SAM, NFMP, and ADVA, ensuring optimal performance.",
                "Configured and managed network devices, including Alcatel Lucent SAS-Ds, SAS-DXps, ONTs, and Mikrotik switches.",
                "Provided technical support and resolved escalated network-related issues to maintain high customer satisfaction.",
                "Led data-driven initiatives by extracting and analyzing network performance data to improve operational efficiency."
            ]
        }
    ]
    return render_template('experience.html', experiences=experiences,email=email)

@app.route('/projects')
def projects():
    projects = [
        {
            "title": "GPON Network Data Pipeline",
            "description": "Developed a GPON network data extraction and transformation pipeline using Python, storing time-series data in PostgreSQL and visualizing trends with Grafana."
        },
        {
            "title": "KPMG Data Analytics Internship",
            "description": "Completed KPMG's Data Analytics Virtual Internship, showcasing expertise in data quality review, visualization (Power BI, Tableau), and stakeholder reporting."
        },
        {
            "title": "Sea Turtle Face Detection",
            "description": "Developed an AI model for individual turtle identification using deep learning techniques."
        },
        {
            "title": "Swahili News Classification",
            "description": "Built a machine learning model to classify Swahili news into various categories."
        }
    ]
    return render_template('projects.html', projects=projects,email=email)

@app.route('/skills')
def skills():
    skills = {
        "Programming": ["Python (NumPy, Pandas, scikit-learn, TensorFlow, Keras)"],
        "Database Management": ["SQL", "PostgreSQL", "MongoDB"],
        "Data Visualization": ["Power BI", "Tableau", "Matplotlib", "Seaborn", "Plotly"],
        "Machine Learning": ["Supervised & Unsupervised Learning", "Deep Learning (CNN, RNN)"],
        "Statistical Analysis": ["Hypothesis Testing", "Regression Analysis", "Time Series Analysis"],
        "Tools & Platforms": ["Jupyter Notebook", "Docker", "Git", "Linux", "Windows"]
    }
    return render_template('skills.html', skills=skills,email=email)

@app.route('/education')
def education():
    education = [
        {
            "degree": "Certificate in Artificial Intelligence and Machine Learning",
            "institution": "Refactory Academy, Clarke International University",
            "duration": "Oct 2023 – Jun 2024"
        },
        {
            "degree": "Certified Associate Data Scientist",
            "institution": "DataCamp",
            "duration": "Feb 2023 – Jul 2023"
        },
        {
            "degree": "Applied Data Science Lab",
            "institution": "WorldQuant University",
            "duration": "Aug 2022 – Jan 2023"
        },
        {
            "degree": "Bachelor of Science in Telecommunications Engineering",
            "institution": "Makerere University",
            "duration": "Aug 2014 – Jan 2019"
        }
    ]
    return render_template('education.html', education=education,email=email)

if __name__ == '__main__':
    app.run(debug=True)
