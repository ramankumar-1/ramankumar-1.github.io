import streamlit as st
import pandas as pd

st.set_page_config(page_title="Raman Kumar",page_icon=":computer:")
st.title("I will be glad to hear from you !")

base = r"https://raw.githubusercontent.com/ramankumar-1/ramankumar-1.github.io/main/resources/"

contact_icons=[base+"github-original.jpg",
               base+"gmail.png",
               base+"linkedin.png"]

contact_ids=[r"https://github.com/ramankumar-1", 
             r"mailto:ramankumar4141410@gmail.com",
             r"https://www.linkedin.com/in/ramankumar-1/"]

contact_df=pd.DataFrame({"medium":contact_icons,"id":contact_ids})

st.data_editor(
    contact_df,
    column_config={
        "medium": st.column_config.ImageColumn("icon"),
        "id": st.column_config.LinkColumn("url")
    },
    use_container_width=True
)

with st.sidebar:
    st.page_link(page="app.py", label=":male-technologist: About")
    st.page_link(page="pages/projects.py", label=":wrench: Projects")
    st.page_link(page="pages/education.py", label=":student: Education")
    st.page_link(page="pages/skills.py", label=":dart: Skills")
    st.page_link(page="pages/contactme.py", label=":telephone_receiver: Contact Me")