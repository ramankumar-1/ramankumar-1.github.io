import streamlit as st

st.set_page_config(page_title="Raman Kumar",page_icon=":computer:")

st.title("My Skills")
st.divider()

st.code(body="""mySkills = ["Python", "Data Science (ML + Analytics)", "Streamlit", ]
myskills.extend(["Langchain", "LLMs"])
        
# Learning new skills everyday...
""",language="python")

with st.sidebar:
    st.page_link(page="app.py", label=":male-technologist: About")
    st.page_link(page="pages/projects.py", label=":wrench: Projects")
    st.page_link(page="pages/education.py", label=":student: Education")
    st.page_link(page="pages/skills.py", label=":dart: Skills")
    st.page_link(page="pages/contactme.py", label=":telephone_receiver: Contact Me")