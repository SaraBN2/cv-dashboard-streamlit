import streamlit as st
import pandas as pd
import altair as alt

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Sara Bennani | Business Intelligence CV Dashboard",
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
h1 { color: #0F172A; font-weight: 700; }
h2, h3 { color: #0A2540; font-weight: 600; }
.card {
    background-color: #FFFFFF;
    padding: 34px;
    border-radius: 18px;
    margin-bottom: 30px;
    box-shadow: 0px 12px 32px rgba(15, 23, 42, 0.08);
    border-left: 6px solid #0A2540;
}
p, li {
    color: #334155;
    font-size: 16px;
    line-height: 1.65;
}
img {
    border-radius: 50%;
    border: 3px solid #0A2540;
}
[data-testid="stSidebar"] {
    background-color: #0F172A;
}
[data-testid="stSidebar"] * {
    color: #E5E7EB;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Sections",
    [
        "Executive Summary",
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
    st.subheader("Data Science • Business Intelligence • Digital Strategy")
    st.markdown("""
    📍 Paris, France  
    📧 **sbennani.sbn@gmail.com**  
    🔗 LinkedIn: Sara Bennani
    """)

st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================
if section == "Executive Summary":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📌 Executive Summary")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("GPA (Semester 4)", "17.33 / 20")
    col2.metric("TOEIC Score", "920")
    col3.metric("Professional Experiences", "4")
    col4.metric("Key Projects", "2")

    st.markdown("""
    Bachelor student in **Digital Marketing Engineering** at **Efrei Paris Panthéon-Assas Université**,  
    combining **data science, business intelligence, and digital strategy**.

    Strong experience in **predictive modeling, NLP, analytics dashboards**, and  
    **data-driven marketing**, with demonstrated leadership and measurable business impact.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROFILE
# ==================================================
elif section == "Profile":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("👩‍💻 Profile")
    st.markdown("""
    Data-oriented engineering student with a strong interest in  
    **Business Intelligence, Data Analytics, Machine Learning and Digital Strategy**.

    Experienced in transforming complex data into **actionable insights**
    to support strategic decision-making in both technical and business environments.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EDUCATION
# ==================================================
elif section == "Education":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎓 Education")

    st.markdown("""
    **Efrei Paris Panthéon-Assas Université** — Paris, France  
    Bachelor in Digital Marketing Engineering  
    *Sep. 2023 – Expected Aug. 2026*  

    **Semester 4 GPA:** **17.33 / 20**  
    **Honor:** Student Ambassador  

    **Relevant Coursework:**  
    Data Science, Data Analytics, Business Intelligence & Analytics,  
    Python Programming, Advanced Programming, Statistics, UX/UI Ergonomics

    ---

    **Integrated Preparatory Classes – Engineering Sciences**  
    *Sep. 2022 – Sep. 2023*  

    Coursework: Mechanics, Electricity, Algorithmics, Linear Algebra, Analysis
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# WORK EXPERIENCE
# ==================================================
elif section == "Work Experience":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("💼 Work Experience")

    exp = pd.DataFrame({
        "Role": [
            "Data Scientist Intern – R&I (Alternance)",
            "Digital & Cloud Innovation Intern",
            "Data Marketing Intern",
            "Digital Marketing Intern"
        ],
        "Impact Score": [90, 85, 80, 70]
    })

    st.altair_chart(
        alt.Chart(exp).mark_bar(cornerRadiusEnd=10).encode(
            x=alt.X("Impact Score:Q", scale=alt.Scale(domain=[0, 100]), title="Impact Level"),
            y=alt.Y("Role:N", sort="-x", title=None),
            color=alt.value("#0A2540"),
            tooltip=["Role", "Impact Score"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Devoteam – Research & Innovation Department** — Paris  
    *Data Scientist Intern (Alternance) | Nov. 2025 – Aug. 2026*  
    - Built an NLP-based engagement prediction model (**+25% reach**)  
    - Led a 4-member team for structured & unstructured data labeling  

    **Devoteam (AWS Partner)** — Paris  
    *Digital & Cloud Innovation Intern | Jun. – Aug. 2025*  
    - Player performance prediction model (**+20% accuracy**)  
    - Sports analytics platform development  

    **Devoteam – Marketing Department** — Paris  
    *Data Marketing Intern | May – Aug. 2024*  
    - Designed event communication materials (10+ partners)  
    - Built 500+ registration tracking & weekly reporting  

    **Inwi (Top 3 Telecom Operator)** — Casablanca  
    *Digital Marketing Intern | Jul. – Aug. 2023*  
    - Customer data integration for marketing campaign optimization
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SKILLS
# ==================================================
elif section == "Skills":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🛠 Skills")

    skills = pd.DataFrame({
        "Skill": ["Python", "SQL", "Business Intelligence", "Data Analytics", "Machine Learning", "Digital Strategy"],
        "Level": [90, 85, 90, 85, 80, 85]
    })

    st.altair_chart(
        alt.Chart(skills).mark_bar(cornerRadiusEnd=10).encode(
            x=alt.X("Level:Q", scale=alt.Scale(domain=[0, 100]), title="Proficiency (%)"),
            y=alt.Y("Skill:N", sort="-x", title=None),
            color=alt.value("#0F172A"),
            tooltip=["Skill", "Level"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Programming & Tools:** Python, SQL, HTML, CSS, Streamlit, Git, Anaconda, Visual Studio  
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
        "Language": ["Arabic", "French", "English"],
        "Level": [100, 100, 90]
    })

    st.altair_chart(
        alt.Chart(lang).mark_arc(innerRadius=80).encode(
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
    **Interactive CV Dashboard – Streamlit (BI Project)**  
    Developed an interactive Business Intelligence application to structure
    and visualize an academic CV using data storytelling principles.  

    🔗 https://cv-dashboard-app-rxyfesphor6ufjqqqni5vw.streamlit.app  

    ---

    **Drawing Portfolio**  
    Ongoing personal project enabling creative expression and visual communication.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EXTRACURRICULAR
# ==================================================
elif section == "Extracurricular":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🏅 Extracurricular Activities")

    st.markdown("""
    **Student Union (BDE) – Event Organizer**  
    - Negotiated €2500 funding  
    - Organized bi-weekly events (200+ attendees)  

    **Football Club – Efrei Paris**  
    Member of the official university team  

    **Volunteering – Bab Rayan Association**  
    Group leader supporting orphan children  

    **Hobbies:** Theater (7 years), Piano (Conservatory), Drawing
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================
st.success("Business Intelligence CV Dashboard — Academic & Professional Project")
