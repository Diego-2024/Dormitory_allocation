import pymysql

db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8', port=3306)
cur = db.cursor()


ID = 32115200039
sql = ("select id,name from value where tab in "
       "(select tab from value where id = {})").format(ID)
cur.execute(sql)
datas = cur.fetchall()

for data in datas:
    print(data[0])
print(len(datas))




cur.close()
db.close()