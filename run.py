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
    """
    Ensure the worksheet has the correct headers.
    If not, insert them at the top.
    """

    current_headers = worksheet.row_values(1)

    headers = [
        "Age", "Screen Time", "Social Networks", "Remote Work", "Digital Fatigue", "Stress Level",
        "Facebook Hrs", "Instagram Hrs", "TikTok Hrs", "Games Hrs", "Recommendation"
    ]

    # Check if current headers match expected ones
    if current_headers != headers:
        worksheet.insert_row(headers, index=1)

    return worksheet.row_values(1)

# --------------------------------------------------------
# 4. Run Survey, Validate Data and Save Responses to Sheet
# --------------------------------------------------------

def run_survey():
    """
    Run the digital stress survey, validate input one-by-one giving feedback if has an error, and save to Google Sheet.
    """

    print("\n--- Digital Stress Survey ---\n")

    # Validate age
    while True:
        age_input = input("Your age (e.g., 25): \n").strip()
        try:
            age = int(age_input)
            if age <= 0:
                print(" Age must be a positive number. \n")
            else:
                break
        except ValueError as e:
            print(f" Please enter a valid number for age. \n")
            print(f"(Details: {e}) \n")

    # Validate screen time
    while True:
        screen_input = input("How many hours of screen time per day? (e.g., 2): \n").strip()
        try:
            screen_time = int(screen_input)
            if screen_time < 0:
                print(" Screen time cannot be negative. \n")
            else:
                break
        except ValueError as e:
            print(" Please enter a valid number for screen time. \n")
            print(f"(Details: {e}) \n")

    # Validate number of networks
    while True:
        network_input = input("How many social networks do you actively use? (e.g., 3): \n").strip()
        try:
            networks = int(network_input)
            if networks < 0:
                print(" Number of networks must be zero or more. \n")
            else:
                break
        except ValueError as e:
            print(" Please enter a valid number for social networks. \n")
            print(f"(Details: {e}) \n")

    # Validate remote work input
    remote_options = ["yes", "partly", "no"]
    while True:
        remote = input("Work/study from home? (yes / partly / no): \n").strip().lower()
        if remote in remote_options:
            break
        else:
            print(" Please enter: yes, partly, or no. \n")

    # Validate digital fatigue
    fatigue_options = ["no", "sometimes", "yes"]
    while True:
        fatigue = input("Do you feel digital fatigue? (no / sometimes / yes): \n").strip().lower()
        if fatigue in fatigue_options:
            break
        else:
            print(" Please enter: no, sometimes, or yes. \n")

    # Validate stress level
    stress_options = ["low", "medium", "high"]
    while True:
        stress = input("Stress level at end of day? (low / medium / high): \n").strip().lower()
        if stress in stress_options:
            break
        else:
            print(" Please enter: low, medium, or high. \n")

    # Final data to append
    final_data = [age, screen_time, networks, remote, fatigue, stress]

    # Append to worksheet
    worksheet = SHEET.worksheet("responses")
    worksheet.append_row(final_data)

    print("\n Thank you for completing the survey! \n")



# ---------------------------
# 5. Categorize age
# ---------------------------
def age_group(age):
    """
    Categorize age into groups.
    """

    try:
        age = int(age)
        if age < 18:
            return "<18"
        elif 18 <= age <= 25:
            return "18–25"
        elif 26 <= age <= 35:
            return "26–35"
        elif 36 <= age <= 50:
            return "36–50"
        else:
            return "51+"
    except ValueError as e:
        print(f"Invalid age: {e}, please enter a number. \n")
        return False


# ------------------------------------------
# 6. Execute
# ------------------------------------------
worksheet = SHEET.worksheet("responses")
ensure_headers(worksheet)
run_survey()