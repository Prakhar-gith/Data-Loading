"""
Code Author: Prakhar

This script demonstrates how to load a CSV file into a MongoDB database using Pandas and PyMongo.
It reads data from a CSV file into a DataFrame, connects to MongoDB, and inserts the data into a collection.
Finally, it retrieves and prints the first 5 records from the collection to verify the data upload.
"""

import pymongo
import pandas as pd

# Load data from CSV into a DataFrame
df_csv = pd.read_csv('MOCK_DATA.csv')  # Read the CSV file into a Pandas DataFrame

# Establish a connection to MongoDB
client = pymongo.MongoClient("localhost:27017")  # Connect to MongoDB server on the default port
db = client['my_database']  # Create or connect to a database named 'my_database'
collection = db['mock_data']  # Create or connect to a collection named 'mock_data'

# Convert DataFrame to a list of dictionaries for MongoDB insertion
data = df_csv.to_dict(orient='records')  # Convert DataFrame rows to dictionaries

# Insert the data into the MongoDB collection
collection.insert_many(data)  # Insert all records into the collection

# Verify the data upload by retrieving and printing the first 5 records
for record in collection.find().limit(5):  # Find and limit the results to 5 records
    print(record)  # Print each record to check if the data was inserted correctly

# Close the MongoDB connection
client.close()  # Close the connection to the MongoDB server