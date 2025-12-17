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
# GLOBAL STYLE (SOBER & ELEGANT)
# ==================================================
st.markdown("""
<style>
body { background-color: #F2F2F2; }
h1, h2, h3 { color: #111111; }
.card {
    background-color: #FFFFFF;
    padding: 28px;
    border-radius: 14px;
    margin-bottom: 24px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.06);
}
.subtle { color: #666666; }
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
# HEADER
# ==================================================
st.markdown('<div class="card">', unsafe_allow_html=True)
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
    Courses: Algorithms & Programming (Python), Linear Algebra,
    Probability, Statistics

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
        alt.Chart(exp).mark_bar(size=40).encode(
            x="Period:N",
            y=alt.Y("Role:N", sort=None),
            color=alt.value("#4A4A4A"),
            tooltip=["Period", "Role"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Devoteam France**  
    - NLP research project with senior researchers and PhDs  
    - Machine learning on large-scale unstructured data  
    - Data-driven dashboards and marketing optimizations  

    - Participation in AI-enabled digital platform testing  
    - Contribution to Devoteam × Alpine communication strategy  

    - Data-driven marketing initiatives  
    - Event coordination and WordPress content updates
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
        alt.Chart(skills).mark_bar(cornerRadiusEnd=8).encode(
            x=alt.X("Level:Q", scale=alt.Scale(domain=[0,100])),
            y=alt.Y("Skill:N", sort="-x"),
            color=alt.value("#2F2F2F"),
            tooltip=["Skill", "Level"]
        ),
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

    donut = alt.Chart(lang).mark_arc(innerRadius=70).encode(
        theta="Level:Q",
        color=alt.Color(
            "Language:N",
            scale=alt.Scale(range=["#1F1F1F", "#6B6B6B", "#B0B0B0"])
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
    Organization of student events and logistics  

    **Student Ambassador – EFREI**  
    Representation during Open Days  

    **Football & Basketball Club – EFREI**  
    Active member – teamwork and discipline  

    **Bab Ryan Association – Casablanca**  
    Group Leader – community initiatives  

    **Interests:** Drawing, Piano, Fitness, Theater
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.success("Business Intelligence Academic Project — Streamlit Application")
