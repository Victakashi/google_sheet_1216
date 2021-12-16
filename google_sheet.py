
# from oauth2client.service_account import ServiceAccountCredentials
import gspread
# scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/driver.file', 'https://www.googleapis.com/auth/driver']

# creds = ServiceAccountCredentials.from_json_keyfile_name('Python Sheet API Key.json',scope)
# client = gspread.authorize(creds)

# abc = client.open("MZ_bot").worksheet("MZ_1")
# abc.update_cell(1,1,"Hello world")



sa = gspread.service_account()
sh = sa.open("MZ_bot")
wks = sh.worsheet("MZ_1")

wks.update('A3', 'Good')


