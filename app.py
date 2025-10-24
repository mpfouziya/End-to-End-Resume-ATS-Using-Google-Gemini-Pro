import streamlit as st
from google.genai import Client
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

try:

    # Alternatively, you can explicitly pass the API key:
    client = Client(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Error initializing Client: {e}")
    print("Please ensure your GOOGLE_API_KEY environment variable is set.")
    client = None


def get_gemini_response(prompt: str):
    """
    Generates a text response from the Gemini 1.5 Flash model using the Client object.
    """
    if client is None:
        return "Client not initialized. Check API key setup."

    # --- 2. Content Generation (Replaces model.generate_content) ---
    try:
        # Note: The model name is passed into the generate_content method,
        # and the method is accessed via client.models
        response = client.models.generate_content(
            model='gemini-2.5-flash',  # Use the desired model
            contents=prompt
        )

        # The response object structure is slightly different from the old SDK
        return response.text

    except Exception as e:
        print(f"An error occurred during content generation: {e}")
        return None


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

#Prompt Template

input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)