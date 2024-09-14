"""
Code Author: Prakhar Swarnkar

This script is designed to load datasets from various file formats such as CSV, Excel (XLSX), and JSON.
It utilizes the pandas library to load the data and supports basic operations like displaying and exploring the dataset.
If an unsupported file format is given, it raises an error.
"""

import pandas as pd
import os

# Function to load data based on file extension
def load_data(file_path):
    """ 
    Load data from a given file path and return it as a DataFrame. The function handles CSV, XLSX, and JSON formats.
    If the format is unsupported, it throws a ValueError. 
    """
    
    # Splitting the filename to get its extension and converting it to lowercase
    file_extension = os.path.splitext(file_path)[1].lower()  

    # if the file is a CSV file, load it
    if file_extension == '.csv':    
        print("Loading CSV file...")  # Printing status
        df = pd.read_csv(file_path)   # Reading CSV file using pandas

    # if the file is an Excel (XLSX) file
    elif file_extension == '.xlsx':  
        print("Loading Excel file...")  # Notifying Excel file is being loaded
        df = pd.read_excel(file_path)   # Reading Excel file

    # if the file is a JSON file
    elif file_extension == '.json':  
        print("Loading JSON file...")   # Loading JSON file
        df = pd.read_json(file_path)    # pandas function to read JSON file

    else:
        # If the file format is not one of the above, raise an error
        raise ValueError(f"Unsupported file format: {file_extension}")

    return df  # return the loaded dataframe

# Example usage
file_path = 'MOCK_DATA.csv'  # Just an example file, a CSV from mockaroo
# file_path = 'MOCK_DATA.json'  # Can switch to JSON file as needed

# Try to load the data and handle potential errors
try:
    # Loading the DataFrame using the load_data function
    df = load_data(file_path)
    print("Data loaded successfully!")  # Success message when data is loaded
    print(df.head())  # Displaying the first 5 rows of the DataFrame

    # The head function shows first 5 rows by default
    # Uncomment below lines to see other parts of the dataset
    # print(df.head(10))  # First 10 rows 
    # print(df.tail(7))  # Last 7 rows

    ''' 
    If the DataFrame is large, pandas only shows first 5 rows and last 5 rows.
    To display more or less, specify the number in df.head() or df.tail()
    '''
    
    '''
    Some useful DataFrame methods:
    ------------------------------
    - df.info() : Summarizes the DataFrame (column types, non-null counts)
    - df.describe() : Descriptive stats for numeric columns (mean, std, etc.)
    - df.columns : Returns the column names
    - df.shape : Returns the dimensions (rows, columns)
    - df.dtypes : Shows the data types for each column
    - df.isnull().sum() : Summarizes missing data by column
    - df.dropna() : Removes rows with missing values
    - df.fillna() : Replaces missing values
    - df.drop_duplicates() : Removes duplicate rows
    - df.value_counts() : Counts unique values in a column
    - df.groupby() : Groups data based on a column(s)
    - df.sort_values() : Sorts data by specified column
    - df.to_csv() : Exports DataFrame to CSV
    - df.to_excel() : Exports DataFrame to Excel
    - df.to_json() : Exports DataFrame to JSON
    '''

    # Checking system's maximum row support 
    print("Maximum rows supported by system: ", pd.options.display.max_rows)

except Exception as e:
    # In case something went wrong, print the error
    print(f"An error occurred: {e}")
