import streamlit as st
import google.generativeai as genai

# 🔑 Configure Gemini (PASTE YOUR API KEY)
genai.configure(api_key="AIzaSyAz6j8biiSiLCYSM1xxwr5V4fkzg1EdUsc")

st.set_page_config(page_title="ConceptGap AI", layout="centered")

st.title("📘 ConceptGap AI")
st.caption("AI that finds the *real* concept gap behind wrong answers")

def build_prompt(question, student_answer):
    return f"""
You are an intelligent educational diagnostic assistant.

Question:
{question}

Student Answer:
{student_answer}

Tasks:
1. Identify the exact misconception.
2. Explain the correct concept simply.
3. Ask one follow-up question.
"""

def analyze_gap(question, answer):
    model = genai.GenerativeModel("models/gemini-flash-lite-latest")
    response = model.generate_content(build_prompt(question, answer))
    return response.text

question = st.text_input("📌 Enter the Question")
answer = st.text_input("✍️ Student's Answer")

if st.button("Analyze Concept Gap"):
    if question and answer:
        with st.spinner("Analyzing..."):
            result = analyze_gap(question, answer)
            st.success("Analysis Complete")
            st.write(result)
    else:
        st.warning("Please fill both fields.")
