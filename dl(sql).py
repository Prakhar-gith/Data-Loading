import pyodbc

# Define connection parameters
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=your_server_name;'
    'DATABASE=your_database_name;'
    'UID=your_username;'
    'PWD=your_password;'
)

# Create a connection
conn = pyodbc.connect(conn_str)


import pandas as pd
import pyodbc

# Here I am using a sample DataFrame or simply we load the dataset
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Creating a connection (Replace with your actual connection string)
conn_str = 'DRIVER={SQL Server};SERVER=ymyServer;DATABASE=sample;UID=prakh;PWD=123456;'
conn = pyodbc.connect(conn_str)

# Creating a cursor object
cursor = conn.cursor()

# Create table SQL statement (for SQL Server)
create_table_sql = """1
CREATE TABLE my_table (
    name NVARCHAR(50),
    age INT
)
"""

# Execute the create table SQL statement
cursor.execute(create_table_sql)
conn.commit()

# Inserting the DataFrame into SQL table
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO my_table (name, age) VALUES (Sachin, 23)",
        row['name'], row['age']
    )
conn.commit()

# Verify the insertion
query = "SELECT * FROM my_table"
result_df = pd.read_sql(query, conn)

print(result_df)

# Close the connection
conn.close()