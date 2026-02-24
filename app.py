from openai import OpenAI
import os
import streamlit as st

# Load your API key securely from Streamlit Secrets
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Resume & Portfolio Builder")

# Collect student input
name = st.text_input("Full Name")
email = st.text_input("Email")
education = st.text_area("Education")
skills = st.text_area("Skills (comma separated)")

if st.button("Generate Resume"):
    prompt = f"""
    Create a professional resume for:
    Name: {name}
    Email: {email}
    Education: {education}
    Skills: {skills}
    Format it clearly with sections.
    """

    # ✅ Correct call with supported model
response = client.chat.completions.create(
    model="gpt-4.1",   # ✅ newer GPT-4 model
    messages=[{"role": "user", "content": prompt}],
    max_tokens=800
)

   
    st.subheader("Generated Resume")
    st.write(response.choices[0].message.content.strip())
