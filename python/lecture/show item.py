from db import con
cur = con.cursor()
cur.execute("SELECT * FROM v_item")
data = cur.fetchall()
print(data)