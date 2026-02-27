from flask import Blueprint, render_template, send_file
from io import BytesIO

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/resume.pdf')
def download_resume():
    # Generate a simple PDF placeholder
    from io import BytesIO
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Professional Resume")
    p.drawString(100, 730, "John Doe - Software Developer")
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='resume.pdf', mimetype='application/pdf')
