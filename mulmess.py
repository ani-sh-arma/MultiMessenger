import pyautogui as pag
import pandas as pd
import sys
import re
from cleanstring import str_utils

if len(sys.argv) != 2:
    print("Usage: python script.py <excel_file_name>")
    sys.exit(1)

# Read data from the Excel file
excel_file = sys.argv[1]
data = pd.read_excel(excel_file, engine="openpyxl")
contacts = data["Phone Number"].tolist()
names = data["Name"].tolist()

pag.PAUSE = 0.5

pag.hotkey("alt","tab")

for i in range(len(contacts)):
    val = str_utils.clean_string(names[i], str(contacts[i]))
    pag.hotkey("ctrl", "n")
    pag.write(
        val.get("contact"), interval=0.01
    )
    pag.press("tab")
    pag.press("tab")
    pag.press("enter")

    greeting = f"Hello {val.get("name")},"
    message = (
        "How are you? This is an auto-generated message for you from Vishal Mobile."
    )

    pag.write(greeting, interval=0.01)
    pag.hotkey("shift", "enter")
    pag.write(message, interval=0.01)
    pag.press("enter")
