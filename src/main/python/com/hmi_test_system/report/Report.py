from reportlab.lib import letter
from reportlab.pdfgen import canvas

class Report:  
    
    pdf_filename = "Report.pdf"
    pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)

    

    pdf_canvas.save()