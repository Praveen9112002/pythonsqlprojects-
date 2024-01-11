import sqlite3
c = sqlite3.connect("clgmanagement.db")
curser = c.cursor()

curser.execute("""CREATE TABLE data
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               department TEXT,
               roll_number INTEGER)""")
curser.execute("INSERT INTO data (name,department,roll_number) VALUES (?,?,?)",('Arisha','CH',6))
curser.execute("INSERT INTO data (name,department,roll_number) VALUES (?,?,?)",('Praveen','MT',34))
c.commit()

curser.execute("SELECT* FROM data")
rows=curser.fetchall()
for row in rows:
    print(row)
c.commit()
    