import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Sara Bennani | Business Intelligence Project",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# GLOBAL STYLE
# ==================================================
st.markdown("""
<style>
body {
    background-color: #F8FAFC;
    font-family: 'Inter', sans-serif;
}
h1 { color: #0F172A; font-weight: 700; letter-spacing: -0.6px; }
h2, h3 { color: #0A2540; font-weight: 600; }
.card {
    background-color: #FFFFFF;
    padding: 34px;
    border-radius: 18px;
    margin-bottom: 30px;
    box-shadow: 0px 12px 32px rgba(15, 23, 42, 0.08);
    border-left: 6px solid #0A2540;
}
p, li { color: #334155; font-size: 16px; line-height: 1.65; }
img { border-radius: 50%; border: 3px solid #0A2540; }
[data-testid="stSidebar"] { background-color: #0F172A; }
[data-testid="stSidebar"] * { color: #E5E7EB; }
</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.image("Logo_Efrei_2022.svg.png", width=150)
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Sections",
    [
        "Project Overview",
        "Profile",
        "Education",
        "Work Experience",
        "Skills",
        "Languages",
        "Projects",
        "Extracurricular"
    ]
)

# ==================================================
# HEADER
# ==================================================
st.markdown('<div class="card">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 4])

with col1:
    st.image("profile.jpg", width=140)

with col2:
    st.title("Sara Bennani")
    st.subheader("Data • Business Intelligence • Digital Marketing")
    st.markdown("""
    📍 Paris, France  
    📧 **sbennani.sbn@gmail.com**  
    🔗 [LinkedIn](https://www.linkedin.com)
    """)

st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROJECT OVERVIEW
# ==================================================
if section == "Project Overview":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📘 Project Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Semester 4 GPA", "17.33 / 20")
    col2.metric("Professional Experiences", "4")
    col3.metric("Projects Delivered", "6+")

    st.markdown("""
    **Project:** Transformation of an academic CV into an interactive  
    **Business Intelligence dashboard** using Streamlit.

    **Academic Context:**  
    Business Intelligence module — **EFREI Paris Panthéon-Assas University**

    **Academic Supervisor:**  
    Prof. **MATHEW Mano Joseph**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROFILE
# ==================================================
elif section == "Profile":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("👩‍💻 Profile")

    st.markdown("""
    Bachelor student in **Digital Marketing Engineering** at  
    **Efrei Paris Panthéon-Assas University**.

    Strong interest in **Business Intelligence, Data Analytics,
    Artificial Intelligence and Digital Strategy**, with hands-on
    experience in predictive modeling, dashboards and data-driven decision making.
    """)

    radar_df = pd.DataFrame({
        "Dimension": ["Data Analytics", "Business Intelligence", "AI / ML", "Digital Marketing", "Strategy"],
        "Score": [85, 90, 80, 85, 80]
    })

    st.altair_chart(
        alt.Chart(radar_df).mark_line(point=True).encode(
            theta="Dimension:N",
            radius="Score:Q",
            color=alt.value("#0A2540")
        ),
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EDUCATION
# ==================================================
elif section == "Education":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎓 Education")

    st.markdown("""
    **Efrei Paris Panthéon-Assas University**  
    Bachelor in Digital Marketing Engineering (Grade License)  
    *Paris, France | Sep. 2023 – Expected Aug. 2026*

    **Semester 4 GPA: 17.33 / 20**  
    Honors: *Student Ambassador*

    Relevant courses:  
    Data Science, Data Analytics, Business Intelligence & Analytics,  
    Statistics, Python Programming, Web Development, UX/UI Ergonomics

    ---

    **Integrated Preparatory Classes – Engineering Sciences**  
    *Sep. 2022 – Sep. 2023*

    Relevant courses:  
    Mechanics and Waves, Electricity, Algorithmics, Analysis, Linear Algebra
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# WORK EXPERIENCE
# ==================================================
elif section == "Work Experience":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("💼 Work Experience")

    exp = pd.DataFrame({
        "Period": [
            "Jul 2023 – Aug 2023",
            "May 2024 – Aug 2024",
            "Jun 2025 – Aug 2025",
            "Nov 2025 – Aug 2026"
        ],
        "Experience Level": [1, 2, 3, 4]
    })

    st.altair_chart(
        alt.Chart(exp).mark_line(point=True).encode(
            x="Period:N",
            y="Experience Level:Q",
            tooltip=["Period"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Devoteam – Research & Innovation Department**  
    *Data Scientist Intern – Work-Study Program*  
    - NLP-based engagement prediction model (**+25% reach**)  
    - Led a 4-member team on structured & unstructured data  

    **Devoteam – Digital & Cloud Innovation (AWS)**  
    - Player performance prediction model (**~20% accuracy improvement**)  
    - Sports analytics platform development  

    **Devoteam – Marketing Department**  
    - Event communication (Parc des Princes)  
    - **500+ registration tracking system**  
    - LinkedIn & newsletter management  

    **Inwi – Telecom Operator**  
    - Digital marketing data framework support
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SKILLS
# ==================================================
elif section == "Skills":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🛠 Skills")

    skills = pd.DataFrame({
        "Skill": ["Python", "SQL", "Business Intelligence", "Data Analytics", "HTML/CSS", "Machine Learning"],
        "Level": [90, 85, 90, 88, 75, 80]
    })

    st.altair_chart(
        alt.Chart(skills).mark_bar(cornerRadiusEnd=10).encode(
            x=alt.X("Level:Q", scale=alt.Scale(domain=[0, 100])),
            y=alt.Y("Skill:N", sort="-x"),
            color=alt.value("#0F172A"),
            tooltip=["Skill", "Level"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Tools:** Python, SQL, Streamlit, Git, Anaconda, Visual Studio  
    **Certifications:** AXA National IT Challenge (2025), EFREI Generative AI Basics (2025)
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# LANGUAGES
# ==================================================
elif section == "Languages":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🌍 Languages")

    lang = pd.DataFrame({
        "Language": ["Arabic", "French", "English (TOEIC 920)"],
        "Level": [100, 100, 90]
    })

    st.altair_chart(
        alt.Chart(lang).mark_arc(innerRadius=70).encode(
            theta="Level:Q",
            color="Language:N",
            tooltip=["Language", "Level"]
        ),
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROJECTS
# ==================================================
elif section == "Projects":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📊 Relevant Projects")

    st.markdown("""
    **Interactive CV Dashboard – Streamlit**  
    Business Intelligence application for structured visualization of an academic CV.

    **Drawing Portfolio**  
    Personal creative project supporting idea clarity and communication.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EXTRACURRICULAR
# ==================================================
elif section == "Extracurricular":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🏅 Extracurricular Activities & Interests")

    st.markdown("""
    **Student Union (BDE) – Event Organizer**  
    - €2,500 funding negotiated  
    - Events with 200+ attendees  

    **Football Club – EFREI Paris**  
    Official university team member  

    **Volunteering – Bab Rayan Association**  
    Group leader supporting orphan children  

    **Arts & Culture:** Theater, Piano, Drawing
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================
st.success("Business Intelligence Academic Project — Streamlit Application")
