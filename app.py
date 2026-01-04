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
    📧 **Academic Supervisor:**  
[mano.mathew@efrei.fr](mailto:mano.mathew@efrei.fr)
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
    col2.metric("Experiences", "4")
    col3.metric("Projects", "6+")

    st.markdown("""
    **Project:** Transformation of an academic CV into an interactive  
    **Business Intelligence dashboard** using Streamlit.

    **Academic Context:**  
    Business Intelligence module — **EFREI Paris Panthéon-Assas University**

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
    Bachelor student in **Digital Marketing Engineering** at  
    **Efrei Paris Panthéon-Assas University**.

    Strong interest in **Business Intelligence, Data Analytics,
    Artificial Intelligence and Digital Strategy**, with hands-on
    experience in data-driven decision making.
    """)

    radar = pd.DataFrame({
        "Dimension": ["BI", "Data Analytics", "AI / ML", "Digital Marketing", "Strategy"],
        "Score": [90, 88, 80, 85, 82]
    })

    st.altair_chart(
        alt.Chart(radar).mark_line(point=True).encode(
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

    edu = pd.DataFrame({
        "Year": ["2022", "2023", "2024", "2025"],
        "Academic Level": [1, 2, 3, 4]
    })

    st.altair_chart(
        alt.Chart(edu).mark_bar().encode(
            x="Year:N",
            y="Academic Level:Q",
            color=alt.value("#0A2540")
        ),
        use_container_width=True
    )

    st.markdown("""
    **Efrei Paris Panthéon-Assas University**  
    Bachelor in Digital Marketing Engineering  
    *Sep. 2023 – Expected Aug. 2026*  

    **Semester 4 GPA: 17.33 / 20** — Honors: *Student Ambassador*
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# WORK EXPERIENCE
# ==================================================
elif section == "Work Experience":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("💼 Work Experience")

    impact = pd.DataFrame({
        "Project": ["NLP Model", "Sports Prediction", "Event Analytics"],
        "Impact (%)": [25, 20, 30]
    })

    st.altair_chart(
        alt.Chart(impact).mark_bar().encode(
            x="Impact (%):Q",
            y="Project:N",
            color=alt.value("#0F172A")
        ),
        use_container_width=True
    )

    st.markdown("""
    **Devoteam – Research & Innovation**  
    NLP-based engagement prediction model (**+25% reach**)

    **Devoteam – AWS Digital Innovation**  
    Player performance prediction (**~20% accuracy gain**)

    **Devoteam – Marketing**  
    500+ registration tracking & event analytics
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SKILLS
# ==================================================
elif section == "Skills":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🛠 Skills")

    skills = pd.DataFrame({
        "Skill": ["Python", "SQL", "BI", "Data Analytics", "HTML/CSS", "ML"],
        "Level": [90, 85, 90, 88, 75, 80]
    })

    st.altair_chart(
        alt.Chart(skills).mark_bar(cornerRadiusEnd=10).encode(
            x="Level:Q",
            y=alt.Y("Skill:N", sort="-x"),
            color=alt.value("#0A2540")
        ),
        use_container_width=True
    )

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
            color="Language:N"
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

    proj = pd.DataFrame({
        "Project": ["Power BI – BMW Sales", "Streamlit CV Dashboard"],
        "Focus Level": [90, 95]
    })

    st.altair_chart(
        alt.Chart(proj).mark_bar().encode(
            x="Focus Level:Q",
            y="Project:N",
            color=alt.value("#0F172A")
        ),
        use_container_width=True
    )

    st.markdown("""
    **Sales Analysis – Business Intelligence Project (Power BI)**  
    🔗 https://drive.google.com/file/d/1EZdoD37IQdLHSPXcpjMn6AOit0DGbI0A/view  

    **Interactive CV Dashboard – Streamlit**  
    🔗 https://cv-dashboard-app-rxyfesphor6ufjqqqni5vw.streamlit.app
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EXTRACURRICULAR
# ==================================================
elif section == "Extracurricular":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🏅 Extracurricular Activities & Interests")

    st.markdown("""
    **Student Union (BDE)** — Event Organizer  
    **Student Ambassador — EFREI**  
    **Football Club — EFREI**  
    **Bab Rayan Association** — Group Leader  

    **Interests:** Theater, Piano, Drawing, Fitness
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================
st.success("Business Intelligence Academic Project — Streamlit Application")
