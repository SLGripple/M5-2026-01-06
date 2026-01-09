import pandas as pd
import os

# Define Base and Data Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

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
    # Strip any quotes from dates
    df[col] = df[col].astype(str).str.replace('"', "", regex=True)

    try:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')
    except Exception as e:
        print(f"Error while converting column {col} to datetime: {e}")

    # Identify rows with invalid dates
    error_flag = df[col].isna()  
    # Move invalid rows to date_errors - Future feature
    df_errors = df[error_flag].copy()
    # Keep only valid rows in df
    df_clean = df[~error_flag].copy()
    # Reset index for the cleaned DataFrame
    df_clean.reset_index(drop=True, inplace=True)
    df_errors.reset_index(drop=True, inplace=True)

    return df_clean,df_errors

def enrich_dateDuration(colA, colB, df):
    #Force to datetime for robustness
    df[colA] = pd.to_datetime(df[colA], dayfirst=True, errors='coerce')
    df[colB] = pd.to_datetime(df[colB], dayfirst=True, errors='coerce')
    #Calculate date difference in days
    df['date_delta'] = (df[colB]-df[colA]).dt.days
    #Conditional Filtering to be able to gauge erroneous loans.
    df['valid_loan_flag'] = df['date_delta'] >= 0
    return df

# ----------------------------- 
# # Cleaning Pipelines 
# # -----------------------------
def clean_book_data(df, date_columns, metrics):
    metrics["initial_rows"] = len(df) 
    df = duplicateCleaner(df) 
    metrics["after_duplicates"] = len(df) 
    df = naCleaner(df) 
    metrics["after_na"] = len(df) 
    all_errors = [] 
    for col in date_columns:
        df, errors = dateCleaner(col, df)
        metrics["date_errors"][col] = len(errors) 
        all_errors.append(errors) 
        date_errors = pd.concat(all_errors, ignore_index=True) 
        metrics["final_rows"] = len(df) 
        return df, date_errors 

def clean_customer_data(df): 
    df = duplicateCleaner(df) 
    df = naCleaner(df) 
    return df

# Metrics Building Function
def build_metrics_df(metrics):    
    row = {
    "initial_rows": metrics["initial_rows"],
    "after_duplicates": metrics["after_duplicates"],
    "after_na": metrics["after_na"],
    "final_rows": metrics["final_rows"]
    }
    for col, count in metrics["date_errors"].items():
        row[f"errors_{col}"] = count
    return pd.DataFrame([row])

# CSV Writer 

def write_csv(df, path, label):
     df.to_csv(path, index=False) 
     print(f"{label} written to {path}")

# Main execution
if __name__ == '__main__':
    print('**************** Starting Clean ****************')
    
    metrics = {
    "initial_rows": 0,
    "after_duplicates": 0,
    "after_na": 0,
    "date_errors": {},
    "final_rows": 0
    }

    # Paths
    books_path = os.path.join("data","03_Library Systembook.csv")
    customers_path = os.path.join("data","03_Library SystemCustomers.csv")
    date_columns = ['Book checkout', 'Book Returned']

    # Load Data
    books_df = fileLoader(books_path)
    customers_df = fileLoader(customers_path)

    # Clean Books
    books_df, date_errors = clean_book_data(books_df, date_columns, metrics)
    books_df = enrich_dateDuration("Book checkout", "Book Returned", books_df)
    # Clean Customers
    customers_df = clean_customer_data(customers_df)

    # Build Metrics DataFrame
    metrics_df = build_metrics_df(metrics)

    # Output Paths 
    books_output_path = os.path.join(DATA_DIR, "03_Library Systembook_cleaned.csv")
    customers_output_path = os.path.join(DATA_DIR, "03_Library SystemCustomers_cleaned.csv")
    errors_output_path = os.path.join(DATA_DIR, "03_Library Errors.csv")
    metrics_output_path = os.path.join(DATA_DIR, "03_Cleaning Metrics.csv")

    # Write Outputs
    write_csv(books_df, books_output_path, "Cleaned Books Data")
    write_csv(customers_df, customers_output_path, "Cleaned Customers Data")
    write_csv(date_errors, errors_output_path, "Date Errors Data")
    write_csv(metrics_df, metrics_output_path, "Cleaning Metrics")
    
    print('**************** DATA CLEANED ****************')

