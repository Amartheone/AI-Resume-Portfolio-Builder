"""
PDF Exporter Module
Uses browser-based print-to-PDF approach for Streamlit Cloud compatibility.
No native C libraries required.
"""
from io import BytesIO
import base64


class PDFExporter:
    """Export HTML documents — provides downloadable HTML that users can print to PDF"""

    def html_to_pdf(self, html_content: str) -> bytes:
        """
        Wrap HTML content into a self-contained, print-ready HTML file.
        Returns UTF-8 bytes of the HTML file.
        Users can open it in a browser and use Ctrl+P / Cmd+P to save as PDF.
        """
        # Build a self-contained HTML document with print-optimized styles
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
<style>
  @media print {{
    body {{ margin: 0; padding: 20px; }}
    .no-print {{ display: none !important; }}
  }}
  .print-banner {{
    background: #4F46E5;
    color: white;
    text-align: center;
    padding: 12px 20px;
    font-family: sans-serif;
    font-size: 14px;
    border-radius: 8px;
    margin-bottom: 20px;
  }}
  .print-banner button {{
    background: white;
    color: #4F46E5;
    border: none;
    padding: 8px 24px;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    margin-left: 12px;
    font-size: 14px;
  }}
</style>
</head>
<body>
<div class="print-banner no-print">
  📄 To save as PDF, click the button or press <b>Ctrl+P</b> / <b>Cmd+P</b>
  <button onclick="window.print()">🖨️ Print / Save PDF</button>
</div>
{html_content}
</body>
</html>"""
        return full_html.encode('utf-8')

    def save_pdf(self, html_content: str, output_path: str) -> bool:
        """Save HTML as a print-ready HTML file"""
        try:
            html_bytes = self.html_to_pdf(html_content)
            with open(output_path, 'wb') as f:
                f.write(html_bytes)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
