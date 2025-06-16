import streamlit as st
import textwrap

# Page configuration
st.set_page_config(page_title="DocuBuddy – AI-Powered Document Helper")
st.title("📄 DocuBuddy – AI-Powered Document Helper for IT Students")

# Description
st.markdown("""
Welcome to **DocuBuddy**, your AI-inspired writing helper for IT students. This tool helps you paraphrase, simplify, summarize, and expand technical content for academic use – all without external AI APIs!
""")

# Sidebar for selecting a function
mode = st.sidebar.selectbox("Choose a Function:", [
    "Paraphrase Text",
    "Simplify Explanation",
    "Bullet Point Maker",
    "Definition Expander",
    "Academic Enhancer",
    "Jargon Replacer"
])

# Input box
user_input = st.text_area("Paste your technical content below:", height=250)

# Define logic for each feature
def process_text(text, mode):
    text = text.strip()
    if mode == "Paraphrase Text":
        return text.replace(" is ", " can be seen as ").replace(" are ", " tend to be ").replace(" provides ", " offers ")
    elif mode == "Simplify Explanation":
        return "🧠 In simpler terms: " + text.lower().capitalize()
    elif mode == "Bullet Point Maker":
        sentences = textwrap.wrap(text.replace(". ", ".\n"), 80)
        return "\n".join(f"• {line}" for line in sentences if line)
    elif mode == "Definition Expander":
        return f"📘 {text} is a commonly used concept in IT. It refers to technologies or methods that enhance system performance, reliability, or communication."
    elif mode == "Academic Enhancer":
        return text.replace(" you ", " a user ").replace(" we ", " IT professionals ").replace(" make ", " develop ").replace(" do ", " execute ")
    elif mode == "Jargon Replacer":
        return text.replace("HTTP", "Hypertext Transfer Protocol")\
                   .replace("IP", "Internet Protocol")\
                   .replace("RAM", "Random Access Memory")\
                   .replace("CPU", "Central Processing Unit")
    else:
        return text

# Output area
if st.button("Generate Result"):
    if not user_input:
        st.warning("⚠️ Please enter some text to process.")
    else:
        result = process_text(user_input, mode)
        st.success("✅ Processed Output:")
        st.text_area("Result:", value=result, height=250)

# Footer
st.markdown("---")
st.markdown("👨‍💻 Created by Parth, Ronak, Neha, and Prarthana")
