import pandas as pd
import pymysql

db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8', port=3306)
cur = db.cursor()

Data = pd.read_excel('模拟宿舍分配(男).xlsx')
data = Data.iloc[:, 0:].values
for i in range(len(data)):
    value = data[i]
    stu_id = value[0]
    name = value[1]
    sex = value[2]
    sql = " INSERT INTO value_1 (id, name, sex) VALUES ({}, '{}', '{}')".format(stu_id, name, sex)
    cur.execute(sql)
    for j in range(12):
        sql1 = "update value_1 set habit{} = {} where id = {} ".format(j + 3, value[j+3], stu_id)
        cur.execute(sql1)


db.commit()
cur.close()
db.close()
