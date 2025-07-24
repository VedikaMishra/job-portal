import sqlite3

conn = sqlite3.connect("job_portol.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in job_portol.db:")
for table in tables:
    print(table[0])
