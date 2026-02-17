"""
AI Resume & Portfolio Builder
A Streamlit application for generating professional resumes, cover letters, and portfolios using AI
"""

import streamlit as st
import os
from dotenv import load_dotenv
from modules.ai_generator import AIGenerator
from modules.resume_builder import ResumeBuilder
from modules.coverletter_builder import CoverLetterBuilder
from modules.portfolio_builder import PortfolioBuilder
from modules.pdf_exporter import PDFExporter

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Resume & Portfolio Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
        color: #1f2937;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: #4F46E5;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        border: none;
    }
    .stButton>button:hover {
        background: #4338CA;
    }
    .success-box {
        padding: 1rem;
        background: #D1FAE5;
        border-left: 4px solid #10B981;
        border-radius: 5px;
        margin: 1rem 0;
    }
    [data-testid="stSidebar"] {
        background-color: #f9fafb;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = {}

def initialize_ai():
    """Initialize AI generator with API key"""
    # Try to get API key from multiple sources
    api_key = None
    
    # 1. Try Streamlit secrets (for deployment)
    try:
        api_key = st.secrets.get("GROQ_API_KEY")
    except:
        pass
    
    # 2. Try environment variable
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")
    
    # 3. Try session state (user input)
    if not api_key and 'api_key' in st.session_state:
        api_key = st.session_state.api_key
    
    return AIGenerator(api_key)

def render_resume_form():
    """Render the resume builder form"""
    st.header("📝 Resume Builder")
    
    with st.form("resume_form"):
        st.subheader("Personal Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name*", placeholder="John Doe")
            email = st.text_input("Email*", placeholder="john@example.com")
            phone = st.text_input("Phone", placeholder="+1 234 567 8900")
        with col2:
            linkedin = st.text_input("LinkedIn URL", placeholder="linkedin.com/in/johndoe")
            website = st.text_input("Website/Portfolio", placeholder="johndoe.com")
        
        st.subheader("Professional Summary")
        professional_summary = st.text_area(
            "Professional Summary (leave empty for AI generation)",
            placeholder="Brief overview of your professional background...",
            height=100
        )
        
        st.subheader("Skills")
        skills_input = st.text_area(
            "Skills (one per line or comma-separated)*",
            placeholder="Python\nJavaScript\nReact\nMachine Learning",
            height=100
        )
        
        st.subheader("Education")
        num_education = st.number_input("Number of Education Entries", min_value=1, max_value=5, value=1)
        education = []
        for i in range(num_education):
            st.markdown(f"**Education {i+1}**")
            col1, col2 = st.columns(2)
            with col1:
                degree = st.text_input(f"Degree", key=f"edu_degree_{i}", placeholder="B.S. Computer Science")
                institution = st.text_input(f"Institution", key=f"edu_inst_{i}", placeholder="University Name")
            with col2:
                period = st.text_input(f"Period", key=f"edu_period_{i}", placeholder="2018 - 2022")
                gpa = st.text_input(f"GPA (optional)", key=f"edu_gpa_{i}", placeholder="3.8/4.0")
            
            if degree and institution:
                education.append({
                    'degree': degree,
                    'institution': institution,
                    'period': period,
                    'gpa': gpa
                })
        
        st.subheader("Experience")
        num_experience = st.number_input("Number of Experience Entries", min_value=0, max_value=5, value=1)
        experience = []
        for i in range(num_experience):
            st.markdown(f"**Experience {i+1}**")
            col1, col2 = st.columns(2)
            with col1:
                title = st.text_input(f"Job Title", key=f"exp_title_{i}", placeholder="Software Engineer")
                company = st.text_input(f"Company", key=f"exp_company_{i}", placeholder="Company Name")
            with col2:
                period = st.text_input(f"Period", key=f"exp_period_{i}", placeholder="Jan 2022 - Present")
            
            responsibilities = st.text_area(
                f"Responsibilities (one per line)",
                key=f"exp_resp_{i}",
                placeholder="- Developed web applications\n- Collaborated with team\n- Improved performance by 50%",
                height=100
            )
            
            if title and company:
                resp_list = [r.strip().lstrip('-•').strip() for r in responsibilities.split('\n') if r.strip()]
                experience.append({
                    'title': title,
                    'company': company,
                    'period': period,
                    'responsibilities': resp_list
                })
        
        st.subheader("Projects")
        num_projects = st.number_input("Number of Projects", min_value=0, max_value=5, value=1)
        projects = []
        for i in range(num_projects):
            st.markdown(f"**Project {i+1}**")
            col1, col2 = st.columns(2)
            with col1:
                proj_name = st.text_input(f"Project Name", key=f"proj_name_{i}", placeholder="E-commerce Platform")
                technologies = st.text_input(f"Technologies", key=f"proj_tech_{i}", placeholder="React, Node.js, MongoDB")
            with col2:
                link = st.text_input(f"Link (optional)", key=f"proj_link_{i}", placeholder="github.com/...")
            
            description = st.text_area(
                f"Description",
                key=f"proj_desc_{i}",
                placeholder="Brief description of the project...",
                height=80
            )
            
            if proj_name:
                projects.append({
                    'name': proj_name,
                    'technologies': technologies,
                    'description': description,
                    'link': link
                })
        
        submitted = st.form_submit_button("🚀 Generate Resume")
        
        if submitted:
            if not name or not email:
                st.error("Please fill in required fields (Name, Email)")
                return
            
            if not skills_input:
                st.error("Please add at least one skill")
                return
            
            with st.spinner("✨ Generating your professional resume with AI..."):
                # Parse skills
                skills = [s.strip() for s in skills_input.replace(',', '\n').split('\n') if s.strip()]
                
                # Build resume data
                resume_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'linkedin': linkedin,
                    'website': website,
                    'professional_summary': professional_summary,
                    'skills': skills,
                    'education': education,
                    'experience': experience,
                    'projects': projects
                }
                
                # Generate resume
                ai = initialize_ai()
                resume_builder = ResumeBuilder(ai)
                enhanced_data = resume_builder.build_resume(resume_data)
                html_content = resume_builder.format_resume_html(enhanced_data)
                
                # Store in session state
                st.session_state.generated_content['resume'] = {
                    'html': html_content,
                    'data': enhanced_data,
                    'type': 'resume'
                }
                
                st.success("✅ Resume generated successfully!")
                st.rerun()

