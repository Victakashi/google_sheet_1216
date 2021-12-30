# from oauth2client.service_account import ServiceAccountCredentials
import gspread

gc = gspread.service_account(filename = "mzbot123001.json")

# scope = ['https://www.googlapis.com/feeds',
#          'https://www.googlapis.com/auth/spreadsheets',
#          'https://www.googleapis.com/auth/drive.file',
#          'https://www.googlapis.com/auth/drive']


# gc = gspread.service_account(filename=　'mzbot123001.json')

# # gc = gspread.oauth(
# #     credentials_filename='mzbotgoogledriver.json',
# #     authorized_user_filename='mzbotgoogledriver.json',
# #     )

# credentials = {
#     {
#         "installed": {
# 　"type": "service_account",
#   "project_id": "mzbot123001",
#   "private_key_id": "0538718f3ace1de4c969bcac1b24eb555cd4cd2f",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCzrWWGin0bode3\nBdN0+0ndYQBzpDux0Dn8+hYhyQBuM6VMkGwiiGhpcOPqCCvEeYr3IFrATK2QHCkP\noy1ZiAwYfws+2/edDoOvnzaBX5Hk1Zjew+fk7RZmxgj2s5dTq01dHFOESpUzsqV3\nJmuM2On877Ql63zkR7DP8TDNGXcQwaAq06axBYeUJWGJbov9Cv2b7t9a3+ilfOGo\n6kCLrOpP9KqEvYhk/N8c0pt6HhSxP+H0ix8ZfoCA7Accg8Q6LE5jN4+wedcALx5g\nSd86ukuUKbOaoxFNIJpn3q9alZxtAfvdlE866N27oCDw3Zf/RvW6ABQzg0Ve1MN9\nSN1KiOZHAgMBAAECggEAKbWnW0ebykXUKx71mvLYj0T801t9JgZl57VwXNBpwqtH\nhJIEIDIVNuDnb4UND/N9EGgY2QoTwl/fIkupc96ynB8lz6ZFgVaEuEiX4Ql79yik\nb5X/p3NoH1x6aTaAewJJl8NDGfMsVo9yfMnU7qHOE5LbeXAEkoOX5nWhdAMk0iUU\nwR0k0m24CkIFRkD1coW2mx3vzSVc4XtgfmNTc8GNe9VGA7TAoDz0hFF+FJtPApmF\n6hxs/DitzUB0W6/L8Hi6+89YxMe7828M6iWWkpvbYVTHY5qCTG803FY7gEIxzI68\nEXGQBGPa9HcaccovuK8QbDWvHMn+v/NRuPhDgPMRbQKBgQDmj/PjtFD43lzzLb0p\n8TcCREMRjE9+6vGGtEeX+o5QmO8QLhd+P8pwhDPVZY8LAGyES4FBp8lMSREYqWk2\n5Y4Q4V47OUNfF59/cXlvXzSfzS/Oj7bDq7FYiVeS02IGUa4P+qfp1hw9reo6Bluu\nGGpTJX/sHJx1K9Bgz57sChX7CwKBgQDHgD0G/AXq1K00Rk05byXNPSjBYO6x9BbC\no944jA3yKRBKaxBZGTb2b+6WMEQ7ElJX5zWL9Me9G7lrFgWMtjrIud6R/fbxJTKa\nU8tAH7tzZzF6wYIEIWnZzzJY68QHnDCMcrwLPBAaz4qoYTQ9RAdu5A7AwRtFc6yh\nAFX9/H/nNQKBgC7/Yvikdej08r+DME8PY2Yr4fv+vOmjHI6Xyww4v6/ALOMAcjuC\n51IeMK6sIAdfE7+34GYwvIC3WCvNxKuzCU15kwrBdnE40INa7yT7pC961ObnNpsW\nMXVZsac1PYMKPU/2iSnKQkF0ZQ1k5GVNhsbiGvxXLLFZuAUz7TIyMB7XAoGAThP5\nTm96HWLo+ql89bpzT/Tcq3o1UP4Xnkul3/moR5scnhNyzXwZz68U8ECpo3jTM0Xw\n5fqB5ZghJDD1MRHsxbxAyGBdshj9yfp7dHg2076SVdm/+b/d/nmh2b1D9jqBoaYR\nxE/YebW6LZYFbOjgA91LjNLGypKwAD7yaLnWkPUCgYEAuhSknAUYm4/HLC8yDvsx\n4elRVXSiQJz+//QULq7zxKN+DZB4XYE9mbpmbX3gNgfCGQvefuHCk6+nV2T9RbU9\nWsHuh0r4Tqc5kBNg0USSYZCagfDOJSVhH2BLp3c6hcqw7rSXPHFD8n+ZmVCjT1Fs\nuA1DvXCsLTr24P3jNSEUDbM=\n-----END PRIVATE KEY-----\n",
#   "client_email": "mzbot12301@mzbot123001.iam.gserviceaccount.com",
#   "client_id": "113222482334239165633",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mzbot12301%40mzbot123001.iam.gserviceaccount.com"
#         }
#     }
# }

# gc, authorized_user = gspread.oauth_from_dict(credentials)


sheet = gc.open_by_key("15g-2coTEOJ5NzERQHg6N-8fKyHnUGo-g2cxX-xyTPv8")

worksheet = sheet.sheet1

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








