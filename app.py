import os
import streamlit as st
import google.generativeai as genai
from fpdf import FPDF  # lightweight PDF library

# Load Gemini API key from Streamlit Secrets
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("AI Resume & Portfolio Builder (Gemini)")

# Collect student input
name = st.text_input("Full Name")
email = st.text_input("Email")
education = st.text_area("Education")
skills = st.text_area("Skills (comma separated)")

if st.button("Generate Resume"):
    try:
        # Build the prompt
        prompt = f"""
        Create a professional resume for:
        Name: {NAME}
        Email: {EMAIL}
        Education: {EDUCATION}
        Skills: {SKILLS}
        Format it clearly with sections.
        """

        # ✅ Automatically pick the first available Gemini model
        available_models = list(genai.list_models())
        if not available_models:
            st.error("⚠️ No Gemini models available for your account.")
        else:
            model_name = available_models[0].name
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            
            resume_text = response.text

          st.subheader("Generated Resume")
         st.write(resume_text)

          # ✅ PDF Export
         pdf = FPDF()
         pdf.add_page()
        pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # load font file
       pdf.set_font("DejaVu", size=12)

       for line in resume_text.split("\n"):
            pdf.multi_cell(0, 10, line)

      pdf_output = pdf.output(dest="S").encode("utf-8")

     st.download_button(
        label="📄 Download Resume as PDF",
        data=pdf_output,
        file_name="resume.pdf",
      mime="application/pdf"
)

        except Exception as e:
        st.error("⚠️ Sorry, something went wrong while generating your resume.")
        st.write(f"Error details: {str(e)}")


