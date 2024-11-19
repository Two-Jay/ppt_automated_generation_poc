
def planning():
    pass

def generate_page():
    pass

def generate_script():
    pass

def create_ppt():
    pass

import streamlit as st

def init():
    pass

def interface():
    st.title("Auto Lecture PPT Generator")
    topic = st.text_input("강의 주제")
    audience = st.text_input("강의 대상 특성")
    if st.button("생성"):
        st.write("생성 중...")

if __name__ == "__main__":
    interface()