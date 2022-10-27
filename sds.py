import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
"""cope = ['https://docs.google.com/spreadsheets/u/0/']
creds = ServiceAccountCredentials.from_json_keyfile_name('logistica5-tableros-cbcc5f8d90e6.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("CopiaReporte")

# Extract and print all of the values
lis1t_of_hashes = sheet.get_all_records()"""
#print(list_of_hashes)
ls=[1,2,3,4,5,60]
print(len(ls))