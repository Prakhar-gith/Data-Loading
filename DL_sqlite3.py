"""
Code Author: Prakhar

This script demonstrates how to load a CSV file into an SQLite database using Pandas and SQLite3.
It creates a table in the database if it does not already exist, then inserts the data from the CSV file into this table.
Finally, it retrieves and prints the first 8 rows from the table.
"""

import sqlite3
import pandas as pd

# Establishing a connection to the SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()  # Creating a cursor object to interact with the database

# Loading data from a CSV file into a DataFrame
df_csv = pd.read_csv('MOCK_DATA.csv')  # Read the CSV file into a DataFrame

# Creating a table in the database if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mock_data_csv (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        gender TEXT,
        ip_address TEXT
    )
''')
conn.commit()  # Committing the table creation to the database

# Inserting the data from the DataFrame into the SQLite table
df_csv.to_sql('mock_data_csv', conn, if_exists='replace', index=False)  # Replace the table if it already exists

# Querying the first 8 rows from the table to verify the data was inserted correctly
cursor.execute('SELECT * FROM mock_data_csv LIMIT 8')  # Execute SQL query to select 8 rows
rows = cursor.fetchall()  # Fetch all results from the query
for row in rows:
    print(row)  # Print each row

# Closing the connection to the database
conn.close()  # Properly close the database connection
