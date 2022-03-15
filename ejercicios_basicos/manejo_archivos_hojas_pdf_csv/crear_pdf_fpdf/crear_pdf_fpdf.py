"""_summary_

    Using FPFG Library

"""

from fpdf import FPDF

pdf_file: FPDF = FPDF()
pdf_file.add_page()
pdf_file.set_font('Arial', 'B', 16)
pdf_file.cell(200, 10, txt="Creando PDF con la libreria FPDF de Python", ln=1, align="C")
pdf_file.output("archivo.pdf")