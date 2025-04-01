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
    conn = psycopg2.connect("postgresql://lab_10_postgres_8wzi_user:B4SiP5YbCiXEwIth7pR2afsnqOgEqFnD@dpg-cvm7kbngi27c73ad8af0-a/lab_10_postgres_8wzi")
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

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://lab_10_postgres_8wzi_user:B4SiP5YbCiXEwIth7pR2afsnqOgEqFnD@dpg-cvm7kbngi27c73ad8af0-a/lab_10_postgres_8wzi")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number) VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://lab_10_postgres_8wzi_user:B4SiP5YbCiXEwIth7pR2afsnqOgEqFnD@dpg-cvm7kbngi27c73ad8af0-a/lab_10_postgres_8wzi")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    conn.close()

    table = "<table border='1'>"
    for row in records:
        table += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    table += "</table>"
    return table

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect("postgresql://lab_10_postgres_8wzi_user:B4SiP5YbCiXEwIth7pR2afsnqOgEqFnD@dpg-cvm7kbngi27c73ad8af0-a/lab_10_postgres_8wzi")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Basketball;")
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"