def render_coverletter_form():
    """Render the cover letter builder form"""
    st.header("✉️ Cover Letter Builder")
    
    with st.form("coverletter_form"):
        st.subheader("Your Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name*", placeholder="John Doe")
            email = st.text_input("Email*", placeholder="john@example.com")
        with col2:
            phone = st.text_input("Phone", placeholder="+1 234 567 8900")
            linkedin = st.text_input("LinkedIn URL", placeholder="linkedin.com/in/johndoe")
        
        st.subheader("Your Background")
        education = st.text_input("Education*", placeholder="B.S. Computer Science, University Name")
        skills = st.text_area("Key Skills*", placeholder="Python, JavaScript, Machine Learning, etc.", height=80)
        experience_summary = st.text_area(
            "Brief Experience Summary*",
            placeholder="Summarize your relevant experience in 2-3 sentences...",
            height=100
        )
        
        st.subheader("Job Information")
        company = st.text_input("Company Name*", placeholder="Tech Company Inc.")
        position = st.text_input("Position*", placeholder="Software Engineer")
        job_description = st.text_area(
            "Job Description (paste key requirements)*",
            placeholder="Paste the job description or key requirements here...",
            height=150
        )
        
        submitted = st.form_submit_button("🚀 Generate Cover Letter")
        
        if submitted:
            if not all([name, email, education, skills, experience_summary, company, position, job_description]):
                st.error("Please fill in all required fields")
                return
            
            with st.spinner("✨ Crafting your personalized cover letter with AI..."):
                profile_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'linkedin': linkedin,
                    'education': education,
                    'skills': [s.strip() for s in skills.split(',')],
                    'experience_summary': experience_summary
                }
                
                job_data = {
                    'company': company,
                    'position': position,
                    'description': job_description
                }
                
                ai = initialize_ai()
                cl_builder = CoverLetterBuilder(ai)
                letter_body = cl_builder.build_cover_letter(profile_data, job_data)
                html_content = cl_builder.format_cover_letter_html(profile_data, job_data, letter_body)
                
                st.session_state.generated_content['cover_letter'] = {
                    'html': html_content,
                    'profile': profile_data,
                    'job': job_data,
                    'type': 'cover_letter'
                }
                
                st.success("✅ Cover letter generated successfully!")
                st.rerun()

