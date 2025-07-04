import gspread
from google.oauth2.service_account import Credentials
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
import platform

# ------------------------------------------
# Welcome Message
# ------------------------------------------
print("\n" + "=" * 60)
print("DIGITAL STRESS SURVEY & ANALYSIS TOOL")
print("=" * 60)
print("""
Welcome! This interactive program will guide you through a short survey 
about your digital habits, screen time, and stress levels.

What you'll do:
- Answer a few simple questions about your tech usage and stress.
- Get a **personalized recommendation** to improve your digital well-being.
      
""")

# ------------------------------------------
# 1. Connect to Google Sheets
# ------------------------------------------
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

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
        "Age", "Screen Time", "Social Networks", "Remote Work",
        "Digital Fatigue", "Stress Level", "Facebook Hrs", "Instagram Hrs",
        "TikTok Hrs", "Games Hrs", "Total Network Time",
        "Personal Recommendation", "Group Recommendation"
    ]
    if current_headers != headers:
        worksheet.clear()
        worksheet.insert_row(headers, index=1)
    return worksheet.row_values(1)


# --------------------------------------------------------
# 3. Personal recommendation
# --------------------------------------------------------
def personal_recommendation(stress, fatigue, screen_time):
    """Generate a personal recommendation based on screen time,"""
    """stress, and fatigue."""
    if screen_time <= 3 or stress == "low" or fatigue == "no":
        return "Your usage is low. Great balance!"
    elif screen_time <= 6 or fatigue == "sometimes":
        return (
            "Moderate usage. Try to reduce screen time and take "
            "screen breaks every hour."
        )
    else:
        return (
            "High usage. Consider reducing screen time and doing "
            "physical or outdoor activities."
        )


# --------------------------------------------------------
# 4. Group recommendation
# --------------------------------------------------------
def group_recommendation(stress, fatigue, screen_time):
    """
    Generate a group recommendation based on stress, fatigue, and screen time.
    """
    if stress == "high" or fatigue == "yes" or screen_time > 5:
        return (
            "Group stress is high. Recommended digital detox strategies and "
            "emotional wellness support."
        )
    elif stress == "medium":
        return (
            "Group stress is moderate. Encourage screen breaks and "
            "physical social time."
        )
    else:
        return "Group stress is low. Keep up the healthy tech habits!"


# --------------------------------------------------------
# 5. Network detailed usage
# --------------------------------------------------------
def network_usage(network_count):
    """Collect detailed usage hours for specific social networks """
    """if network_count > 0. Returns a tuple: """
    """(list of hours [Facebook, Instagram, TikTok, Games], total hours)"""

    all_networks = ["Facebook", "Instagram", "TikTok", "Games"]

    if network_count == 0:
        return [0, 0, 0, 0], 0

    usage_hours = []
    for network in all_networks:
        while True:
            hours_input = input(
                f"How many hours per day do you spend on {network}? \n"
                "(e.g., 1): \n"
            ).strip()
            try:
                hours = int(hours_input)
                if hours < 0:
                    print("Hours cannot be negative.\n")
                else:
                    usage_hours.append(hours)
                    break
            except ValueError as e:
                print("Please enter a valid number for hours.\n")
                print(f"(Details: {e})\n")

    total_hours = sum(usage_hours)
    return usage_hours, total_hours


# ---------------------------
# 6. Categorize age
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
        print(f"Invalid age: {e}. Enter a number.\n")
        return False


