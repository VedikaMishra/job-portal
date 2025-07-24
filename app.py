from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vedika@1212',  # 🔁 Enter your actual MySQL password
        database='job_portol'
    )


@app.route('/')
def job_list():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT DISTINCT title FROM jobs")
    roles = [row['title'] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT location FROM jobs")
    locations = [row['location'] for row in cursor.fetchall()]

    selected_role = request.args.get('role')
    selected_location = request.args.get('location')

    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if selected_role:
        query += " AND title = %s"
        params.append(selected_role)
    if selected_location:
        query += " AND location = %s"
        params.append(selected_location)

    cursor.execute(query, params)
    jobs = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('jobs.html', jobs=jobs, roles=roles, locations=locations)

if __name__ == '__main__':
    app.run(debug=True)
