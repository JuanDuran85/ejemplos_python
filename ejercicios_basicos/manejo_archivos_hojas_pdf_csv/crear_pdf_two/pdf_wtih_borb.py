from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF

def main(pdf_path):
    pdf = Document()
    
    # Add a blank page
    page = Page()
    pdf.append_page(page)
    
    # Create a layout to hold the text
    layout = SingleColumnLayout(page)
    
    # Add some text using the Paragraph class
    layout.add(Paragraph("New text in PDF witn Borb and Python!"))
    
    with open(pdf_path, "wb") as pdf_fh:
        PDF.dumps(pdf_fh, pdf)
        
if __name__ == "__main__":
    main("borb_pdf_wtih_borb.pdf")