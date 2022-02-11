"""[summary]

Generates a pdf file with one page.

"""

from reportlab.pdfgen import canvas

my_canvas = canvas.Canvas("font_pdf_demo.pdf")
my_canvas.drawString(100,750,"New PDF with Reportlab and Python")
my_canvas.save()