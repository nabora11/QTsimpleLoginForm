import mysql
from mysql.connector import connect
from mysql.connector import errorcode

class DB():
    def __init__(self,database_,username_,host_):
        try:
            self.cnx=connect(database=database_,username=username_,password='NiRa7712*',host=host_,port=3306)
            mycursor = self.cnx.cursor()
            mycursor.execute("Show tables from test like 'users';")
            myresult = mycursor.fetchall()
            if myresult==[]:

                q=f"""CREATE TABLE users(
                ID int AUTO_INCREMENT,
                FirstName varchar(255),
                UserName varchar(255) UNIQUE,
                Password varchar(255),
                PRIMARY KEY (ID)
                );"""
                mycursor.execute(q)
                mycursor.execute(""" INSERT INTO users(FirstName,UserName,Password)
                VALUES('Maria','maria@abv.bg','maria123'),
                ('Ivan','ivan@abv.bg','ivan123'),
                ('Petkan','petkan@abv.bg','petkan123');
                """)
                self.cnx.commit()
            mycursor.execute('SELECT * FROM users')
            myresult = mycursor.fetchall()
            print(myresult)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def authenticate(self,mail,pass_):
        mycursor=self.cnx.cursor()
        mycursor.execute('SELECT * FROM users WHERE UserName=%s',(mail,))
        myresult=mycursor.fetchall()
        print(myresult)
        if myresult!= [] and pass_ in myresult[0]:
            return True
        else:
            return False
if __name__ == '__main__':
    db=DB('test','root','localhost')
    myresult=db.authenticate('maria@abv.bg')
    if myresult==[]:
        print("Wrong username try again")
    else:
        print('Successfully loged in')

