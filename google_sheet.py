
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']

gc = gspread.service_account(filename= "client_secret.json")

#sheet = gc.open_by_key('15g-2coTEOJ5NzERQHg6N-8fKyHnUGo-g2cxX-xyTPv8').sgeet1
sheet = gc.open('MZ_bot').sgeet1

sheet.update_cell(1,1,"Hello world121701")






