import sqlite3


conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   email TEXT,
   password TEXT);
""")
conn.commit()

a = 1
while a != 0:
    a = input()
    if a == 'a':
        passw = input()
        lname = input()
        fname = input()
        email = input()

        dann = (fname, lname, email, passw)

        cur.execute("INSERT INTO users(fname, lname, email, password) VALUES(?, ?, ?, ?);", dann)
        conn.commit()
    elif a == 'b':
        email = input()
        passw = input()

        cur.execute("SELECT * FROM users WHERE password = ? AND email = ?;", (passw, email))
        all_results = cur.fetchall()
        print(all_results)