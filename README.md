# MultiMessenger

A Python script that automates the process of sending a message to multiple contacts using the Windows keyboard and mouse.

## Prerequisites

- Whatsapp Desktop Application
- Make sure the whatsapp app is running along with the terminal where you are running the script in a seperate window (This window should have whatsapp application open in the background and the terminal should be in the foreground).

## Usage

### Environment Setup(Optional) :

1. Install Python 3.10 or above.
2. Create a virtual environment using the following command:
   `python -m venv venv`
3. Activate the virtual environment.
   `source venv/bin/activate`

### Installation :

- Clone the repository using the following command:
  `git clone https://github.com/ani-sh-arma/MultiMessenger.git`
- Install the required packages using the following command:
  `pip install -r requirements.txt`

### Running the Script :

1. Open the directory containing the script in a terminal.
2. Make sure your excel file is also in the same directory.
3. Run the xcript using the following command/

`python mulmess.py <excel_file_name>`

Replace <excel_file_name> with the actual name of the Excel file containing the contact numbers and names.

## Example

Suppose you have an Excel file named "contacts.xlsx" with the following content:

| Phone Number      | Name        |
| ----------------- | ----------- |
| +1 (555) 123-4567 | John Doe    |
| +1 (555) 987-6543 | Jane Smith  |
| +1 (555) 456-7890 | Bob Johnson |
| +1 (555) 321-0987 | Sarah Lee   |
| +1 (555) 789-2345 | Tom Wilson  |

To run the script :

`python mulmess.py contacts.xlsx`

This will open the Excel file, extract the contact numbers and names, and send a message to each contact.

## Limitations

1. The script that you have an excel file with the data of contacts and the excel file contains atleast two columns Names and Phone Number.
2. The script will only work if the excel file is in the same directory as the script.
3. This script is only designed for whatsapp desktop application.
4. The script will remove any country code and any characters other than digits from the phone number. Because whatsapp phone number search only allowas digits without any country codes.

## Contributing

If you find any bugs or have any suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
