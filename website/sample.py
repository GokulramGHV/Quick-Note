import sqlite3;

conn = sqlite3.connect('website/database.db')
cur = conn.cursor()
notess = cur.execute("select data,date,id from note where user_id=1 order by date desc;")
l = []
for res in notess:
    l.append(res)

for n,d,i in l:
    print(n,d,i)
conn.commit()
conn.close()

