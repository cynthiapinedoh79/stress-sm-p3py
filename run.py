import gspread
from google.oauth2.service_account import Credentials

# ------------------------------------------
# 1. Connect to Google Sheets
# ------------------------------------------
SCOPE = ["https://spreadsheets.google.com/feeds", 
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"
    ]

# Load credentials from JSON keyfile
CREDS = Credentials.from_service_account_file("creds.json", scopes=SCOPE)
GSPREAD_CLIENT = gspread.authorize(CREDS)
SHEET = GSPREAD_CLIENT.open("stress-sm-p3py")

# ------------------------------------------
# 2. Ensure headers exist
# ------------------------------------------
def ensure_headers(worksheet):
    current_headers = worksheet.row_values(1)

    headers = [
        "Age", "Screen Time", "Social Networks", "Remote Work", "Digital Fatigue", "Stress Level",
        "Facebook Hrs", "Instagram Hrs", "TikTok Hrs", "Games Hrs", "Recommendation"
    ]

    # Check if current headers match expected ones
    if current_headers != headers:
        worksheet.insert_row(headers, index=1)

    return worksheet.row_values(1)


# ------------------------------------------
# 3. Run Survey and Save Responses to Sheet
# ------------------------------------------
def run_survey():
    print("--- Digital Stress Survey ---\n")
    age = input("Your age: \n").strip()
    screen_time = input("Daily screen time? (1-2 / 3-5 / 6+): \n").strip().lower()
    networks = input("Active social networks? (0 / 1-2 / 3+): \n").strip().lower()
    remote = input("Work/study from home? (yes / partly / no): \n").strip().lower()
    fatigue = input("Do you feel digital fatigue? (no / sometimes / yes): \n").strip().lower()
    stress = input("Stress level at end of day? (low / medium / high): \n").strip().lower()
    print("Thank you for completing the survey!")

    # Append to Google Sheet
    worksheet = SHEET.worksheet("responses")
    worksheet.append_row([age, screen_time, networks, remote, fatigue, stress])
    print(f"{worksheet} worksheet updated successfully.")

# ------------------------------------------
# 3. Execute
# ------------------------------------------
worksheet = SHEET.worksheet("responses")
ensure_headers(worksheet)
run_survey()