def render_portfolio_form():
    """Render the portfolio builder form"""
    st.header("🎨 Portfolio Builder")
    
    with st.form("portfolio_form"):
        st.subheader("Personal Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name*", placeholder="John Doe")
            title = st.text_input("Professional Title*", placeholder="Full Stack Developer")
            email = st.text_input("Email*", placeholder="john@example.com")
        with col2:
            phone = st.text_input("Phone", placeholder="+1 234 567 8900")
            linkedin = st.text_input("LinkedIn", placeholder="linkedin.com/in/johndoe")
            github = st.text_input("GitHub", placeholder="github.com/johndoe")
            website = st.text_input("Personal Website", placeholder="johndoe.com")
        
        st.subheader("About You")
        about = st.text_area(
            "About/Bio (leave empty for AI generation)*",
            placeholder="Tell us about yourself, your passion, and what drives you...",
            height=120
        )
        
        st.subheader("Skills")
        skills_input = st.text_area(
            "Skills (one per line or comma-separated)*",
            placeholder="Python\nJavaScript\nReact\nMachine Learning",
            height=100
        )
        
        st.subheader("Featured Projects")
        num_projects = st.number_input("Number of Projects*", min_value=1, max_value=6, value=3)
        projects = []
        for i in range(num_projects):
            st.markdown(f"**Project {i+1}**")
            col1, col2 = st.columns(2)
            with col1:
                proj_name = st.text_input(f"Project Name", key=f"port_proj_name_{i}", placeholder="AI Chatbot")
                technologies = st.text_input(f"Tech Stack", key=f"port_proj_tech_{i}", placeholder="Python, TensorFlow, Flask")
            with col2:
                link = st.text_input(f"Link", key=f"port_proj_link_{i}", placeholder="github.com/...")
            
            description = st.text_area(
                f"Description",
                key=f"port_proj_desc_{i}",
                placeholder="Describe what the project does, the problem it solves...",
                height=80
            )
            
            if proj_name:
                projects.append({
                    'name': proj_name,
                    'technologies': technologies,
                    'description': description,
                    'link': link
                })
        
        st.subheader("Achievements (Optional)")
        achievements_input = st.text_area(
            "Key Achievements (one per line)",
            placeholder="- Won hackathon XYZ\n- Published research paper\n- Contributed to open source",
            height=100
        )
        
        submitted = st.form_submit_button("🚀 Generate Portfolio")
        
        if submitted:
            if not name or not title or not email or not skills_input:
                st.error("Please fill in required fields")
                return
            
            if not projects:
                st.error("Please add at least one project")
                return
            
            with st.spinner("✨ Creating your stunning portfolio with AI..."):
                skills = [s.strip() for s in skills_input.replace(',', '\n').split('\n') if s.strip()]
                achievements = [a.strip().lstrip('-•').strip() for a in achievements_input.split('\n') if a.strip()]
                
                portfolio_data = {
                    'name': name,
                    'title': title,
                    'email': email,
                    'phone': phone,
                    'linkedin': linkedin,
                    'github': github,
                    'website': website,
                    'about': about,
                    'skills': skills,
                    'projects': projects,
                    'achievements': achievements
                }
                
                ai = initialize_ai()
                portfolio_builder = PortfolioBuilder(ai)
                enhanced_data = portfolio_builder.build_portfolio(portfolio_data)
                html_content = portfolio_builder.format_portfolio_html(enhanced_data)
                
                st.session_state.generated_content['portfolio'] = {
                    'html': html_content,
                    'data': enhanced_data,
                    'type': 'portfolio'
                }
                
                st.success("✅ Portfolio generated successfully!")
                st.rerun()

def render_preview_and_download(content_key):
    """Render preview and download options"""
    if content_key in st.session_state.generated_content:
        content = st.session_state.generated_content[content_key]
        
        st.markdown("---")
        st.subheader("📄 Preview & Download")
        
        # Preview
        with st.expander("👁️ Preview Document", expanded=True):
            st.components.v1.html(content['html'], height=600, scrolling=True)
        
        # Generate downloadable HTML file (open in browser → Ctrl+P to save as PDF)
        try:
            pdf_exporter = PDFExporter()
            html_bytes = pdf_exporter.html_to_pdf(content['html'])
            
            col1, col2 = st.columns([3, 1])
            with col2:
                st.download_button(
                    label="⬇️ Download Document",
                    data=html_bytes,
                    file_name=f"{content_key}.html",
                    mime="text/html",
                    key=f"download_btn_{content_key}"
                )
            st.caption("💡 Open the downloaded file in your browser, then press **Ctrl+P** / **Cmd+P** to save as PDF.")
        except Exception as e:
            st.error(f"Error generating download: {e}")

def main():
    """Main application"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 AI Resume & Portfolio Builder</h1>
        <p>Create professional resumes, cover letters, and portfolios powered by AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for API key
    with st.sidebar:
        st.header("⚙️ Settings")
        
        api_key = st.text_input(
            "Groq API Key",
            type="password",
            value=st.session_state.get('api_key', ''),
            help="Get your free API key from https://console.groq.com/"
        )
        if api_key:
            st.session_state.api_key = api_key
        
        if not api_key and not os.getenv("GROQ_API_KEY"):
            st.warning("⚠️ Please add your Groq API key for AI-powered features")
            st.info("👉 Without an API key, you'll get basic template content")
        else:
            st.success("✅ API key configured")
        
        st.markdown("---")
        st.markdown("### 📖 About")
        st.info("""
        This tool helps students create professional documents using AI:
        - **Resume**: ATS-friendly, AI-enhanced
        - **Cover Letter**: Personalized for jobs
        - **Portfolio**: Showcase your projects
        """)
    
    # Main content tabs
    tab1, tab2, tab3 = st.tabs(["📝 Resume", "✉️ Cover Letter", "🎨 Portfolio"])
    
    with tab1:
        render_resume_form()
        render_preview_and_download('resume')
    
    with tab2:
        render_coverletter_form()
        render_preview_and_download('cover_letter')
    
    with tab3:
        render_portfolio_form()
        render_preview_and_download('portfolio')
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6B7280; padding: 2rem 0;'>
        <p>Built with ❤️ using Streamlit and Groq AI</p>
        <p style='font-size: 0.9rem;'>Helping students succeed in their career journey</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
