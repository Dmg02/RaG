import pandas as pd
import re

# Function to clean whitespace
def clean_whitespace(text):
    return re.sub(r'\s+', ' ', str(text)).strip()

# Read the Excel file
df = pd.read_excel('/Users/dmg/Desktop/coding /RaG/data/jurisdb_cleanned.xlsx', engine='openpyxl')

# Apply the cleaning function to the desired column
df['Texto'] = df['Texto'].apply(clean_whitespace)

# Save the cleaned dataframe back to an Excel file
df.to_excel('path_to_cleaned_file.xlsx', index=False, engine='openpyxl')