# --------------------------------------------------------
# 7. Main survey with validation per question
# --------------------------------------------------------
def run_survey():
    """
    Run the digital stress survey, validate input one-by-one giving feedback
    if there's an error, and save to Google Sheet.
    """
    print("--- Let's get started! ---\n")

    while True:
        age_input = input("Your age (e.g., 25): \n").strip()
        try:
            age = int(age_input)
            if age <= 0:
                print("Age must be a positive number.\n")
            else:
                break
        except ValueError as e:
            print("Invalid age. Enter a number.\n")
            print(f"(Details: {e})\n")

    while True:
        screen_input = input(
            "How many hours of screen time per day? (e.g., 2): \n"
        ).strip()
        try:
            screen_time = int(screen_input)
            if screen_time < 0:
                print("Screen time cannot be negative.\n")
            else:
                break
        except ValueError as e:
            print("Invalid screen time. Enter a number.\n")
            print(f"(Details: {e})\n")

    while True:
        network_input = input(
            "How many social networks do you actively use? (e.g., 3): \n"
        ).strip()
        try:
            networks = int(network_input)
            if networks < 0:
                print("Must be zero or more.\n")
            else:
                break
        except ValueError as e:
            print("Please enter a valid number for social networks.\n")
            print(f"(Details: {e})\n")

    remote_options = ["yes", "partly", "no"]
    while True:
        remote = input(
            "Work/study from home? (yes / partly / no): \n"
        ).strip().lower()
        if remote in remote_options:
            break
        else:
            print("Please enter: yes, partly, or no.\n")

    fatigue_options = ["no", "sometimes", "yes"]
    while True:
        fatigue = input(
            "Do you feel digital fatigue? (no / sometimes / yes): \n"
        ).strip().lower()
        if fatigue in fatigue_options:
            break
        else:
            print("Please enter: no, sometimes, or yes.\n")

    stress_options = ["low", "medium", "high"]
    while True:
        stress = input(
            "Stress level at end of day? (low / medium / high): \n"
        ).strip().lower()
        if stress in stress_options:
            break
        else:
            print("Please enter: low, medium, or high.\n")

    if networks > 0:
        print("\nTell us about your usage of specific apps...\n")

    network_hours, total_network_time = network_usage(networks)

    print("\nTHANK YOU FOR COMPLETING THE SURVEY!\n")

    p_recommendation = personal_recommendation(stress, fatigue, screen_time)
    g_recommendation = group_recommendation(stress, fatigue, screen_time)

    print(f"Personal Recommendation:\n  {p_recommendation}\n")
    print(f"Group Recommendation:\n  {g_recommendation}\n")

    row_data = [
        age, screen_time, networks, remote, fatigue, stress
    ] + network_hours + [
        total_network_time, p_recommendation, g_recommendation]

    worksheet = SHEET.worksheet("responses")
    worksheet.append_row(row_data)


# ------------------------------------------
# 8. Analysis responses
# ------------------------------------------
def analyze_responses(worksheet):
    """
    Analyze and print summary statistics from the responses.
    """
    records = worksheet.get_all_records()
    if not records:
        print("No data to analyze.\n")
        return

    total_screen_time = sum(int(record["Screen Time"]) for record in records)
    total_network_time = sum(
        int(record["Total Network Time"]) for record in records)

    avg_screen_time = total_screen_time / len(records)
    avg_network_time = total_network_time / len(records)

    last_entry = records[-1]
    user_screen_time = int(last_entry["Screen Time"])
    user_network_time = int(last_entry["Total Network Time"])

    if user_screen_time < avg_screen_time:
        print("Screen Time: Below average. Well done!\n")
    elif user_screen_time > avg_screen_time:
        print("Screen Time: Above average. Consider taking regular breaks.\n")
    else:
        print("Screen Time: At average. Try small improvements.\n")

    if user_network_time < avg_network_time:
        print("Social Network Usage: "
              "Less than average. Great job staying focused!\n")
    elif user_network_time > avg_network_time:
        print("Social Network Usage: Above average. Try setting limits.\n")
    else:
        print("Social Network Usage: On par with average. "
              "Consider cutting back.\n")

    stress_levels = {"low": 0, "medium": 0, "high": 0}
    for record in records:
        stress = record["Stress Level"].lower()
        if stress in stress_levels:
            stress_levels[stress] += 1

    print("\nStress Level Distribution:\n")
    for level, count in stress_levels.items():
        percentage = (count / len(records)) * 100
        print(f"  {level.capitalize()}: {count} ({percentage:.2f}%)\n")


# ------------------------------------------
# 9. Execute
# ------------------------------------------
worksheet = SHEET.worksheet("responses")
ensure_headers(worksheet)
run_survey()
analyze_responses(worksheet)


# ------------------------------------------
# 10. Load data into DataFrame and plot
# ------------------------------------------
data = worksheet.get_all_records()
df = pd.DataFrame(data)

if df.empty:
    print("No data available to plot.\n")
else:
    numeric_columns = [
        "Screen Time", "Facebook Hrs", "Instagram Hrs",
        "TikTok Hrs", "Games Hrs", "Total Network Time"
    ]
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    group_avg = df[numeric_columns].mean()
    personal_data = df.iloc[-1][numeric_columns]

    labels = numeric_columns
    personal_vals = personal_data.values
    group_vals = group_avg.values

    fig, ax = plt.subplots(figsize=(8, 6))
    x = range(len(labels))
    bar_width = 0.25

    ax.bar(x, personal_vals, width=bar_width,
           label="Personal", edgecolor='black')
    ax.bar(
        [i + bar_width for i in x], group_vals,
        width=bar_width, label="Group Average", edgecolor='black'
    )

    ax.set_title(
        "PERSONAL RESULTS VS GROUP AVERAGES",
        fontsize=16, fontweight='bold', pad=20
    )
    ax.set_xlabel("Metrics", fontsize=14)
    ax.set_ylabel("Hours", fontsize=14)
    ax.set_xticks([i + bar_width / 2 for i in x])
    ax.set_xticklabels(labels, rotation=20, ha='right', fontsize=12)
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper right', fontsize=12)

    plt.tight_layout()
    plt.savefig("chart.png")
