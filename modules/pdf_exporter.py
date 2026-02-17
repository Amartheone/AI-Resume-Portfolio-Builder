"""
PDF Exporter Module
Uses xhtml2pdf (pure Python) - no native system libraries required.
"""
from io import BytesIO
import os
import re

import sys
print(f"[PDF DEBUG] Python executable: {sys.executable}")
print(f"[PDF DEBUG] Python path: {sys.path}")
try:
    from xhtml2pdf import pisa  # type: ignore[import-unresolved]
    HAS_XHTML2PDF = True
    print("[PDF DEBUG] xhtml2pdf imported successfully")
except ImportError as e:
    HAS_XHTML2PDF = False
    pisa = None
    print(f"[PDF DEBUG] xhtml2pdf import FAILED: {e}")
except Exception as e:
    HAS_XHTML2PDF = False
    pisa = None
    print(f"[PDF DEBUG] xhtml2pdf unexpected error: {type(e).__name__}: {e}")


class PDFExporter:
    """Export HTML documents to PDF"""
    
    def __init__(self):
        # Resolve the project root (one level up from modules/)
        self.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    def _inline_css(self, html_content: str) -> str:
        """Replace <link rel='stylesheet'> tags with inline <style> blocks.
        
        xhtml2pdf cannot resolve relative href paths from in-memory HTML,
        so we read the CSS files from disk and inject them directly.
        """
        def replace_link(match):
            href = match.group(1) or match.group(2)
            css_path = os.path.join(self.project_root, href)
            try:
                with open(css_path, 'r', encoding='utf-8') as f:
                    css_content = f.read()
                return f"<style>\n{css_content}\n</style>"
            except FileNotFoundError:
                print(f"Warning: CSS file not found: {css_path}")
                return ""
        
        # Match <link rel="stylesheet" href="..."> in either quote style / attribute order
        pattern = r'<link\s+[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']stylesheet["\'][^>]*/?>|<link\s+[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\'][^>]*/?>'
        return re.sub(pattern, replace_link, html_content)
    
    def html_to_pdf(self, html_content: str) -> bytes:
        """Convert HTML to PDF bytes"""
        if not HAS_XHTML2PDF:
            raise ImportError(
                "xhtml2pdf is not installed. "
                "Run: pip install xhtml2pdf"
            )

        try:
            # Inline any external CSS so xhtml2pdf can render styles
            html_content = self._inline_css(html_content)
            
            result = BytesIO()
            
            # Convert HTML to PDF using xhtml2pdf
            pisa_status = pisa.CreatePDF(  # type: ignore[union-attr]
                src=html_content,
                dest=result,
                encoding='utf-8'
            )
            
            if pisa_status.err:
                raise RuntimeError(f"PDF generation failed with {pisa_status.err} errors")
            
            return result.getvalue()
            
        except ImportError:
            raise
        except Exception as e:
            print(f"Error generating PDF: {e}")
            raise e
    
    def save_pdf(self, html_content: str, output_path: str) -> bool:
        """Save HTML as PDF file"""
        try:
            pdf_bytes = self.html_to_pdf(html_content)
            
            with open(output_path, 'wb') as f:
                f.write(pdf_bytes)
            
            return True
            
        except Exception as e:
            print(f"Error saving PDF: {e}")
            return False
