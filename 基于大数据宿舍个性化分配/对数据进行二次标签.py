import pandas as pd
import pymysql
from sqlalchemy import create_engine


def FenLei_2(number1, number2, number3, sex):
    db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8', port=3306)
    cur = db.cursor()
    if sex == '男':
        value = 'value_1'
    else:
        value = 'value_2'
    sql1 = "select id,tab from {} order by tab asc".format(value)
    cur.execute(sql1)
    Datas = cur.fetchall()
    tab = []
    tab2 = []
    for data in Datas:
        tab.append(data[1])
    t = 0
    x = 0
    y1 = 1
    y2 = 200
    z = 1
    X = []
    Y = []
    Z = []
    tab.append(data[1])
    for i in range(len(Datas)):
        X.append(x)
        tab2.append(t)
        Y.append(y2 + y1)
        Z.append(z)
        x = x + 1
        if Datas[i][1] != tab[i + 1]:
            t = t + 1
            y1 = y1 + 1
            x = 0
        if x == number1:
            t = t + 1
            y1 = y1 + 1
            x = 0
        if y1 == number2 + 1:
            y2 = y2 + 100
            y1 = 1
            x = 0
        if y2 == number3 * 100 + 100:
            z = z + 1
            y1 = 1
            y2 = 200
            x = 0

    for i in range(len(Datas)):
        sql1 = "UPDATE {} SET tab = {}, tab2 = {}, bed = {} , dormitory = {} , building = '{}' WHERE id = {}".format(
            value, Datas[i][1],
            tab2[i],
            X[i] + 1, Y[i], Z[i],
            Datas[i][0])

        cur.execute(sql1)

    db.commit()

    cur.close()
    db.close()
