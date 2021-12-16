
#from oauth2client.service_account import ServiceAccountCredentials
import gspread
scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']

gc = gspread.service_account(filename= "Python Sheet API Key.json")

sheet = gc.open("MZ_bot").worksheet("MZ_1")
sheet.update_cell(1,1,"Hello world123")



# client = gspread.authorize(creds)

# abc = client.open("MZ_bot").worksheet("MZ_1")
# abc.update_cell(1,1,"Hello world")



#sa = gspread.service_account()



# sh = sa.open("MZ_bot")
# wks = sh.worsheet("MZ_1")

# wks.update_cell('A3', 'Good')


