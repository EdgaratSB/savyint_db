import mysql.connector
config = {'user': 'user',
          'password': 'password',
          'host': '172.18.0.3',
          'database': 'db',
          'raise_on_warnings': True
          }
def connect():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users;")
    myresult = cursor.fetchall()
    for x in myresult:
        return x

def push(list):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    add_user = ("INSERT INTO users (username, first_name, last_name, email) VALUES (%(usern)s, %(fname)s, %(lname)s, %(emailad)s)")
    data_user = {"usern":list[0],
                 "fname":list[1],
                 "lname":list[2],
                 "emailad":list[3]
                 }
    cursor.execute(add_user, data_user)
    cnx.commit()
    return print("succes")

