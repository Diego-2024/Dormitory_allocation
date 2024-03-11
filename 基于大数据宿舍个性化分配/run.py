import time

import pandas as pd
from flask import Flask, render_template, request, flash, send_file
import pymysql
from sqlalchemy import create_engine
from 验证码 import *
from 聚类算法 import JuLei
from 对数据进行标签分类 import *
from 对数据进行二次标签 import *

app = Flask(__name__)
app.secret_key = 'fsh12345678'


@app.route('/')
def login():
    image, code = get_verify_code()
    image_path = 'static/images/yzm.png'
    image.save(image_path)
    session['image'] = code
    return render_template('login.html', image=image, code=code)


@app.route('/get_code_image')
def get_code_image():
    image, code = get_verify_code()
    image_path = 'static/images/yzm1.png'
    image.save(image_path)
    session['image'] = code
    return send_file(image_path, mimetype='image/png'), 200


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        stu_id = int(request.form['stu_id'])
        session['stu_id'] = stu_id
        checkcode = request.form['checkcode']

        if checkcode.lower() == session['image'].lower():
            if session['stu_id'] == 32115200039:
                return render_template('select_admin.html')
            else:
                return render_template('select_stu.html')
        else:
            flash('验证码不正确(可点击图像刷新验证码)', 'danger')
    return render_template('login.html')


@app.route('/select_admin')
def select_admin():
    return render_template('select_admin.html')


@app.route('/habit')
def habit():
    return render_template('habit.html')


@app.route('/get_value', methods=['GET', 'POST'])
def get_value():
    if request.method == 'POST':
        db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8', port=3306)
        cur = db.cursor()
        try:
            stu_id = request.form['stu_id']
            name = request.form['name']
            sex = request.form['sex']
            if sex == '男':
                value = 'value_1'
            else:
                value = 'value_2'
            session['value'] = value
            sql1 = " INSERT INTO {} (id, name, sex) VALUES ({}, '{}', '{}')".format(value, stu_id, name, sex)
            cur.execute(sql1)
            sql2 = " INSERT INTO value (id, name, sex) VALUES ({}, '{}', '{}')".format(stu_id, name, sex)
            cur.execute(sql2)
            for i in range(12):
                num = (int(request.form['hobby{}'.format(i + 3)]))
                sql3 = "update {} set habit{} = {} ".format(value, i + 3, num)
                cur.execute(sql3)
            db.commit()
        except:
            flash('填写表单时发生错误,请联系管理员', 'danger')
            return render_template('habit.html')
        cur.close()
        db.close()
    return render_template('out_stu.html')


@app.route('/distribution', methods=['GET', 'POST'])
def distribution():
    if request.method == 'POST':
        sex_1 = '男'
        sex_2 = '女'
        num1 = int(request.form['number1'])
        num2 = int(request.form['number2'])
        num3 = int(request.form['number3'])
        value = int(request.form['select'])
        if value == 1:
            FenLei_1(sex_1)
            FenLei_2(num1, num2, num3, sex_1)
        elif value == 2:
            FenLei_1(sex_2)
            FenLei_2(num1, num2, num3, sex_2)
        else:
            FenLei_1(sex_1)
            FenLei_2(num1, num2, num3, sex_1)
            FenLei_1(sex_2)
            FenLei_2(num1, num2, num3, sex_2)
    return render_template('out_admin.html')


@app.route('/display_stu')
def display_stu():
    db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8', port=3306)
    cur = db.cursor()
    stu_id = session['stu_id']
    sql = "select sex from value where id = {}".format(stu_id)
    cur.execute(sql)
    sex = cur.fetchall()[0][0]
    session['sex'] = sex
    if sex == '男':
        value = 'value_1'
    else:
        value = 'value_2'
    sql1 = "select max(tab) from {}".format(value)
    cur.execute(sql1)
    stu_id = session['stu_id']
    sql2 = ("select id,name,building,dormitory,bed from {} where tab2 in "
            "(select tab2 from {} where id = {})").format(value, value, stu_id)
    cur.execute(sql2)
    datas = cur.fetchall()
    cur.close()
    db.close()
    return render_template('display_stu.html', datas=datas)


@app.route('/display_admin', methods=['GET', 'POST'])
def display_admin():
    if request.method == 'POST':
        db = pymysql.connect(host='localhost', user='root', database='big_data_homework', charset='utf8', port=3306)
        cur = db.cursor()
        num = int(request.form['sex'])
        if num == 1:
            value = 'value_1'
            sex = '男'
        else:
            value = 'value_2'
            sex = '女'
        sql1 = "select id,name,building,dormitory,bed from {} order by building asc, dormitory asc".format(value)
        cur.execute(sql1)
        datas = cur.fetchall()
        cur.close()
        db.close()
        return render_template('display_admin.html', datas=datas, sex=sex)
    return render_template('select_admin.html')


if __name__ == '__main__':
    app.run(debug=True)
