import mysql.connector

def register_user():
    print("#### Registration####")
    username=input("Enter your name")
    password=input("Enter password")

    try:
        db=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="nisha123",
        database="management",
        auth_plugin='mysql_native_password'
    )
        cursor=db.cursor()
        cursor.execute("use management")
       # cursor.execute("create table user11(username varchar(40), password varchar(40))")
        q1="insert into user11(username,password) values(%s,%s)"
        cursor.execute(q1,(username,password))

        db.commit()

        q2="select * from user11"
        cursor.execute(q2)
        db1=cursor.fetchall()
        if db1:
            for i in db1:
                print(i)

        print("Registration done......")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        # Handle the error or log it as needed

    finally:
        # Close the database connection in the 'finally' block
        if 'db' in locals() and db.is_connected():
            db.close()
            print("Connection closed")

register_user()