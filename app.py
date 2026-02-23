import streamlit as st
from dotenv import load_dotenv
from youtube_service import fetch_titles
from agents import run_multi_agent

load_dotenv()

st.title("🔥 Viral YouTube Title Generator")

topic = st.text_input("Enter topic:")

if st.button("Generate"):
    titles = fetch_titles(topic)
    st.subheader("Trending Titles")
    for t in titles:
        st.write("•", t)

    patterns, viral_titles = run_multi_agent(titles, topic)

    st.subheader("Patterns")
    st.write(patterns)

    st.subheader("Viral Titles")
    st.write(viral_titles)