import streamlit as st
from langchain_engine.wiki_loader import fetch_wikipedia_summary

st.set_page_config(page_title="🕰️ TimePlay", layout="centered")

st.title("🕰️ TimePlay: Historic Roleplay Engine")
st.markdown("Choose a year and culture to spawn a legendary figure.")

year = st.text_input("Enter Year", placeholder="e.g., 500 BC, 1800, 1000 AD")
culture = st.selectbox("Select a Culture", ["Greek", "Yoruba", "Japanese", "Roman", "Egyptian"])

if st.button("Spawn Character"):
    st.success(f"🧬 Booting simulation for {culture} in the year {year}...")

    # Temporary test call
    if culture == "Greek":
        st.subheader("🧠 Character Summary")
        summary = fetch_wikipedia_summary("Socrates")
        st.write(summary)
