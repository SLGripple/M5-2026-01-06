## Docker Dependencies are installed via requirements.txt'

import pandas as pd
import os

# Function to output dataframe that can be manipulated via a filepath
def fileLoader(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File Not Found: {filepath}")  
    return pd.read_csv(filepath) 

# Duplicate Dropping Function
def duplicateCleaner(df):
    return df.drop_duplicates().reset_index(drop=True)

# NA handler - future scope can handle errors more elegantly. 
def naCleaner(df):
    return df.dropna().reset_index(drop=True)

# Turning date columns into datetime
def dateCleaner(col, df):
    #date_errors = pd.DataFrame(columns=df.columns)  # Store rows with date errors

    # Strip any quotes from dates
    df[col] = df[col].str.replace('"', "", regex=True)

    try:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')

    except Exception as e:
        print(f"Error while converting column {col} to datetime: {e}")

    # Identify rows with invalid dates
    error_flag = df[col].isna()
        
    # Move invalid rows to date_errors - Future feature
    #date_errors = df[error_flag]
        
    # Keep only valid rows in df
    df = df[~error_flag].copy()

    # Reset index for the cleaned DataFrame
    df.reset_index(drop=True, inplace=True)

    return df

def enrich_dateDuration(colA, colB, df):
    """
    Takes the two datetime input column names and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note:
    colB>colA
    """
    df['date_delta'] = (df[colB]-df[colA]).dt.days

    #Conditional Filtering to be able to gauge eroneous loans.
    df.loc[df['date_delta'] < 0, 'valid_loan_flag'] = False
    df.loc[df['date_delta'] >= 0, 'valid_loan_flag'] = True

    return df

if __name__ == '__main__':
    print('**************** Starting Clean ****************')

    # Paths
    filepath_input = 'data/03_Library Systembook.csv'
    date_columns = ['Book checkout', 'Book Returned']
    date_errors = None

    data = fileLoader(filepath=filepath_input)

    # Drop duplicates & NAs
    data = duplicateCleaner(data)
    data = naCleaner(data)

    # Converting date columns into datetime
    for col in date_columns:
        data = dateCleaner(col, data)
    
    # Enriching the dataset
    data = enrich_dateDuration(df=data, colA='Book Returned', colB='Book checkout')

    #data.to_csv('cleaned_file.csv')
    print(data)

    #Cleaning the customer file
    filepath_input_2 = 'data/03_Library SystemCustomers.csv'

    data2 = fileLoader(filepath=filepath_input_2)

    # Drop duplicates & NAs
    data2 = duplicateCleaner(data2)
    data2 = naCleaner(data2)

    print(data2)
    print('**************** DATA CLEANED ****************')
    
    # Assume 'data' is your cleaned pandas DataFrame
    print(f"Writing to Cleaned CSV")
    output_path = "/app/data/03_Library Systembook_cleaned.csv"
    output_path2 = "/app/data/03_Library SystemCustomers_cleaned.csv"
    data.to_csv(output_path, index=False)
    data2.to_csv(output_path2, index=False)
    print(f"Cleaned CSV written to {output_path}")
    print(f"Cleaned CSV written to {output_path2}")
    
    