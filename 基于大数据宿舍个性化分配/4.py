import pymysql

db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8',
                     port=3306)
cur = db.cursor()
sql = "select id from value"
cur.execute(sql)
ID = 32115101
print(cur.fetchall()[0][0])
print(ID in cur.fetchall())



cur.close()
db.close()