import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Smart ATS - Home",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 2rem 0;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        height:200px;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .feature-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .cta-button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🎯 Smart ATS Analyzer</p>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #666; font-size: 1.3rem; margin-bottom: 3rem;">
    Optimize your resume for success with AI-powered analysis
</div>
""", unsafe_allow_html=True)

# Welcome section
st.markdown("## Welcome! 👋")
st.markdown("""
Smart ATS Analyzer helps you optimize your resume to pass through Applicant Tracking Systems (ATS) 
and land more interviews. Our AI-powered tool analyzes your resume against job descriptions and 
provides actionable insights.
""")

st.divider()

# Features
st.markdown("## ✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📈 Match Score</div>
        <p>Get an accurate percentage match between your resume and job description</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🔍 Keyword Analysis</div>
        <p>Identify critical missing keywords that could boost your chances</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">✍️ AI Summary</div>
        <p>Generate tailored profile summaries optimized for each role</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# How it works
st.markdown("## 🚀 How It Works")

step_col1, step_col2, step_col3 = st.columns(3)

with step_col1:
    st.markdown("### 1️⃣ Upload Resume")
    st.markdown("Upload your resume in PDF format")

with step_col2:
    st.markdown("### 2️⃣ Add Job Description")
    st.markdown("Paste the job description you're targeting")

with step_col3:
    st.markdown("### 3️⃣ Get Insights")
    st.markdown("Receive detailed analysis and recommendations")

st.divider()

# CTA
st.markdown("## 🎯 Ready to Get Started?")
st.markdown("""
Navigate to the **Resume Analyzer** page from the sidebar to begin analyzing your resume!
""")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.page_link("pages/resume_analyzer.py", label="🚀 Start Analyzing Now", use_container_width=True)

st.divider()

# Statistics
st.markdown("## 📊 Why ATS Optimization Matters")

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Companies Using ATS", "75%+")

with stat_col2:
    st.metric("Resumes Rejected by ATS", "~70%")

with stat_col3:
    st.metric("Time Recruiters Spend", "6-7 sec")

with stat_col4:
    st.metric("Match Score Target", "80%+")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>🎯 Smart ATS Analyzer | Powered by Google Gemini AI</p>
    <p style="font-size: 0.9rem;">Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)