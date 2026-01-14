import streamlit as st

def get_concept_gap_response(question, student_answer):
    if "momentum" in question.lower():
        return (
            "You're close! 👀\n\n"
            "Momentum is not just mass in motion.\n"
            "Momentum = mass × velocity.\n\n"
            "Both mass and speed matter."
        )
    elif "acceleration" in question.lower():
        return (
            "Acceleration is not speed ❌\n\n"
            "Acceleration is the rate of change of velocity."
        )
    else:
        return "Nice attempt! Try being more specific."

st.set_page_config(page_title="ConceptGap AI")

st.title("📘 ConceptGap AI")
st.write("Find misconceptions in student answers")

question = st.text_input("Enter the Question")
student_answer = st.text_area("Enter the Student Answer")

if st.button("Analyze Answer"):
    if question and student_answer:
        feedback = get_concept_gap_response(question, student_answer)
        st.success("Analysis Complete ✅")
        st.write(feedback)
    else:
        st.warning("Please fill both fields")
