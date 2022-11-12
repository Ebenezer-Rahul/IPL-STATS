from flask import Flask, render_template
#from flask_mysqldb import MySQL
import mariadb
from datetime import datetime

app = Flask(__name__)

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='we5great',
         database='sys')
cur = connection.cursor()



@app.route('/')
def index():

    cur.execute('SELECT * FROM Team ORDER BY pos');
    print(cur)
    teams = cur.fetchall()
    connection.commit()
    for team in teams:
        print(team)
    return render_template("home.html", teams=teams, i = 0);

@app.route('/team/t_id=<int:t_id>')
def team(t_id):
    cur.execute(f'SELECT * FROM Player WHERE Player.team_id={t_id} ORDER BY runs DESC ')
    players = cur.fetchall();

    return render_template("player.html", players=players);



@app.route('/matches')
def matches():
    cur.execute('SELECT * FROM Match_ ORDER BY time DESC')
    matches = cur.fetchall()
    connection.commit()
    print(matches[0])
    return render_template("matches.html", matches=matches, abs=abs);

@app.route('/match/mid=<int:m_id>')
def match(m_id):

    return render_template("match.html");

@app.route('/players')
def players():
    return render_template("home.html");

@app.route('/player/pid=<int:pid>')
def player(pid):
    print(pid)
    return render_template("home.html");


@app.route('/deliveries/mid=<int:m_id>')
def deliveries(m_id):
    cur.execute(f'SELECT * FROM Delivery WHERE match_id={m_id}')
    deliveries = cur.fetchall()
    for delivery in deliveries :
        print(delivery)
    return render_template("home.html");



if __name__ == ' __main__':
    app.run(debug=True, port=80)
