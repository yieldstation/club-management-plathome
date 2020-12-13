from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    import psycopg2

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

app.run()