import streamlit as st

st.set_page_config(page_title="Raman Kumar",page_icon=":computer:")

st.title("What & Where I studied ?")
st.divider()

st.image("resources/vit.png")
st.code('''{"College": "Vellore Institute of Technology, Chennai",
 "Course" : "B.Tech in Computer Science & Engineering",
 "CGPA"   : 7.46,
 "When"   : "2020-2024"}''',language="json5")

with st.sidebar:
    st.page_link(page="app.py", label=":male-technologist: About")
    st.page_link(page="pages/projects.py", label=":wrench: Projects")
    st.page_link(page="pages/education.py", label=":student: Education")
    st.page_link(page="pages/skills.py", label=":dart: Skills")
    st.page_link(page="pages/contactme.py", label=":telephone_receiver: Contact Me")