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
    📧 **Academic Supervisor:** [mano.mathew@efrei.fr](mailto:mano.mathew@efrei.fr)
    """)

st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROJECT OVERVIEW
# ==================================================
if section == "Project Overview":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📘 Project Overview")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("GPA (S4)", "17.33 / 20")
    col2.metric("Experiences", "4")
    col3.metric("Projects", "2")
    col4.metric("Languages", "3")

    st.markdown("""
    **Project:** Transformation of a full academic CV into an interactive **Business Intelligence dashboard** using Streamlit.  

    **Academic Context:** Business Intelligence & Analytics — **Efrei Paris Panthéon-Assas University**  

    **Academic Supervisor:** Prof. **MATHEW Mano Joseph** — mano.mathew@efrei.fr
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROFILE
# ==================================================
elif section == "Profile":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("👩‍💻 Profile")

    st.markdown("""
    Bachelor student in **Digital Marketing Engineering at Efrei Paris Panthéon-Assas University**.  

    Strong interest in **Business Intelligence, Data Analytics, Artificial Intelligence and Digital Strategy**, 
    with concrete academic and professional experience in predictive modeling, dashboarding, 
    data storytelling and decision-support systems.
    """)

    radar_df = pd.DataFrame({
        "Dimension": [
            "Business Intelligence",
            "Data Analytics",
            "Machine Learning",
            "Digital Marketing",
            "Strategy",
            "Communication"
        ],
        "Score": [90, 88, 82, 85, 83, 86]
    })

    st.altair_chart(
        alt.Chart(radar_df).mark_line(point=True).encode(
            theta=alt.Theta("Dimension:N"),
            radius=alt.Radius("Score:Q", scale=alt.Scale(domain=[0,100])),
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

    edu_df = pd.DataFrame({
        "Year": ["2022", "2023", "2024", "2025", "2026"],
        "Level": ["Prep Classes", "Bachelor", "Bachelor", "Bachelor", "Bachelor"]
    })

    st.altair_chart(
        alt.Chart(edu_df).mark_bar().encode(
            x="Year:N",
            y="Level:N",
            color=alt.value("#0A2540")
        ),
        use_container_width=True
    )

    st.markdown("""
    **Efrei Paris Panthéon-Assas University — Paris, France**  
    Bachelor in Digital Marketing Engineering (Grade License)  
    *Sep. 2023 – Expected Aug. 2026*  

    **Semester 4 GPA: 17.33 / 20** — Honors: *Student Ambassador*  

    **Relevant courses:**  
    Data Science, Data Analytics, Web Development, Business Intelligence & Analytics,  
    Calculus, Statistics, Python Programming, Advanced Programming, Neuroscience, UX/UI Ergonomics  

    **Integrated Preparatory Classes – Engineering Sciences**  
    *Sep. 2022 – Sep. 2023*  

    Mechanics and Waves, Mechanics and Electricity, Algorithmics, Analysis, Linear Algebra
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# WORK EXPERIENCE
# ==================================================
elif section == "Work Experience":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("💼 Work Experience")

    timeline_df = pd.DataFrame({
        "Period": [
            "Jul–Aug 2023",
            "May–Aug 2024",
            "Jun–Aug 2025",
            "Nov 2025–Aug 2026"
        ],
        "Company": [
            "Inwi",
            "Devoteam – Marketing",
            "Devoteam – AWS",
            "Devoteam – R&I"
        ],
        "Impact Score": [60, 75, 85, 90]
    })

    st.altair_chart(
        alt.Chart(timeline_df).mark_circle(size=200).encode(
            x="Period:N",
            y="Impact Score:Q",
            color="Company:N",
            tooltip=["Company", "Impact Score"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Devoteam – Research & Innovation Department**  
    *Data Scientist Intern – Work-Study Program*  
    - Built and presented an NLP-based engagement prediction model (**+25% reach**)  
    - Led a 4-member team on structured & unstructured data  

    **Devoteam – Digital & Cloud Innovation (AWS)**  
    - Player performance prediction model (**~20% accuracy improvement**)  
    - Sports analytics platform (matches & player statistics)  

    **Devoteam – Marketing Department**  
    - Designed official event flyer (Parc des Princes, 10+ ServiceNow partners)  
    - Built a **500+ registration tracking system**  
    - Managed LinkedIn & newsletter communications  

    **Inwi – Telecom Operator (Morocco)**  
    - Supported development of a data-driven digital marketing framework
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SKILLS
# ==================================================
elif section == "Skills":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🛠 Skills")

    skill_matrix = pd.DataFrame({
        "Skill": [
            "Python", "SQL", "Business Intelligence", "Data Analytics",
            "Machine Learning", "HTML/CSS", "Streamlit", "Git"
        ],
        "Level": [90, 85, 90, 88, 82, 75, 88, 80]
    })

    st.altair_chart(
        alt.Chart(skill_matrix).mark_bar(cornerRadiusEnd=8).encode(
            x=alt.X("Level:Q", scale=alt.Scale(domain=[0,100])),
            y=alt.Y("Skill:N", sort="-x"),
            color=alt.value("#0A2540"),
            tooltip=["Skill", "Level"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Programming & Tools:** Python, SQL, HTML, CSS, Anaconda, Visual Studio, Streamlit, Git  

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

    lang_df = pd.DataFrame({
        "Language": ["Arabic", "French", "English (TOEIC 920)"],
        "Level": [100, 100, 90]
    })

    st.altair_chart(
        alt.Chart(lang_df).mark_arc(innerRadius=80).encode(
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

    project_df = pd.DataFrame({
        "Project": [
            "Interactive CV Dashboard (Streamlit)",
            "Drawing Portfolio"
        ],
        "Analytical Focus": [95, 70]
    })

    st.altair_chart(
        alt.Chart(project_df).mark_bar().encode(
            x="Analytical Focus:Q",
            y="Project:N",
            color=alt.value("#0F172A")
        ),
        use_container_width=True
    )

    st.markdown("""
    **Interactive CV Dashboard – Streamlit**  
    🔗 https://cv-dashboard-app-rxyfesphor6ufjqqqni5vw.streamlit.app  

    Developed a complete BI application for structured visualization of an academic CV.

    **Drawing Portfolio**  
    🔗 https://drive.google.com/file/  

    Ongoing personal practice enabling creative expression and idea clarification.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EXTRACURRICULAR
# ==================================================
elif section == "Extracurricular":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🏅 Extracurricular Activities & Interests")

    st.markdown("""
    **Student Union (BDE) — Event Organizer (Mar. 2024 – Present)**  
    - Negotiated €2,500 funding  
    - Managed bi-weekly events (200+ attendees)  

    **Football Club — Efrei Paris Panthéon-Assas University**  
    Official university team member  

    **Volunteering — Bab Rayan Association**  
    Group leader supporting orphan children  

    **Arts & Culture:**  
    Theater (7 years, annual performances), Piano (Conservatory), Drawing
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================
st.success("Business Intelligence Academic Project — Streamlit Application")
