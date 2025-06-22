import gspread
from oauth2client.service_account import Credentials

def get_google_sheet(sheet_name, worksheet_name):
    SCOPE = ["https://spreadsheets.google.com/feeds", 
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

    # Load credentials from JSON keyfile
    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("love_sandwiches")

    worksheet = SHEET.worksheet(worksheet_name)
    return worksheet

