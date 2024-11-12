import pyautogui as pag
import pandas as pd
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python script.py <excel_file_name>")
    sys.exit(1)

# Read data from the Excel file
excel_file = sys.argv[1]
data = pd.read_excel(excel_file, engine="openpyxl")
contacts = data["Phone Number"].tolist()
names = data["Name"].tolist()


def extract_digits(input_string):
    # Use a regular expression to remove all non-digit characters
    cleaned_string = re.sub(r"[^0-9]", "", input_string)

    # Get the last 10 digits of the cleaned string
    last_10_digits = cleaned_string[-10:]

    return last_10_digits


pag.PAUSE = 0.5

pag.keyDown("alt")
pag.press("tab")
pag.keyUp("alt")

for i in range(len(contacts)):
    pag.hotkey("ctrl", "n")
    pag.write(extract_digits(contacts[i]), interval=0.01)
    pag.press("tab")
    pag.press("tab")
    pag.press("enter")

    greeting = f"Hello {names[i]},"
    message = (
        "How are you? This is an auto-generated message for you from Vishal Mobile."
    )
    print(f"{greeting}\n{message}")

    pag.write(greeting, interval=0.01)
    pag.hotkey("shift", "enter")
    pag.write(message, interval=0.01)
    pag.press("enter")
