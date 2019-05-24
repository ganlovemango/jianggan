import hashlib

import pymysql

import settings

conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

username = input("请输入用户名：")
password = input("请输入密码：")
password = hashlib.sha1(password.encode('utf8')).hexdigest()
sql = "select username,password from user where username=%s and password=%s"
res = cursor.execute(sql, [username, password])

if res:
    print('登陆成功')


cursor.close()
conn.close()