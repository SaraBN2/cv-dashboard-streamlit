import streamlit as st
import pandas as pd
import altair as alt

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

/* HEADINGS */
h1 {
    color: #0F172A;
    font-weight: 700;
    letter-spacing: -0.6px;
}
h2, h3 {
    color: #0A2540;
    font-weight: 600;
}

/* CARDS */
.card {
    background-color: #FFFFFF;
    padding: 34px;
    border-radius: 18px;
    margin-bottom: 30px;
    box-shadow: 0px 12px 32px rgba(15, 23, 42, 0.08);
    border-left: 6px solid #0A2540;
}

/* TEXT */
p, li {
    color: #334155;
    font-size: 16px;
    line-height: 1.65;
}
.subtle {
    color: #6B7280;
    font-size: 14px;
}

/* PROFILE PHOTO */
.profile-pic {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #0A2540;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #0F172A;
}
[data-testid="stSidebar"] * {
    color: #E5E7EB;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR NAVIGATION
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
# HEADER (WITH PHOTO)
# ==================================================
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    st.markdown(
        '<img src="profile.jpg" class="profile-pic">',
        unsafe_allow_html=True
    )

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

    st.markdown("""
    **Project:** Transformation of an academic CV into an interactive
    **Business Intelligence dashboard** using Streamlit.

    **Objective:**  
    Structure, model and visualize academic and professional data
    to enhance readability, analysis and storytelling.

    **Academic Context:**  
    Developed within the **Business Intelligence** module at **EFREI Paris**.

    **Academic Supervisor:**  
    Prof. **MATHEW Mano Joseph**  
    🔗 https://www.linkedin.com/in/manomathew/
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROFILE
# ==================================================
elif section == "Profile":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("👩‍💻 Profile")

    st.markdown("""
    Engineering student at **EFREI Paris – Grande École d’Ingénieurs du Numérique**,
    pursuing a **BSc in Digital Marketing Engineering**.

    Strong interest in **Business Intelligence, Data Analysis, Data Science,
    Artificial Intelligence and Digital Strategy**, with academic and professional
    exposure to data-driven decision-making.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EDUCATION
# ==================================================
elif section == "Education":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎓 Education")

    st.markdown("""
    **EFREI Paris – Grande École d’Ingénieurs du Numérique**  
    BSc in Digital Marketing Engineering — **GPA: 3.29 / 4.0**  
    *Paris, France | 2023 – 2026*  

    Relevant courses:  
    Data Analysis, Data Science, Statistics & Sales Forecasting,
    Artificial Intelligence, Business Intelligence, Digital Strategy

    **Integrated Preparatory Program – Engineering Sciences**  
    *2022 – 2023*  

    **Groupe Scolaire Romandie – Casablanca, Morocco**  
    Scientific Baccalaureate (Mathematics & Physics), **Honors (Merit)**  
    *2022*
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
            "Nov 2025 – Aug 2026",
            "Jun – Aug 2025",
            "May – Jun 2024"
        ],
        "Role": [
            "Data Scientist Apprentice – Research & Innovation",
            "Digital & Cloud Innovation Intern (AWS Partner)",
            "Data Marketing Intern – N Platform"
        ]
    })

    st.altair_chart(
        alt.Chart(exp).mark_bar(
            size=38,
            cornerRadiusTopRight=8,
            cornerRadiusBottomRight=8
        ).encode(
            x=alt.X("Period:N", title=None),
            y=alt.Y("Role:N", sort=None, title=None),
            color=alt.value("#0A2540"),
            tooltip=["Period", "Role"]
        ).properties(height=220),
        use_container_width=True
    )

    st.markdown("""
    **Devoteam France**  
    - NLP research project with senior researchers and PhDs  
    - Machine learning on large-scale unstructured data  
    - Data-driven dashboards and marketing optimizations  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SKILLS
# ==================================================
elif section == "Skills":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🛠 Skills")

    skills = pd.DataFrame({
        "Skill": [
            "Python", "SQL", "HTML", "CSS",
            "Business Intelligence", "Data Analysis"
        ],
        "Level": [85, 80, 70, 70, 90, 85]
    })

    st.altair_chart(
        alt.Chart(skills).mark_bar(
            cornerRadiusEnd=10
        ).encode(
            x=alt.X("Level:Q", scale=alt.Scale(domain=[0, 100]), title="Proficiency (%)"),
            y=alt.Y("Skill:N", sort="-x", title=None),
            color=alt.value("#0F172A"),
            tooltip=["Skill", "Level"]
        ).properties(height=260),
        use_container_width=True
    )

    st.markdown("""
    **Tools:** Anaconda, Visual Studio, Git  
    **Certifications:**  
    - AXA National IT Challenge (2025)  
    - EFREI Generative AI Basics (2025)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# LANGUAGES
# ==================================================
elif section == "Languages":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🌍 Languages")

    lang = pd.DataFrame({
        "Language": [
            "Arabic (Native)",
            "French (Native)",
            "English (Advanced – TOEIC 920)"
        ],
        "Level": [100, 100, 90]
    })

    donut = alt.Chart(lang).mark_arc(
        innerRadius=85,
        outerRadius=130
    ).encode(
        theta="Level:Q",
        color=alt.Color(
            "Language:N",
            scale=alt.Scale(range=["#0F172A", "#475569", "#94A3B8"])
        ),
        tooltip=["Language", "Level"]
    )

    st.altair_chart(donut, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROJECTS
# ==================================================
elif section == "Projects":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📊 Relevant Project")

    st.markdown("""
    **Business Intelligence Project – Sales Analysis**  
    - Interactive **Power BI dashboard** on global BMW sales  
    - Trend analysis by region, model, pricing and fuel type  
    - Strategic insights to support business decisions  

    🔗 https://drive.google.com/file/d/1EZdoD37IQdLHSPXcpjMn6AOit0DGbI0A/view
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EXTRACURRICULAR
# ==================================================
elif section == "Extracurricular":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🏅 Extracurricular Activities & Interests")

    st.markdown("""
    **Student Union (BDE) – EFREI**  
    Events Department – Member  

    **Student Ambassador – EFREI**  

    **Bab Ryan Association – Casablanca**  
    Group Leader  

    **Interests:** Drawing, Piano, Fitness, Theater
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.success("Business Intelligence Academic Project — Streamlit Application")
