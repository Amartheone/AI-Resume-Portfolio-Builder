"""
Cover Letter Builder Module
"""
from typing import Dict
from modules.ai_generator import AIGenerator
from datetime import datetime


class CoverLetterBuilder:
    """Build personalized cover letters with AI"""
    
    def __init__(self, ai_generator: AIGenerator):
        self.ai = ai_generator
    
    def build_cover_letter(self, profile_data: Dict, job_data: Dict) -> str:
        """Generate a personalized cover letter"""
        
        # Generate the main body using AI
        letter_body = self.ai.generate_cover_letter(profile_data, job_data)
        
        return letter_body
    
    def format_cover_letter_html(self, profile_data: Dict, job_data: Dict, letter_body: str) -> str:
        """Format cover letter as HTML"""
        
        today = datetime.now().strftime("%B %d, %Y")
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="styles/document_styles.css">
        </head>
        <body class="cover-letter">
            <div class="header">
                <h1>{profile_data.get('name', '')}</h1>
                <div class="contact">
                    {profile_data.get('email', '')} • {profile_data.get('phone', '')}
                    {f" • {profile_data.get('linkedin', '')}" if profile_data.get('linkedin') else ''}
                </div>
            </div>
            
            <div class="date">{today}</div>
            
            <div class="recipient">
                <div><strong>Hiring Manager</strong></div>
                <div>{job_data.get('company', 'Company Name')}</div>
            </div>
            
            <div class="salutation">Dear Hiring Manager,</div>
            
            <div class="letter-body">
                {self._format_paragraphs(letter_body)}
            </div>
            
            <div class="closing">
                <div>Sincerely,</div>
                <div class="signature">{profile_data.get('name', '')}</div>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def _format_paragraphs(self, text: str) -> str:
        """Format text into HTML paragraphs"""
        paragraphs = text.split('\n\n')
        return ''.join([f'<p>{p.strip()}</p>' for p in paragraphs if p.strip()])
