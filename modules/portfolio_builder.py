"""
Portfolio Builder Module
"""
from typing import Dict, List
from modules.ai_generator import AIGenerator


class PortfolioBuilder:
    """Build professional portfolios with AI enhancement"""
    
    def __init__(self, ai_generator: AIGenerator):
        self.ai = ai_generator
    
    def build_portfolio(self, data: Dict) -> Dict:
        """Build a complete portfolio from user data"""
        
        # Generate skills summary
        if data.get('skills') and not data.get('skills_summary'):
            data['skills_summary'] = self.ai.generate_skills_summary(
                data['skills'],
                context=f"Technical professional with expertise in various domains"
            )
        
        # Enhance project descriptions
        enhanced_projects = []
        for project in data.get('projects', []):
            if not project.get('enhanced_description'):
                enhanced_desc = self.ai.generate_project_description(
                    project.get('name', ''),
                    project.get('technologies', ''),
                    project.get('description', '')
                )
                project['enhanced_description'] = enhanced_desc
            enhanced_projects.append(project)
        
        data['projects'] = enhanced_projects
        
        return data
    
    def format_portfolio_html(self, data: Dict) -> str:
        """Format portfolio data as HTML"""
        
        # Build About section
        about_html = f"""
        <div class='section about'>
            <h2>About Me</h2>
            <p class='summary'>{data.get('about', data.get('professional_summary', 'Passionate professional dedicated to excellence.'))}</p>
            {f"<p class='skills-summary'>{data.get('skills_summary', '')}</p>" if data.get('skills_summary') else ''}
        </div>
        """
        
        # Build Skills section
        skills_html = ""
        if data.get('skills'):
            skills_html = """
            <div class='section skills-section'>
                <h2>Technical Skills</h2>
                <div class='skills-grid'>
            """
            for skill in data['skills']:
                skills_html += f"<div class='skill-tag'>{skill}</div>"
            skills_html += "</div></div>"
        
        # Build Projects showcase
        projects_html = ""
        if data.get('projects'):
            projects_html = "<div class='section projects-showcase'><h2>Featured Projects</h2>"
            for idx, proj in enumerate(data['projects']):
                projects_html += f"""
                <div class='project-card'>
                    <div class='project-number'>0{idx + 1}</div>
                    <h3>{proj.get('name', '')}</h3>
                    <div class='tech-stack'>{proj.get('technologies', '')}</div>
                    <p class='project-description'>{proj.get('enhanced_description', proj.get('description', ''))}</p>
                    {f"<a href='{proj.get('link', '')}' class='project-link' target='_blank'>View Project →</a>" if proj.get('link') else ''}
                </div>
                """
            projects_html += "</div>"
        
        # Build Achievements section
        achievements_html = ""
        if data.get('achievements'):
            achievements_html = "<div class='section'><h2>Achievements</h2><ul class='achievements'>"
            for achievement in data['achievements']:
                achievements_html += f"<li>{achievement}</li>"
            achievements_html += "</ul></div>"
        
        # Combine into full HTML
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="styles/document_styles.css">
        </head>
        <body class="portfolio">
            <div class="portfolio-header">
                <h1 class='name'>{data.get('name', '')}</h1>
                <p class='title'>{data.get('title', 'Professional Developer')}</p>
                <div class="contact">
                    {data.get('email', '')} • {data.get('phone', '')}
                    {f" • <a href='{data.get('linkedin', '')}' target='_blank'>LinkedIn</a>" if data.get('linkedin') else ''}
                    {f" • <a href='{data.get('github', '')}' target='_blank'>GitHub</a>" if data.get('github') else ''}
                    {f" • <a href='{data.get('website', '')}' target='_blank'>Website</a>" if data.get('website') else ''}
                </div>
            </div>
            
            {about_html}
            {skills_html}
            {projects_html}
            {achievements_html}
        </body>
        </html>
        """
        
        return html
