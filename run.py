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
        "Facebook Hrs", "Instagram Hrs", "TikTok Hrs", "Games Hrs", "Personal Recommendation", "Group Recommendation"
    ]

    # Check if current headers match expected ones
    if current_headers != headers:
        worksheet.clear()
        worksheet.insert_row(headers, index=1)

    return worksheet.row_values(1)

# --------------------------------------------------------
# 4. Personal recommendation
# --------------------------------------------------------
"""
Generate a personal recommendation based on hours of screen time.
"""
def personal_recommendation(stress, fatigue, screen_time):
    if screen_time <= 3 or stress=="low" or fatigue=="no":
        return "Your usage is low. Great balance!"
    elif screen_time <=6 or fatigue == "sometimes":
        return "Moderate usage. Try to reduce screen time and take screen breaks every hour."
    else:
        return "High usage. Consider reducing screen time and doing physical or outdooor activities"
    

# --------------------------------------------------------
# 5. Group recommendation
# --------------------------------------------------------
"""
Generate a group recommendation based on stress, fatigue, and screen time.
"""
def group_recommendation(stress, fatigue, screen_time):
    if stress == "high" or fatigue == "yes" or screen_time > 5:
        return "Group stress is high. Recommended digital detox strategies and emotional wellnes support."
    elif stress == "medium":
        return "Group stress is moderate. Encourage screen breaks and physical social time."
    else:
        return "Group stress is low. Keep up the healthy tech habits!."

# --------------------------------------------------------
# 4. Network detailed usage
# --------------------------------------------------------
def network_usage(network_count):
    """
    Collect detailed usage hours for specific social networks if network_count > 0.
    Returns a list of hours [Facebook, Instagram, TikTok, Games] or [0, 0, 0, 0]
    """
    all_networks = ["Facebook", "Instagram", "TikTok", "Games"]

    if network_count == 0:
        return [0, 0, 0, 0]

    usage_hours = []
    for network in all_networks:
        while True:
            hours_input = input(f"How many hours per day do you spend on {network}? (e.g., 1): \n").strip()
            try:
                hours = int(hours_input)
                if hours < 0:
                    print(" Hours cannot be negative.\n")
                else:
                    usage_hours.append(hours)
                    break
            except ValueError as e:
                print(" Please enter a valid number for hours.")
                print(f"(Details: {e})")
    return usage_hours


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
    

# --------------------------------------------------------
# 6. Main survey
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
            print(f"Invalid age. Enter a number. \n")
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
            print(" Invalid screen time. Enter a number. \n")
            print(f"(Details: {e}) \n")

    # Validate number of networks
    while True:
        network_input = input("How many social networks do you actively use? (e.g., 3): \n").strip()
        try:
            networks = int(network_input)
            if networks < 0:
                print("Must be zero or more. \n")
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

    # Collect network usage
    print("\n Tell us about your usage of specific apps...\n")
    network_hours = network_usage(networks)


    # Generate recommendation
    p_recommendation = personal_recommendation(stress, fatigue, screen_time)
    g_recommendation = group_recommendation(stress, fatigue, screen_time)

    print(f"\n Personal Recommendation: {p_recommendation} \n")
    print(f"\n Group Recommendation: {g_recommendation} \n")

    # Combine all data
    row_data = [age, screen_time, networks, remote, fatigue, stress] + network_hours + [p_recommendation, g_recommendation]

    # Append to worksheet
    worksheet = SHEET.worksheet("responses")
    worksheet.append_row(row_data)

    print("\n Thank you for completing the survey! \n")


# ------------------------------------------
# 7. Execute
# ------------------------------------------
worksheet = SHEET.worksheet("responses")
ensure_headers(worksheet)
run_survey()