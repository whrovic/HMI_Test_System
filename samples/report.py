from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Create a new PDF document with the given filename
pdf_filename = "Example Report.pdf"
pdf_canvas = canvas.Canvas(pdf_filename, pagesize=A4)

# Add some text to the PDF
pdf_canvas.drawString(100, 750, "Example PDF Report")

# Save the PDF document
pdf_canvas.save()