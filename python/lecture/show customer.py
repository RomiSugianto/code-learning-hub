from db import con
cur = con.cursor()
cur.execute("SELECT * FROM customer")
data = cur.fetchall()
print(data)