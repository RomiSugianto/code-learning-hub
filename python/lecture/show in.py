from db import con
cur = con.cursor()
cur.execute("SELECT * FROM pengeluaran")
data = cur.fetchall()
print(data)