import streamlit as st
import threading
from main import speak_text

# Page configuration
st.set_page_config(
    page_title="Robo Speaker 1.1",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Dark mode styling
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0e1117;
    color: #FAFAFA;
    font-family: 'Segoe UI', sans-serif;
}
.stTextInput > div > input {
    background-color: #1c1e22;
    color: #f1f1f1;
    border-radius: 10px;
}
.stButton > button {
    background-color: #1f77b4;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h2 style='text-align:center;color:#66fcf1;'>🎙️ Robo Speaker 1.1</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Created by <b>Avni</b></p>", unsafe_allow_html=True)
st.markdown("---")

# Input
text_to_speak = st.text_input("💬 Enter the sentence you want me to speak:")

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🔊 Speak"):
        if text_to_speak.strip():
            threading.Thread(target=speak_text, args=(text_to_speak,)).start()
            st.success("Speaking...")
        else:
            st.warning("Please enter text")

with col2:
    if st.button("🚪 Exit"):
        threading.Thread(target=speak_text, args=("Bye bye friend!",)).start()
        st.stop()

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;font-size:12px;'>Powered by Python & Streamlit</p>",
    unsafe_allow_html=True
)

