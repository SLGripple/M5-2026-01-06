"""
Library Data Cleaning Script
"""
import pandas as pd

def clean_text(text_series):
    """
    Apply multiple text replacements to a column.
    Add or modify replacements in the list below.
    """
    replacements = [
        ('"', ''),                          # Remove Quotes 
        ('32/05/2023', '31/05/2023'),       # Correct Date
        ('Of The Kind', 'Of The King')     # Correct Title      
    ]
    
    for old, new in replacements:
        text_series = text_series.str.replace(old, new, regex=False)
    
    return text_series

def days_on_loan(bookout,bookin):
    """
    Calculate the time the book was on loan
    """
    on_loan = (bookin - bookout).dt.days   
    return on_loan

def clean_library_data(csv_filename):
    """
    Main Function : accepts csv, returns cleaned dataframe
    """
    print(f"Reading Data from{csv_filename}...")
    df = pd.read_csv(csv_filename)
    
    print(f"Cleaning Data...")
    # drop empty rows and columns and useless records 
    df = df.dropna(how='all')
    df = df.dropna(axis=1, how = 'all')
    df = df.dropna(subset=['Customer ID'])
    # Convert ID to INT
    df['Id'] = df['Id'].astype(int) 
    df['Customer ID'] = df['Customer ID'].astype(int)
    # trim spaces & remove quotes
    df = df.apply(lambda x:x.str.strip().str.replace('"','',regex=False) if x.dtype == "object" else x)
    # Properly case the book titles
    df['Books'] = df['Books'].str.title()
    # convert Weeks to days
    df['Days allowed to borrow'] = df['Days allowed to borrow'].str.replace('2 weeks','14',regex=False) 
    #Convert to Datetime
    df['Book checkout'] = pd.to_datetime(df['Book checkout'],dayfirst=True)
    df['Book Returned'] = pd.to_datetime(df['Book Returned'],dayfirst=True)
    #Calculate Days on Loan
    df['Days On Loan'] = days_on_loan(df['Book checkout'], df['Book Returned'])

    print(f"\n✓ Data cleaned successfully!")
    print(f"  Final shape: {df.shape[0]} rows, {df.shape[1]} columns")
    
    return df


# Allow running as standalone script
if __name__ == '__main__':
    # Clean the data
    cleaned_df = clean_library_data('03_Library Systembook.csv')
    
    # Display results
    print("\nCleaned DataFrame:")
    print(cleaned_df.head(10))
    
    # Optionally save to CSV
    # cleaned_df.to_csv('cleaned_library_data.csv', index=False)
    # print("\n✓ Saved to cleaned_library_data.csv")




    