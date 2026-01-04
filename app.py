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
body {background-color: #F8FAFC; font-family: 'Inter', sans-serif;}
h1, h2, h3 {color: #0A2540;}
.card {
    background: white;
    padding: 32px;
    border-radius: 18px;
    margin-bottom: 30px;
    box-shadow: 0px 10px 28px rgba(0,0,0,0.08);
    border-left: 6px solid #0A2540;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "",
    [
        "Executive Overview",
        "Profile",
        "Education",
        "Work Experience",
        "Skills",
        "Projects",
        "Leadership & Activities"
    ]
)

# ==================================================
# HEADER
# ==================================================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("Sara Bennani")
st.subheader("Business Intelligence • Data Analytics • Digital Strategy")

st.markdown("""
📍 Paris, France  
📧 sbennani.sbn@gmail.com  
🔗 LinkedIn: Sara Bennani
""")
st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EXECUTIVE OVERVIEW
# ==================================================
if section == "Executive Overview":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("GPA (S4)", "17.33 / 20")
    col2.metric("Projects", "6+")
    col3.metric("Languages", "3")
    col4.metric("Professional Experiences", "4")

    st.markdown("""
    Business Intelligence–oriented engineering student at **Efrei Paris Panthéon-Assas University**,  
    combining **data analytics, AI modeling and digital strategy** to support decision-making.

    Strong exposure to **real-world business cases**, applied machine learning and data-driven marketing.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROFILE
# ==================================================
elif section == "Profile":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Profile")

    st.markdown("""
    Bachelor student in **Digital Marketing Engineering**, with a strong analytical mindset and
    a particular interest in **Business Intelligence, Data Analytics, AI applications and strategy**.

    Experienced in transforming **raw data into actionable insights**, communicating results to both
    technical and non-technical stakeholders.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# EDUCATION
# ==================================================
elif section == "Education":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Education")

    st.markdown("""
    **Efrei Paris Panthéon-Assas University** — Paris, France  
    Bachelor in Digital Marketing Engineering  
    *Sep. 2023 – Expected Aug. 2026*  

    **GPA (Semester 4): 17.33 / 20**  
    Honors: *Student Ambassador*

    **Key coursework:**  
    Data Science, Data Analytics, Business Intelligence & Analytics, Statistics,  
    Python Programming, Web Development, UX/UI Ergonomics
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# WORK EXPERIENCE
# ==================================================
elif section == "Work Experience":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Professional Experience")

    exp = pd.DataFrame({
        "Period": [
            "Nov 2025 – Aug 2026",
            "Jun 2025 – Aug 2025",
            "May 2024 – Aug 2024",
            "Jul 2023 – Aug 2023"
        ],
        "Role": [
            "Data Scientist Intern – Research & Innovation",
            "Digital & Cloud Innovation Intern (AWS)",
            "Data Marketing Intern",
            "Digital Marketing Intern"
        ]
    })

    st.altair_chart(
        alt.Chart(exp).mark_bar(size=35).encode(
            x="Period:N",
            y=alt.Y("Role:N", sort=None),
            color=alt.value("#0A2540"),
            tooltip=["Period", "Role"]
        ),
        use_container_width=True
    )

    st.markdown("""
    **Devoteam – Research & Innovation (Data Scientist Intern)**  
    - Built and presented an NLP-based engagement prediction model (+25% reach)  
    - Led a 4-member team on structured & unstructured data preparation  

    **Devoteam – Digital & Cloud Innovation (AWS)**  
    - Developed a player performance prediction model (~20% accuracy improvement)  
    - Contributed to a sports analytics platform (matches & player statistics)

    **Devoteam – Marketing Department**  
    - Designed official event communication (Parc des Princes)  
    - Built a 500+ registration tracking & reporting system  

    **Inwi (Telecom Operator)**  
    - Supported data-driven digital marketing campaign framework
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# SKILLS
# ==================================================
elif section == "Skills":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Skills Matrix")

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
    **Languages:** Arabic (Native), French (Native), English (Fluent – TOEIC 920)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# PROJECTS
# ==================================================
elif section == "Projects":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Selected Projects")

    st.markdown("""
    **Interactive CV Dashboard – Streamlit**  
    Designed a Business Intelligence application to structure and visualize an academic CV.

    **Drawing Portfolio**  
    Ongoing artistic practice supporting creativity, communication and idea clarification.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# LEADERSHIP
# ==================================================
elif section == "Leadership & Activities":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Leadership & Extracurricular Activities")

    st.markdown("""
    **Student Union (BDE) – Event Organizer**  
    - Negotiated €2,500 funding  
    - Managed events with 200+ attendees  

    **Football Club – Efrei Paris**  
    Member of the official university team  

    **Volunteering – Bab Rayan Association**  
    Group leader supporting orphan children  

    **Arts & Culture:** Theater, Piano (Conservatory), Drawing
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.success("Business Intelligence CV Dashboard — Academic & Professional Project")
