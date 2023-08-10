import re
import openpyxl

def extract_emails_from_content(content):
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', content)
    return emails

# Load the downloaded content from a file
with open("C:\\Users\\ASUS\\Downloads\\LeaderboardDataCampLearn.html", "r", encoding="utf-8") as file:
    website_content = file.read()

email_list = extract_emails_from_content(website_content)

if email_list:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Email List"
    
    for idx, email in enumerate(email_list, start=1):
        ws.cell(row=idx, column=1, value=email)
    
    excel_filename = "extracted_emails.xlsx"
    wb.save(excel_filename)
    
    print(f"Extracted email addresses saved to '{excel_filename}'.")
else:
    print("No email addresses found in the downloaded content.")
