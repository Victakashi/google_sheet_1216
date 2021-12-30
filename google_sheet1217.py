
import gspred

gc = gspread.service_account(filename = 'mzbotgoogledriver.json')

#gspread.service_account(filename='/home/docs/.config/gspread/service_account.json', scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])


sheet = gc.open_by_key("15g-2coTEOJ5NzERQHg6N-8fKyHnUGo-g2cxX-xyTPv8")

worksheet = sh.sheet1

worksheet.update_cell(1,1, "Hello world888999993")


# from oauth2client.service_account import ServiceAccountCredentials
# import gspread
# import pandas
# import json
# import os

# scope = ['https://www.googlapis.com/feeds',
#          'https://www.googlapis.com/auth/spreadsheets',
#          'https://www.googleapis.com/auth/drive.file',
#          'https://www.googlapis.com/auth/drive']


# json_creds = os.getenv("client_secret.json")

# creds_dict = json.loads(json_creds)
# creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
# creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
# gc = gspread.authorize(creds)


# # gc = gspread.service_account(filename= "client_secret.json")
# sheet = gc.open("MZ_bot").worksheet("MZ_1")
# sheet.update_cell(1,1,"Hello world888999993")








