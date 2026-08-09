from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)
DB = "complaints.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            complaint_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            year TEXT NOT NULL,
            department TEXT NOT NULL,
            complaint_about TEXT NOT NULL,
            details TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def generate_id():
    conn = sqlite3.connect(DB)
    while True:
        complaint_id = random.randint(10000, 99999)
        exists = conn.execute(
            "SELECT complaint_id FROM complaints WHERE complaint_id = ?",
            (complaint_id,)
        ).fetchone()
        if not exists:
            conn.close()
            return complaint_id

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        student_name = request.form["student_name"]
        year = request.form["year"]
        department = request.form["department"]
        complaint_about = request.form["complaint_about"]
        details = request.form["details"]

        complaint_id = generate_id()

        conn = sqlite3.connect(DB)
        conn.execute("""
            INSERT INTO complaints
            (complaint_id, student_name, year, department, complaint_about, details)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (complaint_id, student_name, year, department, complaint_about, details))
        conn.commit()
        conn.close()

        return render_template("success.html", complaint_id=complaint_id)

    return render_template("index.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
