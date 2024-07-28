import sqlite3

# Connect to the database
conn = sqlite3.connect('sample.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM user")

# Fetch all results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
conn.close()
