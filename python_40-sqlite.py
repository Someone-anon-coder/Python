import sqlite3

conn = sqlite3.connect("Database/example.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

conn.commit()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Someone", 100))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Someone Else", 84))

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("UPDATE users SET age = ? WHERE name = ?", (101, "Someone"))
conn.commit()

cursor.execute("DELETE FROM users WHERE name = ?", ("Someone Else",))
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "test_user",
    password = "my_password",
    database = "example_db",
)

cursor = conn.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS example_db")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
''')

cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Someone', 100))
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ('Someone Else', 84))

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("UPDATE users SET age = %s WHERE name = %s", (101, "Someone"))
conn.commit()

cursor.execute("DELETE FROM users WHERE name = %s", ("Someone Else",))
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()