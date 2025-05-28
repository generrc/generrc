from flask import Flask, request, render_template
import sqlite3

DB_FILE = 'weather_database.db'


def init_db():
    cn = sqlite3.connect(DB_FILE)
    c = cn.cursor()
    c.execute()
    cn.commit()
    cn.close()


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    cn = sqlite3.connect(DB_FILE)
    c = cn.cursor()
    c.execute()
    ccn.commit()
    cn.close()
    return {'status': 'ok'}

@app.route('/')
def index():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT datetime, temperature, air_pressure, humidity FROM weather ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)