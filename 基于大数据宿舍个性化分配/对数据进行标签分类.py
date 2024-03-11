import pandas as pd
import pymysql
from sqlalchemy import create_engine
from 聚类算法 import JuLei


def FenLei_1(sex):
    db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8', port=3306)
    cur = db.cursor()
    engine = create_engine('mysql+pymysql://root:@localhost:3306/big_data_homework')
    if sex == '男':
        value = 'value_1'
    else:
        value = 'value_2'
    Data = pd.read_sql_table(value, con=engine)
    data1 = Data.iloc[:, 3:15].values
    ID = Data.iloc[:, 0].values
    result = JuLei(data1)

    for i in range(len(result)):
        sql1 = "UPDATE {} SET tab = {} WHERE id = {}".format(value, result[i], ID[i])
        cur.execute(sql1)

    db.commit()

    cur.close()
    db.close()
