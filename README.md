# hackerrank_automation

# HackerRank Automation Readme

## Author
- **Author:** Abhishek Yadav

## Description
This project provides a Python script for automating the process of logging into HackerRank, navigating to a Python coding challenge, uploading a solution code file, and submitting it for testing. This automation aims to save time and effort for users who frequently participate in HackerRank challenges.

## Version
- **Version:** 1.0

## Date
- **Date:** 14-Aug-2023

## Azure Ticket Link
- **Azure Ticket Link:** [Azure Ticket](https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3058)

## Prerequisites
Before running the script, make sure you have the following:
- Python 3.x installed on your system.
- Required Python packages: `dotenv`, `selenium`. You can install them using `pip`
- Chrome browser and the appropriate version of `chromedriver` for your Chrome browser installed.

## Usage
1. Clone this repository to your local machine or download the provided script.
2. Install the required packages as mentioned in the "Prerequisites" section.
3. Update the `.env` file with your HackerRank username and password:
   ```
   HACKERRANK_USERNAME=your_username
   HACKERRANK_PASSWORD=your_password
   ```
4. Modify the file path in the script to point to the correct location of the solution code file you want to upload:
   ```
   hidden_element.send_keys("/path/to/your/solution/file.py")
   ```
5. Run the script using the following command:
   ```
   python hackerrank_automation.py
   ```

## Script Details
The script `hackerrank_automation.py` performs the following actions:
1. Initializes a Chrome browser using the `webdriver` from Selenium.
2. Logs into HackerRank using the provided credentials.
3. Navigates to the Python coding challenges page.
4. Selects a specific Python coding challenge and opens it.
5. Uploads the solution code file for the selected challenge.
6. Submits the code for testing and displays a success message upon successful submission.

## Note
- This script is provided as-is and might need adjustments based on changes in the HackerRank website's structure or any other dependencies. It's recommended to review and modify the script accordingly if needed.

## Disclaimer
This project is for educational and automation purposes only. The author is not responsible for any unauthorized actions or misuse of this script. Use this script responsibly and only on HackerRank challenges you have the right to participate in.

Demo:
[<img src="https://i.ytimg.com/vi/Hc79sDi3f0U/maxresdefault.jpg" width="50%">](https://drive.google.com/file/d/1xgkQcxfQm-SAth0Wxv8UAGkD1YqC0elw/view?usp=drive_link)
