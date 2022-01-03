import gspread

gc = gspread.service_account(filename = "mzbot123001.json")

sheet = gc.open_by_key("15g-2coTEOJ5NzERQHg6N-8fKyHnUGo-g2cxX-xyTPv8")
#worksheet = sheet.sheet1
worksheet = sh.worksheet("mz")
worksheet.update_cell(1,1, "Hello world888999993")
worksheet.update_cell(1,2, "Hello world8889922293")
worksheet.update_cell(1,3, "Hello world85559993")
worksheet.batch_clear(["A1:B1"])







