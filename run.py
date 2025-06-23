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

    expected_headers = [
        "Horas de pantalla",
        "Redes sociales",
        "Trabajo remoto",
        "Fatiga digital",
        "Nivel de estrés"
    ]

    # Check if current headers match expected ones
    if current_headers != expected_headers:
        worksheet.insert_row(expected_headers, index=1)

    return worksheet.row_values(1)


# ------------------------------------------
# 3. Run Survey and Save Responses to Sheet
# ------------------------------------------
def run_survey():
    print("--- Encuesta sobre Salud Digital y Estrés Tecnológico ---\n")
    horas_pantalla = input("¿Cuántas horas al día usas pantallas? (1-2 / 3-5 / 6+): \n")
    redes = input("¿Cuántas redes sociales usas activamente? (0 / 1-2 / 3+): \n")
    remoto = input("¿Trabajas o estudias desde casa? (sí / parcialmente / no): \n")
    fatiga = input("¿Sientes fatiga digital? (no / a veces / sí): \n")
    estres = input("¿Nivel de estrés al final del día? (bajo / medio / alto): \n")
    print("Thank you for completing the survey!")

    # Append to Google Sheet
    worksheet = SHEET.worksheet("responses")
    worksheet.append_row([horas_pantalla, redes, remoto, fatiga, estres])
    print(f"{worksheet} worksheet updated successfully.")

# ------------------------------------------
# 3. Execute
# ------------------------------------------
worksheet = SHEET.worksheet("responses")
ensure_headers(worksheet)
run_survey()