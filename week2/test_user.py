import sqlite3

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()

# create_table = "CREATE TABLE user(id INTEGER primary key,name TEXT,email TEXT)"

# cursor.execute(create_table)

insert_query = "INSERT INTO user(name,email) VALUES(?,?)"
values = [
  ('John', 'john@email.com'),
  ('Mary', 'mary@email.com'), 
  ('Robert', 'robert@email.com'),
  ('Laura', 'laura@email.com')]

for name,email in values:
    cursor.execute(insert_query,(name,email))

connection.commit()