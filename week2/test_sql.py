import sqlite3

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()

# create_table = "CREATE TABLE (id integer primary key ,name TEXT,surname TEXT)"

# cursor.execute(create_table)

datas = [("kawata","akimoto"),("kawata","ikuko"),("kawata","mayoko")]

insert_data = "INSERT INTO people (name,surname) VALUES(?,?)"

for key,value in datas:
    cursor.execute(insert_data,(key,value))

connection.commit