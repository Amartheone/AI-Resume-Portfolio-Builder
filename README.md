# 🎓 AI Resume & Portfolio Builder

A powerful Streamlit web application that helps students create professional resumes, cover letters, and portfolios using AI-powered content generation.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31+-red.svg)

## ✨ Features

- **📝 AI-Powered Resume Builder**
  - Professional, ATS-friendly resume templates
  - AI-enhanced bullet points and descriptions
  - Multiple industry-standard layouts
  - Automatic professional summary generation

- **✉️ Personalized Cover Letter Generator**
  - Job-specific cover letters
  - AI-powered content matching job requirements
  - Professional formatting

- **🎨 Dynamic Portfolio Builder**
  - Modern, eye-catching portfolio layouts
  - Project showcase with AI-enhanced descriptions
  - Skills highlighting and achievements

- **📄 PDF Export**
  - One-click PDF download
  - Print-optimized formatting
  - Professional styling

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key (free tier available at [console.groq.com](https://console.groq.com/))

### Local Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /Users/amartheone/Developer/Edunet
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
   
   **Get your free API key:**
   - Visit [console.groq.com](https://console.groq.com/)
   - Sign up for a free account
   - Generate an API key
   - Copy and paste it into your `.env` file

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📖 How to Use

### Creating a Resume

1. Navigate to the **Resume** tab
2. Fill in your personal information, education, experience, and skills
3. Click "Generate Resume"
4. Preview your AI-enhanced resume
5. Download as PDF

### Creating a Cover Letter

1. Navigate to the **Cover Letter** tab
2. Enter your information and the job details
3. Paste the job description
4. Click "Generate Cover Letter"
5. Review and download your personalized cover letter

### Creating a Portfolio

1. Navigate to the **Portfolio** tab
2. Add your profile information and projects
3. Click "Generate Portfolio"
4. Preview your stunning portfolio
5. Download as PDF

## 🌐 Deploying to Streamlit Cloud

### Step 1: Prepare Your Repository

1. **Initialize Git (if not already done)**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: AI Resume & Portfolio Builder"
   ```

2. **Push to GitHub**
   ```bash
   # Create a new repository on GitHub, then:
   git remote add origin https://github.com/yourusername/ai-resume-builder.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. **Visit [share.streamlit.io](https://share.streamlit.io/)**

2. **Sign in with GitHub**

3. **Click "New app"**

4. **Configure your app:**
   - Repository: Select your GitHub repository
   - Branch: `main`
   - Main file path: `app.py`

5. **Add your API key as a secret:**
   - Click "Advanced settings"
   - In the "Secrets" section, add:
     ```toml
     GROQ_API_KEY = "your_actual_api_key_here"
     ```

6. **Click "Deploy!"**

Your app will be live at `https://yourusername-ai-resume-builder.streamlit.app`

## 🔧 Configuration

### API Key Configuration

The application supports multiple ways to provide your API key:

1. **Environment Variable** (for local development)
   - Add to `.env` file: `GROQ_API_KEY=your_key`

2. **Streamlit Secrets** (for deployment)
   - Add to `.streamlit/secrets.toml`:
     ```toml
     GROQ_API_KEY = "your_key"
     ```

3. **UI Input** (temporary)
   - Enter in the sidebar settings

### Using Without API Key

The app works without an API key but provides basic template content instead of AI-generated content.

## 📁 Project Structure

```
Edunet/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── .streamlit/
│   └── config.toml            # Streamlit configuration
├── modules/
│   ├── __init__.py
│   ├── ai_generator.py        # AI content generation
│   ├── resume_builder.py      # Resume generation logic
│   ├── coverletter_builder.py # Cover letter generation
│   ├── portfolio_builder.py   # Portfolio generation
│   └── pdf_exporter.py        # PDF export functionality
└── styles/
    └── document_styles.css    # Document styling
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Groq API](https://groq.com/)** - AI content generation (Llama 3.1 70B)
- **[WeasyPrint](https://weasyprint.org/)** - HTML to PDF conversion
- **Python 3.8+** - Backend logic

## 🎯 Use Cases

- **Students** creating their first professional resume
- **Job seekers** tailoring applications for specific positions
- **Freelancers** building project portfolios
- **Career changers** highlighting transferable skills
- **Recent graduates** showcasing academic projects

## 🔒 Privacy & Security

- All processing happens on your machine (local) or in your Streamlit Cloud instance
- No data is stored permanently
- API communications are encrypted
- Your documents are never saved on external servers

## 🐛 Troubleshooting

### PDF Generation Issues

If you encounter PDF generation errors:

1. **Install system dependencies** (macOS):
   ```bash
   brew install cairo pango gdk-pixbuf libffi
   ```

2. **Install system dependencies** (Linux):
   ```bash
   sudo apt-get install python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
   ```

### API Key Issues

- Ensure no extra spaces in your API key
- Verify the key is active at [console.groq.com](https://console.groq.com/)
- Check you haven't exceeded the free tier rate limits

### Import Errors

- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Use a virtual environment to avoid conflicts

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

If you encounter any issues or have questions:
- Check the troubleshooting section
- Review the [Streamlit documentation](https://docs.streamlit.io/)
- Check [Groq API documentation](https://console.groq.com/docs)

## 🌟 Acknowledgments

- Built with inspiration from modern resume builders
- Powered by Groq's lightning-fast LLM inference
- Designed for student success

---

**Made with ❤️ to help students succeed in their career journey**
