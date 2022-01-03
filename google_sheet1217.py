import gspread

gc = gspread.service_account(filename = "mzbot123001.json")

sheet = gc.open_by_key("15g-2coTEOJ5NzERQHg6N-8fKyHnUGo-g2cxX-xyTPv8")
#worksheet = sheet.sheet1
worksheet = sheet.worksheet("mz")

val = worksheet.acell('B7').value
worksheet.update_cell(1,1, "Hello world888999993")
worksheet.update_cell(1,2, str(val))
worksheet.update_cell(1,3, val)
#worksheet.batch_clear(["A1:B1"])







