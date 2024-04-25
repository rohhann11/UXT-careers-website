#from sqlalchemy import create_engine, text
import os
#ssl_args = {'ssl': {'ca': 'C:/Users/rohan/Downloads/singlestore_bundle.pem'}}
#engine = create_engine(
#  "mysql+pymysql://vamshi-1eaa2:6kAfL6gc4d1R6BrZz6ExvWeNDNoy4C3e@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/ database_08ae2?charset=utf8mb4",
#  connect_args=ssl_args)
#with engine.connect() as conn:
#  result = conn.execute(text("select * from uxt"))
# print(result.fetchall())


#from sqlalchemy import create_engine, text

#ssl_args = {'ssl': {'ca': 'C:/Users/rohan/Downloads/singlestore_bundle.pem'}}

#engine = create_engine(
 #   "mysql+pymysql://vamshi-1eaa2:6kAfL6gc4d1R6BrZz6ExvWeNDNoy4C3e@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/ database_08ae2?charset=utf8mb4",
  #  connect_args=ssl_args)

#with engine.connect() as conn:
 # result = conn.execute(text("SELECT * FROM uxt"))
  #print(result.fetchall())


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)