import streamlit as st
import requests

st.set_page_config(page_title="🕉️ Sattva", layout="centered")

st.title("Sattva")
st.markdown("Get timeless wisdom from the Bhagavad Geeta as interpreted in *Yatharth Geeta*. Ask your question below:")

query = st.text_area("What’s on your mind?", height=150, placeholder="e.g., I feel lost. What should I do?")

if st.button("Get Wisdom"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking deeply..."):
            try:
                response = requests.post(
                    "https://db38261dee72.ngrok-free.app/ask",
                    json={"question": query},
                    timeout=20
                )
                response.raise_for_status()
                data = response.json()
                result = data.get("response", {}).get("result", "No answer found.")
                st.markdown("### Answer from Yatharth Geeta")
                st.markdown(result)
            except Exception as e:
                st.error(f"Error: {e}")