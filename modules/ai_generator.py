"""
AI Content Generator using Groq API
"""
import os
from groq import Groq
from typing import Optional


class AIGenerator:
    """Generate AI-enhanced content using Groq API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the AI generator with API key"""
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.client = None
        
        if self.api_key and self.api_key != "your_api_key_here":
            try:
                self.client = Groq(api_key=self.api_key)
            except Exception as e:
                print(f"Error initializing Groq client: {e}")
                self.client = None
    
    def _generate_content(self, prompt: str, max_tokens: int = 1000) -> str:
        """Generate content using Groq API"""
        if not self.client:
            return self._fallback_content(prompt)
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert career counselor and professional resume writer. Generate clear, professional, and impactful content."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.1-70b-versatile",
                temperature=0.7,
                max_tokens=max_tokens,
            )
            return chat_completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating content: {e}")
            return self._fallback_content(prompt)
    
    def _fallback_content(self, prompt: str) -> str:
        """Provide fallback content when API is not available"""
        if "resume" in prompt.lower():
            return "Experienced professional with strong skills and proven track record."
        elif "cover letter" in prompt.lower():
            return "I am writing to express my interest in this position. My skills and experience make me an ideal candidate."
        elif "portfolio" in prompt.lower():
            return "Showcasing innovative projects and technical expertise."
        return "Professional content generated."
    
    def enhance_bullet_points(self, bullet_points: list, context: str = "") -> list:
        """Enhance resume bullet points"""
        if not bullet_points:
            return []
        
        prompt = f"""Enhance these professional bullet points to be more impactful and achievement-focused. 
Context: {context}

Bullet points to enhance:
{chr(10).join(['- ' + bp for bp in bullet_points])}

Return ONLY the enhanced bullet points, one per line, starting with '-'. Keep them concise and quantifiable when possible."""
        
        result = self._generate_content(prompt, max_tokens=500)
        
        # Parse the bullet points
        enhanced = [line.strip().lstrip('-').strip() for line in result.split('\n') if line.strip().startswith('-')]
        
        # Fallback to original if parsing fails
        return enhanced if enhanced else bullet_points
    
    def generate_professional_summary(self, profile_data: dict) -> str:
        """Generate a professional summary"""
        prompt = f"""Create a compelling professional summary (2-3 sentences) for a resume based on this information:

Name: {profile_data.get('name', 'Student')}
Education: {profile_data.get('education', 'Bachelor degree')}
Skills: {', '.join(profile_data.get('skills', ['various skills']))}
Experience: {profile_data.get('years_experience', '0-2')} years

Make it impactful and achievement-focused."""
        
        return self._generate_content(prompt, max_tokens=200)
    
    def generate_cover_letter(self, profile_data: dict, job_data: dict) -> str:
        """Generate a personalized cover letter"""
        prompt = f"""Write a professional cover letter for this candidate applying to this position:

CANDIDATE INFO:
Name: {profile_data.get('name', 'Candidate')}
Education: {profile_data.get('education', '')}
Skills: {', '.join(profile_data.get('skills', []))}
Experience: {profile_data.get('experience_summary', '')}

JOB INFO:
Company: {job_data.get('company', 'the company')}
Position: {job_data.get('position', 'the position')}
Job Description: {job_data.get('description', '')}

Write a compelling 3-4 paragraph cover letter that:
1. Opens with enthusiasm for the specific role
2. Highlights relevant skills and experiences
3. Shows knowledge of the company
4. Ends with a strong call to action

Return ONLY the cover letter body (without address/date header)."""
        
        return self._generate_content(prompt, max_tokens=800)
    
    def generate_project_description(self, project_name: str, tech_stack: str, brief_desc: str) -> str:
        """Generate an enhanced project description"""
        prompt = f"""Create a compelling project description for a portfolio:

Project Name: {project_name}
Technologies: {tech_stack}
Brief Description: {brief_desc}

Write 2-3 sentences that highlight the problem solved, technical approach, and impact. Make it impressive and specific."""
        
        return self._generate_content(prompt, max_tokens=300)
    
    def generate_skills_summary(self, skills: list, context: str = "") -> str:
        """Generate a skills summary paragraph"""
        prompt = f"""Create a brief paragraph (2-3 sentences) highlighting these technical skills in context:

Skills: {', '.join(skills)}
Context: {context}

Make it sound professional and impressive."""
        
        return self._generate_content(prompt, max_tokens=200)
