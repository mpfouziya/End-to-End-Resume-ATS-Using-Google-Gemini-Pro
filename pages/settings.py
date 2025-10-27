import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Settings - Smart ATS",
    page_icon="⚙️",
    layout="wide",
)

st.title("⚙️ Settings & Configuration")
st.markdown("Manage your application settings and API configuration")

# Custom CSS
st.markdown("""
<style>
    .info-box {
        background-color: #e0f2fe;
        color:black;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0284c7;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fef3c7;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #f59e0b;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d1fae5;
        color:black;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #10b981;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🔑 API Configuration", "🎨 Preferences", "ℹ️ About"])

with tab1:
    st.header("Google Gemini API Configuration")

    # Check current API key status
    current_key = os.getenv("GOOGLE_API_KEY")

    if current_key:
        st.markdown("""
        <div class="success-box">
            <h4>✅ API Key Configured</h4>
            <p>Your Google Gemini API key is currently configured and ready to use.</p>
        </div>
        """, unsafe_allow_html=True)

        # Masked key display
        masked_key = current_key[:8] + "*" * (len(current_key) - 12) + current_key[-4:] if len(
            current_key) > 12 else "*" * len(current_key)
        st.code(f"API Key: {masked_key}", language="text")
    else:
        st.markdown("""
        <div class="warning-box">
            <h4>⚠️ No API Key Found</h4>
            <p>You need to configure your Google Gemini API key to use this application.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("📝 How to Set Up Your API Key")

    with st.expander("Step-by-Step Setup Guide", expanded=not bool(current_key)):
        st.markdown("""
        ### 1. Get Your API Key

        1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Sign in with your Google account
        3. Click **"Create API Key"** or **"Get API Key"**
        4. Copy the generated API key

        ### 2. Configure the API Key

        **Method 1: Using .env file (Recommended)**

        1. Create a file named `.env` in your project root directory
        2. Add the following line:
        ```
        GOOGLE_API_KEY=your_api_key_here
        ```
        3. Replace `your_api_key_here` with your actual API key
        4. Save the file
        5. Restart the Streamlit application

        **Method 2: Using Environment Variables**

        **Windows:**
        ```bash
        set GOOGLE_API_KEY=your_api_key_here
        ```

        **Mac/Linux:**
        ```bash
        export GOOGLE_API_KEY=your_api_key_here
        ```

        ### 3. Verify Configuration

        After setting up, restart the app and check this page to confirm the API key is detected.
        """)

    st.divider()

    st.subheader("🔒 API Key Security")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### ✅ Do's
        - Store API keys in `.env` file
        - Add `.env` to `.gitignore`
        - Use environment variables
        - Keep keys confidential
        - Rotate keys regularly
        """)

    with col2:
        st.markdown("""
        ### ❌ Don'ts
        - Hard-code keys in source code
        - Share keys publicly
        - Commit keys to version control
        - Use keys in client-side code
        - Expose keys in logs
        """)

    st.divider()

    st.subheader("📊 API Usage & Limits")

    st.markdown("""
    <div class="info-box">
        <h4>ℹ️ Google Gemini API Limits</h4>
        <p>Free tier includes generous quotas for testing and development.</p>
        <ul>
            <li><strong>Free Tier:</strong> 15 requests per minute</li>
            <li><strong>Rate Limits:</strong> Varies by model</li>
            <li><strong>Token Limits:</strong> Depends on model chosen</li>
        </ul>
        <p>For production use, consider upgrading to a paid plan for higher limits.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Refresh API Status", type="secondary"):
        st.rerun()

with tab2:
    st.header("Application Preferences")

    st.subheader("🎨 Display Settings")

    # Theme preference (note: actual theme control is limited in Streamlit)
    st.markdown("""
    <div class="info-box">
        <h4>💡 Tip: Changing Theme</h4>
        <p>To change the app theme, click the menu (⋮) in the top right → Settings → Theme</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.subheader("🤖 Model Preferences")

    default_model = st.selectbox(
        "Default Gemini Model",
        ["gemini-2.0-flash-exp", "gemini-1.5-flash", "gemini-1.5-pro"],
        index=0,
        help="This will be your default model selection"
    )

    st.info(
        "💡 This preference will be saved for your current session. To make it permanent, modify the default in the code.")

    st.divider()

    st.subheader("📄 Resume Processing")

    max_pages = st.slider(
        "Maximum Resume Pages to Process",
        min_value=1,
        max_value=10,
        value=5,
        help="Limit the number of pages extracted from PDF resumes"
    )

    show_progress = st.checkbox(
        "Show detailed progress during analysis",
        value=True,
        help="Display step-by-step progress bars and status messages"
    )

    st.divider()

    st.subheader("💾 Export Settings")

    default_format = st.radio(
        "Default Export Format",
        ["TXT", "JSON", "Both"],
        help="Choose default format for downloading analysis results"
    )

    include_timestamp = st.checkbox(
        "Include timestamp in exported filenames",
        value=True,
        help="Add date and time to downloaded file names"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Save Preferences", type="primary", use_container_width=True):
            st.success("✅ Preferences saved for current session!")
            st.info("Note: Preferences are session-based and will reset when you refresh the app.")

    with col2:
        if st.button("🔄 Reset to Defaults", use_container_width=True):
            st.rerun()

with tab3:
    st.header("About Smart ATS Analyzer")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
        ### 🎯 Version
        **v1.0.0**

        ### 🏗️ Built With
        - Streamlit
        - Google Gemini AI
        - Python
        - PyPDF2
        """)

    with col2:
        st.markdown("""
        ### 📋 About This Application

        Smart ATS Analyzer is an AI-powered tool designed to help job seekers optimize their resumes 
        for Applicant Tracking Systems (ATS). Using Google's Gemini AI, it analyzes resumes against 
        job descriptions and provides actionable insights to improve your chances of landing interviews.

        ### ✨ Key Features

        - 📈 **Match Score Analysis**: Get accurate ATS compatibility scores
        - 🔍 **Keyword Detection**: Identify missing critical keywords
        - ✍️ **AI-Generated Summaries**: Create tailored profile summaries
        - 💾 **Export Results**: Download analysis in multiple formats
        - 🎨 **User-Friendly Interface**: Clean, intuitive design
        """)

    st.divider()

    st.subheader("🛠️ Technical Details")

    tech_col1, tech_col2 = st.columns(2)

    with tech_col1:
        st.markdown("""
        ### Supported Models
        - **gemini-2.0-flash-exp** (Latest, Recommended)
        - **gemini-1.5-flash** (Fast, Efficient)
        - **gemini-1.5-pro** (Most Capable)

        ### Supported File Types
        - PDF (Text-based only)
        - Maximum 5 pages recommended
        - File size limit: 10MB
        """)

    with tech_col2:
        st.markdown("""
        ### System Requirements
        - Python 3.8+
        - Internet connection
        - Google Gemini API key
        - Modern web browser

        ### Privacy & Security
        - No data stored permanently
        - Session-based processing
        - Secure API communication
        """)

    st.divider()

    st.subheader("📚 Resources")

    resource_col1, resource_col2, resource_col3 = st.columns(3)

    with resource_col1:
        st.markdown("""
        ### 📖 Documentation
        - User guide
        - API reference
        - Troubleshooting
        """)

    with resource_col2:
        st.markdown("""
        ### 🔗 Links
        - [Google AI Studio](https://makersuite.google.com)
        - [Streamlit Docs](https://docs.streamlit.io)
        - GitHub Repository
        """)

    with resource_col3:
        st.markdown("""
        ### 💬 Support
        - Report issues
        - Feature requests
        - Community forum
        """)

    st.divider()

    st.subheader("📝 Changelog")

    with st.expander("Version 1.0.0 - Initial Release"):
        st.markdown("""
        **Features:**
        - Resume analysis with Google Gemini AI
        - ATS match score calculation
        - Missing keyword detection
        - AI-generated profile summaries
        - Multi-model support
        - Export functionality (TXT, JSON)
        - Comprehensive tips and guides
        - Settings and configuration page

        **Release Date:** 2024
        """)

    st.divider()

    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem 0;">
        <p style="font-size: 1.2rem;">🎯 Smart ATS Analyzer</p>
        <p>Powered by Google Gemini AI | Made with ❤️ using Streamlit</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">© 2024 All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)

# Quick Actions Section
st.markdown("---")
st.header("⚡ Quick Actions")

action_col1, action_col2, action_col3 = st.columns(3)

with action_col1:
    st.page_link("app.py", label="🏠 Back to Home", use_container_width=True)

with action_col2:
    st.page_link("pages/resume_analyzer.py", label="📊 Analyze Resume", use_container_width=True)

with action_col3:
    st.page_link("pages/tips_and_guide.py", label="💡 View Tips", use_container_width=True)