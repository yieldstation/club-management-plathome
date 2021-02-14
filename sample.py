from flask import Flask, render_template
from flask import request
import psycopg2
app = Flask(__name__)

@app.route("/")
def hello_world():
    

    # connect postgreSQL
    users = 'postgres' # initial user
    dbnames = 'test'
    passwords = 'postgres'
    conn = psycopg2.connect(host="localhost",port=5432,user=users,database=dbnames,password=passwords)

    # excexute sql
    cur = conn.cursor()
    cur.execute('SELECT * FROM mst_member;')
    members = cur.fetchall()

    #output result
    print(members)

    cur.close()
    conn.close()
    
    return render_template("sample.html",members=members)

@app.route("/member", methods=["POST"])
def add_member():
    name = request.form["member_name"]
    dept_num = request.form["department"]
    users = 'postgres' # initial user
    dbnames = 'test'
    passwords = 'postgres'
    with psycopg2.connect(host="localhost",port=5432,user=users,database=dbnames,password=passwords) as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO mst_member (name,number,department) VALUES (%s,%s,%s)', (name,2,dept_num))
        conn.commit()
    return "add"

app.run(debug=True)