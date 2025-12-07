import json
from langchain_engine.wiki_loader import fetch_wikipedia_summary

with open("data/personas.json", "r") as f:
    persona_data = json.load(f)

st.title("🕰️ TimePlay: Historic Roleplay Engine")
st.markdown("Enter a time in history and become someone legendary.")

culture = st.selectbox("🌍 Select a Culture / Era", list(persona_data.keys()))
year = st.selectbox("📅 Pick a Year", list(persona_data[culture].keys()))
character = st.selectbox("🧬 Choose a Character", persona_data[culture][year])

if st.button("Spawn Character"):
    st.success(f" Generating backstory for {character}...")

    st.subheader("📜 Character Summary")
    st.write(fetch_wikipedia_summary(character))
