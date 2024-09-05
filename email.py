import pandas as pd
import re

# Load the Excel file with both sheets
file_path = "D:/Projects/TestFiles.xlsx"  # Change this to your actual file path
xls = pd.ExcelFile(file_path)

# Load both sheets into separate dataframes
df1 = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
df2 = pd.read_excel(xls, sheet_name=xls.sheet_names[1])

# Function to generate email addresses
def generate_email(name):
    # Remove special characters from the name (retain spaces and comma)
    name = re.sub(r"[^a-zA-Z\s,]", "", name)

