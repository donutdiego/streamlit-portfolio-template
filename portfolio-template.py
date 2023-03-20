import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="", # text that will display in browser tab 
    page_icon="", # browser tab icon or emoji 
    layout="wide", # page layout - acceptable formats are wide or centered
    initial_sidebar_state="collapsed" # defines if side bar should be expanded or collapsed when loading site
    ) 

def local_css(file_name): # function to parse local CSS
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css") # path to CSS file

def interest(sel): # function to change text values of 'interests' column depending on dropdown selection
    title = st.title(sel + " interests:")  
    if sel == 'professional': # dropdown selection option
        text = st.write(
            """
            - python
            """)
    elif sel == 'personal': # dropdown selection option
        text = st.write(
            """
            - Music
            """)
    else:                   # dropdown selection option
        text = st.write(
            """
            - Food
            """)

    return title, text

with st.sidebar: # side bar with selection dropdown
        st.write("interest selection")
                                                        # values for dropdown - MUST match values in top function
        interest_selection = st.selectbox('No Label', ('professional', 'personal', 'other'), label_visibility="collapsed")

with st.container(): # top columns that can be used to place GitHub, LinkedIn, or other redirect link - blank for preferance
    left_col, middle_col, right_col = st.columns(3)
    with left_col:
        st.empty()
    with middle_col:
        st.empty()
    with right_col:
        st.empty()

# \\\ Main Section /// #
st.subheader("hi! my name is ___ and this is my portfolio") # main header that can be used for name

with st.container():
    left_col, middle_col, right_col = st.columns(3)
    with left_col: # left column section
        st.title("left section title") 
        st.write("")
    with middle_col: # middle column section
        st.title("middle section title") 
        st.write("")
    with right_col: # right column section - value changes based on side bar dropdown selection
            # if you don't want to use dropdown selection to change values, replace with this code:
                # st.title("") 
                # st.write("")
        text = interest(interest_selection) 

st.write("---") # --- Used to space out sections

# \\\ Project Section /// #
st.title("projects:")

st.write("##")

with st.container():
    main_body, right_col = st.columns((2,1)) # section divided into two columns with left column wider than right
    with main_body: 
        st.subheader("project one title")
        st.write("project description")
        st.markdown("[![Repo](https://img.icons8.com/material-outlined/48/000000/github.png)]()") #GitHub logo to redirect if needed - else just delete
    with right_col: # right column of section that can be used to place image by using st.image()
        st.empty()

st.write("##") 

with st.container():
    main_body, right_col = st.columns((2,1)) # section divided into two columns with left column wider than right
    with main_body: 
        st.subheader("project two title")
        st.write("project description")
        st.markdown("[![Repo](https://img.icons8.com/material-outlined/48/000000/github.png)]()") #GitHub logo to redirect if needed - else just delete
    with right_col: # right column of section that can be used to place image by using st.image()
        st.empty()

st.write("##")

with st.container():
    main_body, right_col = st.columns((2,1))
    with main_body: 
        st.subheader("project three title")
        st.write("project description")
        st.markdown("[![Repo](https://img.icons8.com/material-outlined/48/000000/github.png)]()") 
    with right_col:
        st.empty()

st.write("---")

# \\\ Extra Section /// #
    # Can be deleted if not needed
st.title("extra section title") # section title
st.write("##")
with st.container():
    left_col, middle_col, right_col = st.columns(3)
    with left_col:
        st.subheader("left section")
        st.write("description")
    with middle_col:
        st.subheader("middle section")
        st.write("description")
    with right_col:
        st.subheader("right section")
        st.write("description")

st.write("---")

# \\\ Contact Form /// #

# Visit https://formsubmit.co/ to set up account #

contact_form = """
<form action="https://formsubmit.co/EMAIL-TO-RECEIVE-MESSAGES" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="name" required>
    <input type="email" name="email" placeholder="email" required>
    <textarea name="message" placeholder="type your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""

st.title("contact me: ") # contact section title

left_col, middle_col, right_col = st.columns(3)

with left_col:
    st.markdown(contact_form, unsafe_allow_html=True)
with middle_col:
    st.empty()
with right_col:
    st.empty()
