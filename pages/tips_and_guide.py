import streamlit as st

st.set_page_config(
    page_title="Tips & Guide - Smart ATS",
    page_icon="💡",
    layout="wide",
)

st.title("💡 Tips & Resume Optimization Guide")
st.markdown("Learn how to optimize your resume for ATS systems and increase your chances of landing interviews")

# Custom CSS
st.markdown("""
<style>
    .tip-box {
        background-color: #f0f9ff;
        color: black;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fef3c7;
        color: black;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #f59e0b;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d1fae5;
        color: black;
        height:300px;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #10b981;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 ATS Basics",
    "📝 Resume Format",
    "🔑 Keywords",
    "❌ Common Mistakes"
])

with tab1:
    st.header("Understanding ATS Systems")

    st.markdown("""
    ### What is an ATS?

    An Applicant Tracking System (ATS) is software used by employers to manage the recruitment process. 
    It automatically scans, parses, and ranks resumes based on job requirements.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>📊 Key Statistics</h4>
            <ul>
                <li>75%+ of large companies use ATS</li>
                <li>~70% of resumes are rejected by ATS</li>
                <li>Recruiters spend 6-7 seconds per resume</li>
                <li>80%+ match score increases interview chances</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="success-box">
            <h4>✅ How ATS Works</h4>
            <ul>
                <li>Parses resume content</li>
                <li>Extracts key information</li>
                <li>Matches keywords with job description</li>
                <li>Ranks candidates based on match score</li>
                <li>Filters out low-scoring resumes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("Resume Formatting for ATS")

    st.subheader("✅ ATS-Friendly Formats")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Recommended File Types
        - ✅ **PDF** (preferred for most ATS)
        - ✅ **DOCX** (Microsoft Word)
        - ❌ Avoid: JPG, PNG, or scanned documents

        ### Font Choices
        - ✅ Arial, Calibri, Helvetica
        - ✅ Times New Roman, Georgia
        - ✅ Font size: 10-12pt
        - ❌ Avoid: Fancy or decorative fonts
        """)

    with col2:
        st.markdown("""
        ### Layout Guidelines
        - ✅ Use standard section headings
        - ✅ Left-align text
        - ✅ Use bullet points (•, -, or numbers)
        - ✅ Keep it simple and clean
        - ❌ Avoid: Tables, columns, text boxes
        - ❌ Avoid: Headers/footers with important info
        - ❌ Avoid: Graphics, logos, or images
        """)

    st.divider()

    st.subheader("📋 Essential Resume Sections")

    st.markdown("""
    1. **Contact Information** (at the top)
       - Full name
       - Phone number
       - Email address
       - LinkedIn profile (optional)
       - Location (city, state)

    2. **Professional Summary** (2-4 sentences)
       - Highlight key qualifications
       - Include relevant keywords
       - Tailor to the specific role

    3. **Work Experience**
       - Job title
       - Company name
       - Employment dates
       - Achievements and responsibilities (bullet points)

    4. **Education**
       - Degree type
       - Major/field of study
       - Institution name
       - Graduation date

    5. **Skills**
       - Technical skills
       - Soft skills
       - Certifications
       - Languages

    6. **Optional Sections**
       - Projects
       - Publications
       - Awards
       - Volunteer work
    """)

with tab3:
    st.header("🔑 Keyword Optimization")

    st.markdown("""
    ### Why Keywords Matter

    ATS systems rank resumes based on keyword matches with the job description. 
    Including relevant keywords significantly increases your chances of passing the initial screening.
    """)

    st.markdown("""
    <div class="tip-box">
        <h4>💡 Keyword Strategy</h4>
        <ol>
            <li><strong>Analyze the Job Description</strong>
                <ul>
                    <li>Identify required skills and qualifications</li>
                    <li>Note repeated terms and phrases</li>
                    <li>Look for both hard and soft skills</li>
                </ul>
            </li>
            <li><strong>Use Exact Phrases</strong>
                <ul>
                    <li>If JD says "project management," use "project management" not "managed projects"</li>
                    <li>Include acronyms AND full terms (e.g., "SEO (Search Engine Optimization)")</li>
                </ul>
            </li>
            <li><strong>Natural Integration</strong>
                <ul>
                    <li>Don't just list keywords</li>
                    <li>Incorporate them into your experience descriptions</li>
                    <li>Use them in context to show actual experience</li>
                </ul>
            </li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Types of Keywords to Include

        **Technical Skills**
        - Programming languages (Python, Java, SQL)
        - Software/tools (Excel, Salesforce, AutoCAD)
        - Methodologies (Agile, Scrum, Lean)

        **Industry Terms**
        - Specific job titles
        - Industry jargon
        - Certifications (PMP, CPA, AWS)

        **Action Verbs**
        - Managed, developed, implemented
        - Increased, improved, optimized
        - Led, coordinated, analyzed
        """)

    with col2:
        st.markdown("""
        ### Where to Place Keywords

        1. **Professional Summary**
           - Front-load with top keywords

        2. **Skills Section**
           - List relevant technical and soft skills

        3. **Work Experience**
           - Integrate into achievement statements

        4. **Education & Certifications**
           - Include relevant coursework
           - List all relevant certifications
        """)

with tab4:
    st.header("❌ Common ATS Mistakes to Avoid")

    st.markdown("""
    <div class="warning-box">
        <h4>⚠️ Critical Mistakes That Get Resumes Rejected</h4>
    </div>
    """, unsafe_allow_html=True)

    mistakes = [
        {
            "mistake": "Using Images or Graphics",
            "why": "ATS can't read images or logos",
            "solution": "Use text only; save visual elements for portfolio"
        },
        {
            "mistake": "Complex Formatting",
            "why": "Tables, columns, and text boxes confuse ATS parsers",
            "solution": "Use simple, linear layout with clear sections"
        },
        {
            "mistake": "Headers/Footers with Key Info",
            "why": "Many ATS systems skip headers and footers",
            "solution": "Put contact info in the main body of the resume"
        },
        {
            "mistake": "Submitting as PNG/JPG",
            "why": "Image files aren't parsable by ATS",
            "solution": "Always use PDF or DOCX format"
        },
        {
            "mistake": "Keyword Stuffing",
            "why": "Looks unnatural and may trigger spam filters",
            "solution": "Integrate keywords naturally in context"
        },
        {
            "mistake": "Missing Standard Headings",
            "why": "ATS looks for specific section names",
            "solution": "Use standard headings: 'Work Experience,' 'Education,' 'Skills'"
        },
        {
            "mistake": "Inconsistent Date Formats",
            "why": "Confuses ATS parsing algorithms",
            "solution": "Use consistent format: MM/YYYY or Month YYYY"
        },
        {
            "mistake": "Special Characters in Names",
            "why": "Can cause parsing errors",
            "solution": "Avoid: @, #, &, %, etc. in section headings"
        }
    ]

    for i, item in enumerate(mistakes, 1):
        with st.expander(f"{i}. {item['mistake']}"):
            st.markdown(f"""
            **Why it's a problem:** {item['why']}

            **Solution:** {item['solution']}
            """)