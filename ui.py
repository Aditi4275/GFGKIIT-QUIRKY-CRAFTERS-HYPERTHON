import streamlit as st

def set_custom_ui():
    """Set custom CSS and page configuration."""
    st.set_page_config(page_title="Technical ATS Resume Expert", page_icon="📄", layout="wide")
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://www.transparenttextures.com/patterns/always-grey.png');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextArea>textarea {
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 10px;
            font-size: 16px;
        }
        .stFileUploader>div>div>div>div {
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        .stMarkdown h1 {
            text-align: center;
            color: #4CAF50;
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        .stMarkdown h2 {
            color: #333;
            font-size: 1.8em;
            margin-bottom: 15px;
        }
        .stMarkdown h3 {
            color: #4CAF50;
            font-size: 1.5em;
            margin-bottom: 10px;
        }
        .stMarkdown p {
            color: #555;
            font-size: 1.1em;
            line-height: 1.6;
        }
        .stMarkdown a {
            color: #4CAF50; /* Link color */
            text-decoration: none; /* Remove underline */
            font-weight: bold;
            transition: color 0.3s ease;
        }
        .stMarkdown a:hover {
            color: #357ABD; /* Hover color */
            text-decoration: underline; /* Add underline on hover */
        }
        .stImage img {
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stPlotlyChart {
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        /* Hide the sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        /* Highlight important text */
        .highlight {
            background-color: #FFEB3B; /* Yellow background */
            color: #000; /* Black text */
            padding: 2px 5px;
            border-radius: 3px;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True
    )
def display_header():
    """Display the header section."""
    st.markdown("<h1>📄 Technical Resume Expert</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; color: #666; font-size: 1.4em;'>
            Upload your resume and job description to get a detailed analysis and improvement suggestions.
        </p>
    """, unsafe_allow_html=True)

def display_inputs():
    """Display input fields for job description and resume upload."""
    col1, col2 = st.columns(2)
    with col1:
        input_text = st.text_area("📝 **Job Description:**", height=200, key="input", placeholder="Paste the job description here...")
    with col2:
        uploaded_file = st.file_uploader("📂 **Upload your resume (PDF):**", type=["pdf"], help="Upload your resume in PDF format.")
    return input_text, uploaded_file

def display_buttons():
    """Display action buttons."""
    col1, col2, col3 = st.columns(3)
    with col1:
        submit1 = st.button("🔍 Analyse Resume")
    with col2:
        submit2 = st.button("📈 Improve Skills")
    with col3:
        submit3 = st.button("📊 Match Resume with Job Description")
    return submit1, submit2, submit3