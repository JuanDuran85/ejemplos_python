from openpyxl import Workbook

try:
    workbook_one = Workbook()
    sheet = workbook_one.active

    sheet["A1"] = "New line"
    sheet["A2"] = " Other new line"
    sheet["A3"] = "another new line with OpenPyXL"

    workbook_one.save("new_file.xlsx")
    print("File created successfully")
except Exception as e:
    print(f"Error --> {e}")