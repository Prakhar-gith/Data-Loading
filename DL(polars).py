"""
Code Author: Prakhar
Reference src: polars documentation

This script is designed to load datasets from different file formats like CSV, Excel (XLSX), and JSON using Polars library.
It handles loading of the data and performs basic exploration tasks. It raises an error if the file format is unsupported.
"""

import polars as pl
import os

# Function to load data based on file extension
def load_data(file_path):
    """ 
    Loads data from the specified file path and returns it as a DataFrame.
    It supports CSV, XLSX, and JSON file formats. Unsupported formats will trigger a ValueError.
    """
    
    # Get the file extension and convert it to lowercase
    file_extension = os.path.splitext(file_path)[1].lower()  

    # Loading CSV files
    if file_extension == '.csv':    
        print("Loading CSV file...")  
        df = pl.read_csv(file_path)   # Using Polars to read CSV file

    # Loading Excel files
    elif file_extension == '.xlsx':  
        print("Loading Excel file...")  
        df = pl.read_excel(file_path)   # Polars to read Excel file

    # Loading JSON files
    elif file_extension == '.json':  
        print("Loading JSON file...")   
        df = pl.read_json(file_path)    # Polars for reading JSON

    # Raise an error for unsupported file formats
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")  

    return df  # Return the loaded dataframe

# Example usage
# file_path = 'MOCK_DATA.csv'  # Commented out - example CSV file
file_path = 'MOCK_DATA.json'  # JSON file from mockaroo

# Try block to load the data and handle errors
try:
    # Load the DataFrame using the function
    df = load_data(file_path)
    print("Data loaded successfully!")  # Confirmation of successful loading
    print(df.head())  # Shows first 5 rows of the DataFrame

    # Uncomment to see more rows or the last rows
    # df.head(10)  # First 10 rows 
    # df.tail(7)   # Last 7 rows

    '''
    Some other useful methods with Polars DataFrames:
    -------------------------------------------------
    - df.describe() : Summary statistics of the dataset
    - df.columns : List of column labels
    - df.shape : Returns the shape (rows, columns) of the DataFrame
    - df.dtypes : Data types of each column
    - df.null_count() : Shows number of null values in each column
    - df.drop_nulls() : Remove rows with null values
    - df.fill_null() : Replace null values with specified value
    - df.unique() : Remove duplicate rows
    - df.value_counts() : Frequency of unique values in a column
    - df.groupby() : Group data by a column for aggregation
    - df.sort() : Sort the DataFrame by a particular column
    - df.write_csv() : Export DataFrame to CSV
    - df.write_excel() : Export DataFrame to Excel
    - df.write_json() : Export DataFrame to JSON
    '''

except Exception as e:
    # Catching any error during the loading process and displaying it
    print(f"An error occurred: {e}")
