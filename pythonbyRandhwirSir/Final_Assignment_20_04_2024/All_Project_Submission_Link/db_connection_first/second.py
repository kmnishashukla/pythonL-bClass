import mysql.connector
try:
    mydb1=mysql.connector.connect(
        host="localhost",
        user ="root",
        passwd="nisha123",
        database="management",
        auth_plugin="mysql_native_password"
    )
    cursor=mydb1.cursor()
    q1="show databases"
    cursor.execute(q1)
    db=cursor.fetchall()
    if db:
        for i in db:
            print(i)

    if mydb1.is_connected():
        print("connected to the MYSQL database")
except mysql.connector.Error as err:
    print(f"Error {err}")
finally:
      if 'mydb1' in locals() and mydb1.is_connected():
          mydb1.close()
          print("Connetion closed")                    

