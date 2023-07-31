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