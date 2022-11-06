from flask import Flask
#from flask_mysqldb import MySQL
import mariadb


app = Flask(__name__)

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='we5great',
         database='sys')
cur = connection.cursor()

cur.execute('INSERT INTO Student VALUES (28, "Eren yeager");')
connection.commit()

@app.route('/')
def index():
    return '<h1> Rahul the server is working for real<h1>'


if __name__ == ' __main__':
    app.run(debug=True, port=80)
