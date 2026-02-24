from openai import OpenAI
import os
import streamlit as st

# Load your API key securely
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Resume & Portfolio Builder")

# Collect student input
name = st.text_input("Full Name")
email = st.text_input("Email")
education = st.text_area("Education")
skills = st.text_area("Skills (comma separated)")

if st.button("Generate Resume"):
    try:
        # ✅ Define the prompt
        prompt = f"""
        Create a professional resume for:
        Name: {name}
        Email: {email}
        Education: {education}
        Skills: {skills}
        Format it clearly with sections.
        """

        # ✅ Call OpenAI safely
        response = client.chat.completions.create(
            model="gpt-4.1",   # or gpt-4.1-mini / gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )

        st.subheader("Generated Resume")
        st.write(response.choices[0].message.content.strip())

    except Exception as e:
        # ✅ Friendly error message
        st.error("⚠️ Sorry, something went wrong while generating your resume. Please try again later.")
        st.write(f"Error details: {str(e)}")
