import streamlit as st
from google.genai import Client
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import time

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Resume Analyzer - Smart ATS",
    page_icon="📊",
    layout="wide",
)

# Custom CSS
st.markdown("""
<style>
    .keyword-tag {
        background-color: #ff4b4b;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.9rem;
    }
    .summary-box {
        background-color: #f0f9ff !important;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        border: 2px solid #bfdbfe;
    }
    .summary-text {
        color: #0f172a !important;
        margin: 0;
        line-height: 1.6;
        font-size: 1rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)


# Initialize Gemini Client
@st.cache_resource
def initialize_client():
    """Initialize Gemini client with error handling"""
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("⚠️ GOOGLE_API_KEY not found in environment variables!")
            return None
        return Client(api_key=api_key)
    except Exception as e:
        st.error(f"Failed to initialize Gemini Client: {e}")
        return None


client = initialize_client()


def get_gemini_response(prompt: str, model_name: str = "gemini-2.0-flash-exp"):
    """Generate response from Gemini with error handling and retry logic"""
    if client is None:
        return None, "Client not initialized. Check API key setup."

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text, None
    except Exception as e:
        error_msg = str(e)
        # Try fallback model if the first one fails
        if "2.0" in model_name:
            try:
                st.warning("Trying fallback model...")
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=prompt
                )
                return response.text, None
            except Exception as e2:
                return None, f"Both models failed. Error: {str(e2)}"
        return None, error_msg


def input_pdf_text(uploaded_file):
    """Extract text from PDF with progress tracking"""
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        total_pages = len(reader.pages)

        progress_bar = st.progress(0)
        status_text = st.empty()

        for page_num in range(total_pages):
            page = reader.pages[page_num]
            text += str(page.extract_text()) + "\n"

            # Update progress
            progress = (page_num + 1) / total_pages
            progress_bar.progress(progress)
            status_text.text(f"Reading page {page_num + 1} of {total_pages}...")
            time.sleep(0.1)

        progress_bar.empty()
        status_text.empty()

        return text if text.strip() else None
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None


# Improved prompt template
input_prompt = """
Act as an expert ATS (Application Tracking System) with deep knowledge in software engineering, 
data science, data analytics, and big data engineering.

Analyze the resume against the job description and provide:
1. JD Match percentage (be realistic and accurate)
2. Missing keywords that are critical for the role
3. A compelling profile summary tailored to the JD

**IMPORTANT: Respond ONLY with valid JSON in this exact format:**
{{"JD Match": "XX%", "MissingKeywords": ["keyword1", "keyword2", "keyword3"], "Profile Summary": "A professional summary here"}}

Resume:
{text}

Job Description:
{jd}

Remember: Output ONLY the JSON object, no additional text.
"""

# Header
st.title("📊 Resume Analyzer")
st.markdown("Analyze your resume against job descriptions using AI")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")

    model_choice = st.selectbox(
        "Select Gemini Model",
        ["gemini-2.0-flash-exp", "gemini-1.5-flash", "gemini-1.5-pro"],
        index=0,
        help="Choose the AI model for analysis"
    )

    st.divider()

    st.header("📌 Quick Tips")
    st.markdown("""
    - Use clear, text-based PDFs
    - Include specific job descriptions
    - Keep resume under 5 pages
    - Ensure PDF is not password-protected
    """)

    if st.button("🔄 Reset Analysis", use_container_width=True):
        st.rerun()

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Job Description")
    jd = st.text_area(
        "Paste the job description here",
        height=300,
        placeholder="Enter the complete job description including required skills, qualifications, and responsibilities...",
        label_visibility="collapsed"
    )

    chars_count = len(jd)
    st.caption(f"Characters: {chars_count}/5000")

with col2:
    st.subheader("📄 Resume Upload")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF format)",
        type="pdf",
        help="Please upload a PDF file containing your resume",
        label_visibility="collapsed"
    )

    if uploaded_file:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        file_size = uploaded_file.size / 1024
        st.caption(f"File size: {file_size:.2f} KB")

st.divider()

# Analysis button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit = st.button("🚀 Analyze Resume", type="primary", use_container_width=True)

if submit:
    # Validation
    if not jd.strip():
        st.error("❌ Please paste a job description before analyzing.")
    elif uploaded_file is None:
        st.error("❌ Please upload your resume in PDF format.")
    elif len(jd) < 50:
        st.warning("⚠️ Job description seems too short. Please provide a detailed description.")
    else:
        # Create progress container
        with st.container():
            st.markdown("---")
            st.subheader("🔄 Analysis in Progress")

            main_progress = st.progress(0)
            status_container = st.empty()

            # Step 1: Extract PDF text
            status_container.info("📖 Step 1/3: Extracting text from PDF...")
            main_progress.progress(10)

            text = input_pdf_text(uploaded_file)

            if not text:
                st.error("❌ Failed to extract text from PDF. Please ensure it's a valid, text-based PDF.")
            else:
                main_progress.progress(40)

                # Step 2: Prepare data
                status_container.info("🔧 Step 2/3: Preparing data for analysis...")
                time.sleep(0.5)

                # Limit text to avoid token issues
                text = text[:8000]
                jd_text = jd[:3000]

                formatted_prompt = input_prompt.format(text=text, jd=jd_text)
                main_progress.progress(60)

                # Step 3: AI Analysis
                status_container.info("🤖 Step 3/3: Analyzing with Gemini AI...")

                response, error = get_gemini_response(formatted_prompt, model_choice)
                main_progress.progress(100)

                status_container.empty()
                main_progress.empty()

                if error:
                    st.error(f"❌ Error: {error}")

                    with st.expander("🔧 Troubleshooting"):
                        st.markdown("""
                        **Common Solutions:**
                        1. Check your GOOGLE_API_KEY in .env file
                        2. Verify API key at [Google AI Studio](https://makersuite.google.com/app/apikey)
                        3. Ensure you have API quota available
                        4. Try a different model from sidebar
                        5. Reduce resume length (under 3 pages)
                        """)
                else:
                    st.success("✅ Analysis completed successfully!")
                    st.markdown("---")

                    try:
                        # Parse JSON response
                        response_clean = response.strip()

                        # Remove markdown code blocks if present
                        if response_clean.startswith("```"):
                            lines = response_clean.split("\n")
                            response_clean = "\n".join(lines[1:-1])
                        response_clean = response_clean.replace("```json", "").replace("```", "").strip()

                        result = json.loads(response_clean)

                        # Display results with enhanced UI
                        st.header("📊 Analysis Results")

                        # Metrics in columns
                        metric_col1, metric_col2, metric_col3 = st.columns(3)

                        with metric_col1:
                            match_score = result.get("JD Match", "N/A")
                            st.metric(
                                "📈 ATS Match Score",
                                match_score,
                                help="Percentage match with job description"
                            )

                        with metric_col2:
                            missing_keywords = result.get("MissingKeywords", [])
                            st.metric(
                                "🔑 Missing Keywords",
                                len(missing_keywords),
                                help="Critical keywords not found in resume"
                            )

                        with metric_col3:
                            # Calculate match quality
                            try:
                                score_val = int(match_score.replace("%", ""))
                                if score_val >= 80:
                                    quality = "Excellent ⭐"
                                elif score_val >= 60:
                                    quality = "Good 👍"
                                elif score_val >= 40:
                                    quality = "Fair ⚠️"
                                else:
                                    quality = "Needs Work 📝"
                            except:
                                quality = "N/A"

                            st.metric(
                                "📋 Match Quality",
                                quality,
                                help="Overall resume quality assessment"
                            )

                        st.divider()

                        # Missing Keywords Section
                        st.subheader("🔍 Missing Keywords Analysis")
                        if missing_keywords:
                            st.warning(f"Found {len(missing_keywords)} critical keywords missing from your resume:")

                            # Display keywords as styled tags
                            keywords_html = ""
                            for kw in missing_keywords:
                                keywords_html += f'<span class="keyword-tag">{kw}</span> '

                            st.markdown(keywords_html, unsafe_allow_html=True)

                            st.info("💡 **Tip:** Try to naturally incorporate these keywords into your resume.")
                        else:
                            st.success("✅ Great! Your resume contains all critical keywords.")

                        st.divider()

                        # Profile Summary
                        st.subheader("✍️ AI-Generated Profile Summary")
                        summary = result.get("Profile Summary", "")

                        if summary:
                            st.markdown(f"""
                            <div class="summary-box">
                                <p class="summary-text">{summary}</p>
                            </div>
                            """, unsafe_allow_html=True)

                            st.caption("💡 You can use this summary at the top of your resume or LinkedIn profile.")
                        else:
                            st.info("No summary generated.")

                        st.divider()

                        # Download Results
                        st.subheader("💾 Export Results")

                        result_text = f"""
=================================
SMART ATS ANALYSIS RESULTS
=================================

Match Score: {match_score}
Match Quality: {quality}

Missing Keywords ({len(missing_keywords)}):
{', '.join(missing_keywords) if missing_keywords else 'None'}

Profile Summary:
{summary}

Model Used: {model_choice}
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}

=================================
Generated by Smart ATS Analyzer
=================================
"""

                        col1, col2 = st.columns(2)
                        with col1:
                            st.download_button(
                                label="📥 Download as TXT",
                                data=result_text,
                                file_name=f"ats_analysis_{time.strftime('%Y%m%d_%H%M%S')}.txt",
                                mime="text/plain",
                                use_container_width=True
                            )

                        with col2:
                            json_data = json.dumps(result, indent=2)
                            st.download_button(
                                label="📥 Download as JSON",
                                data=json_data,
                                file_name=f"ats_analysis_{time.strftime('%Y%m%d_%H%M%S')}.json",
                                mime="application/json",
                                use_container_width=True
                            )

                    except json.JSONDecodeError as e:
                        st.warning("⚠️ Could not parse AI response as JSON")
                        st.subheader("Raw Response:")
                        st.code(response, language="text")
                        st.error(f"JSON Error: {e}")
                        st.info("The AI didn't return properly formatted JSON. Try again or adjust your inputs.")