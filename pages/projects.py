import streamlit as st
st.set_page_config(page_title="Raman Kumar", page_icon=":computer:")
st.title("Projects built (....so far!)")
st.divider()

st.write("1. Document-based Chatbot")
st.image("resources/docbot.png", width=400)
st.code("""LLM-powered Chatbot that can answer queries about an uploaded document.
Made with the help of LangChain and Streamlit framework.""", language="None")
st.link_button(label="Try it now!", url="https://docbot1.streamlit.app/")
st.link_button(label="View on Github", url="https://github.com/ramankumar-1/docbot")

st.divider()

st.write("2. NPTEL E-Course Recommender")
st.code("""recommendation of similar NPTEL courses using content-based filtering 
and vector model searching of NPTEL courses performed on the data scraped 
from the NPTEL website using BeautifulSoup.""", language="None")
st.link_button(label="View on Github", url="https://github.com/ramankumar-1/course-recommender")

with st.sidebar:
    st.page_link(page="app.py", label=":male-technologist: About")
    st.page_link(page="pages/projects.py", label=":wrench: Projects")
    st.page_link(page="pages/education.py", label=":student: Education")
    st.page_link(page="pages/skills.py", label=":dart: Skills")
    st.page_link(page="pages/contactme.py", label=":telephone_receiver: Contact Me")