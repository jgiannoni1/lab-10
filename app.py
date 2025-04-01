from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from James Giannoni in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("https://lab-10-20z0.onrender.com")
    conn.close()
    return "Database connection successful"

