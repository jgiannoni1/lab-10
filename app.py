from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from James Giannoni in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_postgres_8wzi_user:B4SiP5YbCiXEwIth7pR2afsnqOgEqFnD@dpg-cvm7kbngi27c73ad8af0-a/lab_10_postgres_8wzi")
    conn.close()
    return "Database connection successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("your_db_url_here")
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
    return "Basketball table created"
