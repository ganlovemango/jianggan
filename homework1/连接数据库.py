import pymysql

import settings

conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = """
create table  if not exists user(uid int primary key auto_increment,username varchar(30) not null unique,usertype enum("0","1") default "0",password char(48) not null, regtime datetime default now(), email varchar(40));
"""

username = input("请输入用户名：")
sql1 = "select username from user"
cursor.execute(sql1)
usernames = cursor.fetchall()
if usernames:
    for user in usernames:
        if username == user["username"]:
            print("用户名重复")

        if not username or len(username) < 2:
            print("用户名有误")


    password = input("请输入密码：")
    email = input("请输入邮箱：")
    user_type = input("请选择用户类型01：")

cursor.close()
conn.close()