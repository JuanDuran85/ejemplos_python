from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def simple_table() -> None:
    doc: SimpleDocTemplate = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
    story: list = []
    
    data: list = [['col_{}'.format(x) for x in range(1,6)], [str(x) for x in range(1,6)], ['a','b','c','d','e']]
    
    tbl: Table = Table(data)
    story.append(tbl)
    
    doc.build(story)
    print("simple_table.pdf generated")
    
    
def simple_table_with_style() -> None:
    doc_two: SimpleDocTemplate = SimpleDocTemplate("simple_table_with_style.pdf", pagesize=letter)
    story_two: list = []
    
    data_two: list = [['col_{}'.format(x) for x in range(1,6)], [str(x) for x in range(1,6)], ['a','b','c','d','e']]
    
    tbl_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.red),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.blue)])
    
    tbl_two: Table = Table(data_two)
    tbl_two.setStyle(tbl_style)
    story_two.append(tbl_two)
    
    doc_two.build(story_two)
    print("simple_table_with_style.pdf generated")
    
if __name__ == "__main__":
    simple_table()
    simple_table_with_style()
    