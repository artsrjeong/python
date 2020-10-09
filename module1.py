import win32com.client
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.Workbooks.Open('F:\\temp\\Book1.xlsx')
ws=wb.ActiveSheet
print(ws.Cells(1,1).Value)
excel.Quit()
print("test")