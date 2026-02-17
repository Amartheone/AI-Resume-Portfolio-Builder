"""
Resume Builder Module
"""
from typing import Dict, List
from modules.ai_generator import AIGenerator


class ResumeBuilder:
    """Build professional resumes with AI enhancement"""
    
    def __init__(self, ai_generator: AIGenerator):
        self.ai = ai_generator
    
    def build_resume(self, data: Dict) -> Dict:
        """Build a complete resume from user data"""
        
        # Generate professional summary if not provided
        if not data.get('professional_summary'):
            data['professional_summary'] = self.ai.generate_professional_summary({
                'name': data.get('name', ''),
                'education': data.get('education', [{}])[0].get('degree', '') if data.get('education') else '',
                'skills': data.get('skills', []),
                'years_experience': len(data.get('experience', []))
            })
        
        # Enhance experience bullet points
        enhanced_experience = []
        for exp in data.get('experience', []):
            if exp.get('responsibilities'):
                enhanced_bullets = self.ai.enhance_bullet_points(
                    exp['responsibilities'],
                    context=f"{exp.get('title', '')} at {exp.get('company', '')}"
                )
                exp['enhanced_responsibilities'] = enhanced_bullets
            enhanced_experience.append(exp)
        
        data['experience'] = enhanced_experience
        
        # Enhance project descriptions
        enhanced_projects = []
        for project in data.get('projects', []):
            if project.get('name') and not project.get('enhanced_description'):
                enhanced_desc = self.ai.generate_project_description(
                    project.get('name', ''),
                    project.get('technologies', ''),
                    project.get('description', '')
                )
                project['enhanced_description'] = enhanced_desc
            enhanced_projects.append(project)
        
        data['projects'] = enhanced_projects
        
        return data
    
    def format_resume_html(self, data: Dict, template: str = "professional") -> str:
        """Format resume data as HTML"""
        
        # Build skills section
        skills_html = ""
        if data.get('skills'):
            skills_html = "<div class='section'><h2>Skills</h2><div class='skills'>"
            skills_html += " • ".join(data['skills'])
            skills_html += "</div></div>"
        
        # Build experience section
        experience_html = ""
        if data.get('experience'):
            experience_html = "<div class='section'><h2>Professional Experience</h2>"
            for exp in data['experience']:
                experience_html += f"""
                <div class='experience-item'>
                    <div class='item-header'>
                        <strong>{exp.get('title', '')}</strong>
                        <span class='period'>{exp.get('period', '')}</span>
                    </div>
                    <div class='company'>{exp.get('company', '')}</div>
                    <ul>
                """
                responsibilities = exp.get('enhanced_responsibilities', exp.get('responsibilities', []))
                for resp in responsibilities:
                    experience_html += f"<li>{resp}</li>"
                experience_html += "</ul></div>"
            experience_html += "</div>"
        
        # Build education section
        education_html = ""
        if data.get('education'):
            education_html = "<div class='section'><h2>Education</h2>"
            for edu in data['education']:
                education_html += f"""
                <div class='education-item'>
                    <div class='item-header'>
                        <strong>{edu.get('degree', '')}</strong>
                        <span class='period'>{edu.get('period', '')}</span>
                    </div>
                    <div>{edu.get('institution', '')}</div>
                    {f"<div class='gpa'>GPA: {edu.get('gpa', '')}</div>" if edu.get('gpa') else ''}
                </div>
                """
            education_html += "</div>"
        
        # Build projects section
        projects_html = ""
        if data.get('projects'):
            projects_html = "<div class='section'><h2>Projects</h2>"
            for proj in data['projects']:
                projects_html += f"""
                <div class='project-item'>
                    <div class='item-header'>
                        <strong>{proj.get('name', '')}</strong>
                        {f"<span class='tech'>{proj.get('technologies', '')}</span>" if proj.get('technologies') else ''}
                    </div>
                    <p>{proj.get('enhanced_description', proj.get('description', ''))}</p>
                    {f"<a href='{proj.get('link', '')}' class='project-link'>View Project →</a>" if proj.get('link') else ''}
                </div>
                """
            projects_html += "</div>"
        
        # Combine into full HTML
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="styles/document_styles.css">
        </head>
        <body class="resume {template}">
            <div class="header">
                <h1>{data.get('name', '')}</h1>
                <div class="contact">
                    {data.get('email', '')} • {data.get('phone', '')}
                    {f" • {data.get('linkedin', '')}" if data.get('linkedin') else ''}
                    {f" • {data.get('website', '')}" if data.get('website') else ''}
                </div>
            </div>
            
            {f"<div class='section'><p class='summary'>{data.get('professional_summary', '')}</p></div>" if data.get('professional_summary') else ''}
            
            {skills_html}
            {experience_html}
            {education_html}
            {projects_html}
        </body>
        </html>
        """
        
        return html
