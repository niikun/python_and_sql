import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("sample.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Execute the SELECT statement
cursor.execute("SELECT * FROM people")

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print the fetched rows
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
connection.close()
