
# Resume Analyzer
The **Resume Analyzer** is a web application built using **Streamlit** and powered by **Google's Gemini AI**. It helps users analyze their resumes, compare them against job descriptions, and receive actionable feedback to improve their skills and job application success.

# Features
**Resume Analysis:** Get a detailed evaluation of your resume against a job description.

**Job Description Matching Score:** Check how well your resume matches the job requirements using an ATS (Applicant Tracking System) score.

**Improvement Suggestions:** Receive personalized recommendations to improve your skills and resume.

**Dynamic Visualizations:** View your ATS score as a pie chart.

**Resource Links:** Access direct links to courses, tutorials, and certifications to upskill.

# Technologies Used
**Streamlit:** For building the web application.

**Google Gemini AI:** For generating resume analysis and recommendations.

**PyMuPDF (fitz):** For extracting and processing PDF resumes.

**Matplotlib:** For generating visualizations (pie chart).

**Pillow (PIL):** For image processing.

**Python-dotenv:** For managing environment variables.

# Installation
**Prerequisites**
Python 3.8 or higher.
A Google API key for Gemini AI (follow Google's documentation to get your API key).

**Steps**
**Clone the Repository:**

```bash
   git clone https://github.com/Aditi4275/GFGKIIT-QUIRKY-CRAFTERS-HYPERTHON.git
   cd resume-analyzer
   ```
**Create a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
**Install Dependencies:**

```bash
pip install -r requirements.txt
```
**Set Up Environment Variables:**
Create a .env file in the root directory.

Add your Google API key:

```bash
GOOGLE_API_KEY=your_api_key_here
```
# Usage
**Upload Your Resume:** Upload your resume in PDF format.

**Enter Job Description:** Paste the job description you want to compare your resume against.

**Analyze Your Resume:** Click the Analyze Resume button to get a detailed evaluation.

**Click the Match Resume with Job Description:** Click to get an job description matching score and missing keywords.

**Improve Your Skills:** Click the Improve Skills button to get personalized recommendations and resource links.

# File Structure
```bash
resume-analyzer/
├── main.py                # Main application script
├── ui.py                  # UI-related functions
├── utils.py               # Utility functions (e.g., PDF processing, Gemini API calls)
├── charts.py              # Functions for generating charts (e.g., pie chart)
├── requirements.txt       # List of dependencies
├── .env                   # Environment variables (e.g., Google API key)
└── README.md              # Project documentation
```
Video Demostration link:https://youtu.be/1bQxHwIFVtQ
