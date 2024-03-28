import mysql
from mysql.connector import connect
from mysql.connector import errorcode
from configparser import ConfigParser

class DB():
    def __init__(self):
        try:
            db_config=DB.read_db_config_file()
            self.cnx=connect(database=db_config['database'],username=db_config['user'],
                             password=db_config['password'],host=db_config['host'],port=db_config['port'])
            mycursor = self.cnx.cursor()
            # uid = db_config['user']
            # old_pwd = db_config['password']
            # new_pwd = 'root123'
            # sql = "ALTER USER 'root'@'127.0.0.1'  IDENTIFIED WITH 'NiRa7712*' BY 'root123';"
            # mycursor.execute(sql)
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
    def read_db_config_file(filename='./config.ini', section='mysql'):
        parser=ConfigParser()
        parser.read(filename)

        config_db= {}
        if parser.has_section(section):
            items=parser.items(section)
            for item in items:
                config_db[item[0]]=item[1]
        else:
            raise Exception(f'{section} not found in {filename}')
        return config_db

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
    db=DB()
    myresult=db.authenticate('maria@abv.bg')
    if myresult==[]:
        print("Wrong username try again")
    else:
        print('Successfully loged in')

