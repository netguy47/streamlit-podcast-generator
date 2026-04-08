import streamlit as st
import asyncio
import edge_tts
from pathlib import Path

st.set_page_config(page_title="Podcast Generator", page_icon="🎙️", layout="centered")

st.title("🎙️ Podcast Generator")
st.markdown("### Create podcasts from text")

voice = st.selectbox("Voice", [
    "en-US-AriaNeural",
    "en-US-GuyNeural",
    "en-GB-SoniaNeural",
    "en-GB-RyanNeural"
])

text = st.text_area("Your Content", height=300)

async def generate_podcast(text, voice, output_path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(output_path))

if st.button("Generate") and text.strip():
    output = Path("output") / "web_podcast.mp3"
    output.parent.mkdir(exist_ok=True)
    
    with st.spinner("Creating podcast..."):
        asyncio.run(generate_podcast(text, voice, output))
    
    with open(output, "rb") as f:
        st.audio(f.read(), format="audio/mp3")
        st.download_button("Download", data=f.read(), file_name="web_podcast.mp3", mime="audio/mp3")