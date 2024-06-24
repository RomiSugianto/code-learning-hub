from db import con
cur = con.cursor()
cur.execute("SELECT * FROM penerimaan")
data = cur.fetchall()
print(data)