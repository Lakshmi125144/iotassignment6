#!/usr/bin/python3
import pymysql
conn = pymysql.connect(database="users",user="lakshmi",password="iotassignment6",host="localhost")
cur=conn.cursor()
#to store user data
name = input('Enter the name: ')
age = input('Enter the age: ')
city = input('Enter the city: ')
state= input('Enter the state: ')
data={'userName':name,'userAge':age, 'userCity':city,'userState':state}
print(data)
# Saving data to DB
cur.execute("INSERT INTO userdata (userName, userAge, userCity, userState) VALUES (%(userName)s,%(userAge)s,%(userCity)s,%(userState)s);",data)
conn.commit()
print("saved to db")
