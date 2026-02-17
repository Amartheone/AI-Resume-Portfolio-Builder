# 🎓 AI Resume & Portfolio Builder

An AI-powered web application that helps students and professionals create **polished resumes**, **personalized cover letters**, and **stunning portfolios** — all enhanced by the Groq AI engine.

Built with **Streamlit** and powered by **Groq's Llama 3.1 70B** model, this tool transforms basic career information into professional, ATS-friendly documents ready for download.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 **Resume Builder** | Generate ATS-friendly resumes with AI-enhanced bullet points, professional summaries, and project descriptions |
| ✉️ **Cover Letter Builder** | Create personalized, job-specific cover letters tailored to any position and company |
| 🎨 **Portfolio Builder** | Build a professional portfolio showcasing your projects, skills, and achievements |
| 🤖 **AI Enhancement** | Automatically improve bullet points, generate summaries, and enhance project descriptions using Groq AI |
| 📄 **Document Export** | Download all generated documents as self-contained HTML files — open in any browser and print to PDF |
| 🔑 **Flexible API Setup** | Provide your Groq API key via environment variable, Streamlit secrets, or the in-app sidebar |
| 🛡️ **Fallback Mode** | Works even without an API key — generates basic template content so you can still use the tool |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- A free [Groq API key](https://console.groq.com/) (optional but recommended for AI features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Resume-Portfolio-Builder.git
   cd AI-Resume-Portfolio-Builder
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS / Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and replace `your_api_key_here` with your Groq API key:
   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```
   The app will open in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
AI-Resume-Portfolio-Builder/
├── app.py                          # Main Streamlit application
├── modules/
│   ├── __init__.py
│   ├── ai_generator.py            # Groq AI content generation engine
│   ├── resume_builder.py          # Resume data processing & HTML formatting
│   ├── coverletter_builder.py     # Cover letter generation & formatting
│   ├── portfolio_builder.py       # Portfolio creation & formatting
│   └── pdf_exporter.py            # Document export (print-ready HTML)
├── styles/
│   └── document_styles.css        # Shared CSS for all generated documents
├── .streamlit/
│   └── config.toml                # Streamlit theme configuration
├── requirements.txt               # Python dependencies
├── run.sh                         # Quick-start shell script
├── .env.example                   # Environment variable template
└── .gitignore
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web application framework & UI |
| [Groq API](https://groq.com/) | AI content generation (Llama 3.1 70B) |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📖 How to Use

### 📝 Resume Builder
1. Navigate to the **Resume** tab
2. Fill in your personal information, skills, education, experience, and projects
3. Click **🚀 Generate Resume** — AI will enhance your bullet points and generate a professional summary
4. Preview the result and download it (open the file in your browser → **Ctrl+P** / **Cmd+P** to save as PDF)

### ✉️ Cover Letter Builder
1. Navigate to the **Cover Letter** tab
2. Enter your background information and the target job details
3. Paste the job description for best results
4. Click **🚀 Generate Cover Letter** — AI will craft a personalized letter
5. Preview and download (print to PDF from your browser)

### 🎨 Portfolio Builder
1. Navigate to the **Portfolio** tab
2. Add your personal details, skills, projects, and achievements
3. Click **🚀 Generate Portfolio** — AI will enhance your project descriptions and create a skills summary
4. Preview your portfolio and download (print to PDF from your browser)

---

## ⚙️ Configuration

### API Key Options

You can provide your Groq API key in three ways (in order of priority):

1. **Streamlit Secrets** (for deployment) — add to `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxxx"
   ```
2. **Environment Variable** — set in your `.env` file or shell
3. **In-App Sidebar** — paste your key directly in the app's settings panel

### Streamlit Deployment

To deploy on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code to GitHub
2. Connect your repository on Streamlit Cloud
3. Add `GROQ_API_KEY` in the app's **Secrets** section
4. Deploy!

---

## 📦 Dependencies

```
streamlit>=1.31.0
groq>=0.4.2
python-dotenv>=1.0.0
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with ❤️ using Streamlit and Groq AI<br>
  <em>Helping students succeed in their career journey</em>
</p>
