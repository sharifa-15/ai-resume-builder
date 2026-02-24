# AI Resume & Portfolio Builder (Gemini)

This project helps students automatically generate tailored resumes using **Google Gemini AI**.  
It highlights individual strengths in a professional format and allows easy download as a Word document.

## 🚀 Features
- Collects student details (Name, Email, Education, Skills).
- Generates a professional resume using Gemini AI.
- Displays the resume instantly in the Streamlit app.
- Provides a **Download Resume as DOCX** button for easy saving and editing.

## 📂 Project Structure
ai-resume-builder/
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
## ⚙️ Setup Instructions
### 1. Clone the Repository
git clone https://github.com/sharifa-15/ai-resume-builder.git
cd ai-resume-builder
2. Install Dependencies
pip install- requirements.txt
3.Adding Gemini API Key
Set your API key as an environment variable:
 export GEMINI_API_KEY="your_api_key_here" Or add it in Streamlit Secrets when deploying.
4.Run the App Locally
   streamlit run app.py

🌐 Deploy on Streamlit Cloud
      Push your code to GitHub.
      Go to Streamlit Cloud.
       Connect your GitHub repo.
  Deploy — Streamlit will automatically install dependencies and run app.py.

📦 Requirements
streamlit
google-generativeai
python-docx

📝 Usage
Enter your details in the app.
Click Generate Resume.
View your resume instantly.
Download it as a Word (.docx) file.

📌 Notes
This app uses Gemini AI models. Make sure your account has access to available models.
DOCX export avoids font/Unicode issues that can occur with PDF.


