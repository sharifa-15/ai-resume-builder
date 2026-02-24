import os
import openai


# Set your OpenAI API key

openai.api_key = os.getenv("OPENAI_API_KEY")


st.title("AI Resume & Portfolio Builder")

# Collect student input
name = st.text_input("Full Name")
email = st.text_input("Email")
education = st.text_area("Education")
skills = st.text_area("Skills (comma separated)")
projects = st.text_area("Projects")
experience = st.text_area("Work/Internship Experience")
career_goal = st.selectbox("Career Goal", ["Internship", "Job", "Research"])

if st.button("Generate Resume"):
    prompt = f"""
    Create a professional resume for {name}.
    Email: {email}
    Education: {education}
    Skills: {skills}
    Projects: {projects}
    Experience: {experience}
    Career Goal: {career_goal}
    Format it cleanly with sections and bullet points.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=800
    )
    
    resume_text = response["choices"][0]["message"]["content"]
    st.subheader("Generated Resume")
    st.write(resume_text)

if st.button("Generate Cover Letter"):
    prompt = f"""
    Write a tailored cover letter for {name}.
    Career Goal: {career_goal}
    Skills: {skills}
    Projects: {projects}
    Experience: {experience}
    Make it professional but personalized.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=600
    )
    
    cover_letter = response["choices"][0]["message"]["content"]
    st.subheader("Generated Cover Letter")
    st.write(cover_letter)

if st.button("Generate Portfolio"):
    prompt = f"""
    Create a portfolio summary for {name}.
    Highlight Education, Skills, Projects, and Experience.
    Make it attractive and concise.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        max_tokens=600
    )
    
    portfolio = response["choices"][0]["message"]["content"]
    st.subheader("Generated Portfolio")
    st.write(portfolio)
