import os
import streamlit as st
import google.generativeai as genai

# Load Gemini API key from Streamlit Secrets
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# App title
st.title("AI Resume & Portfolio Builder (Gemini)")

# Collect student input
name = st.text_input("Full Name")
email = st.text_input("Email")
education = st.text_area("Education")
skills = st.text_area("Skills (comma separated)")

# Button to generate resume
if st.button("Generate Resume"):
    try:
        # Build the prompt
        prompt = f"""
        Create a professional resume for:
        Name: {name}
        Email: {email}
        Education: {education}
        Skills: {skills}
        Format it clearly with sections.
        """

        # Call Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"
        response = model.generate_content(prompt)

        # Display result
        st.subheader("Generated Resume")
        st.write(response.text)

    except Exception as e:
        # Friendly error message
        st.error("⚠️ Sorry, something went wrong while generating your resume.")
        st.write(f"Error details: {str(e)}")
