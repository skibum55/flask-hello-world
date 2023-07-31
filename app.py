import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola Mundo!'

 
@app.route('/db_test')
def testing(): 
    conn = psycopg2.connect("postgres://skuser:4X6aRfFuNCvi5dux1wCYTeFR2u5NFOQm@dpg-cj3u2sdiuie55pnqiub0-a/skflask")
    conn.close()
    return 'Database connection successful!'

@app.route('/db_create')
def creating(): 
    conn = psycopg2.connect("postgres://skuser:4X6aRfFuNCvi5dux1wCYTeFR2u5NFOQm@dpg-cj3u2sdiuie55pnqiub0-a/skflask")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table created successfully!'

@app.route('/db_insert')
def inserting(): 
    conn = psycopg2.connect("postgres://skuser:4X6aRfFuNCvi5dux1wCYTeFR2u5NFOQm@dpg-cj3u2sdiuie55pnqiub0-a/skflask")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball rows inserted successfully!'

@app.route('/db_select')
def selecting(): 
    conn = psycopg2.connect("postgres://skuser:4X6aRfFuNCvi5dux1wCYTeFR2u5NFOQm@dpg-cj3u2sdiuie55pnqiub0-a/skflask")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    response_string="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    conn.close()
    console.log(records)
    return response_string

@app.route('/db_drop')
def dropping(): 
    conn = psycopg2.connect("postgres://skuser:4X6aRfFuNCvi5dux1wCYTeFR2u5NFOQm@dpg-cj3u2sdiuie55pnqiub0-a/skflask")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table successfully dropped!'