"""_summary_

    Using library xlsxwriter to create an excel file.


"""

from xlsxwriter import Workbook

try:
    work_book: Workbook = Workbook('ejemplo.xlsx')
    sheet = work_book.add_worksheet(name="ejemplo")

    data: list = [15,45,56,34,1,67]
    sheet.write_column("A1",data)

    # create the chart object
    chart = work_book.add_chart({'type':'line'})
    chart.add_series({'values':'=ejemplo!$A$1:$A$6'})

    # add the chart to the spreadsheet
    sheet.insert_chart("C1",chart)
    work_book.close()
except Exception as e:
    print(e)