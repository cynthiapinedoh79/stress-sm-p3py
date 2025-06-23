import gspread
from google.oauth2.service_account import Credentials

def get_google_sheet(worksheet_name):
    SCOPE = ["https://spreadsheets.google.com/feeds", 
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

    # Load credentials from JSON keyfile
    CREDS = Credentials.from_service_account_file("creds.json", scopes=SCOPE)
    GSPREAD_CLIENT = gspread.authorize(CREDS)
    SHEET = GSPREAD_CLIENT.open("stress-sm-p3py")


    worksheet = SHEET.worksheet(worksheet_name)
    data = worksheet.get_all_values()
    print(data)

# Example call:
get_google_sheet("stress")