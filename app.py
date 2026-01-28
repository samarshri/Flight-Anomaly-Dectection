from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flightuser",
        password="flightpass",
        database="flight_anomaly"
    )

@app.route("/")
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Main table data
    cursor.execute("""
        SELECT flight_id, anomaly_score, final_anomaly, explanation, speed, altitude
        FROM flights
        ORDER BY anomaly_score DESC
        LIMIT 50
    """)
    flights = cursor.fetchall()

    # KPI queries
    cursor.execute("SELECT COUNT(*) AS total FROM flights")
    total_flights = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS anomalies FROM flights WHERE final_anomaly = 1")
    anomalies = cursor.fetchone()["anomalies"]

    cursor.execute("SELECT COUNT(*) AS normal FROM flights WHERE final_anomaly = 0")
    normal = cursor.fetchone()["normal"]

    cursor.execute("SELECT MAX(anomaly_score) AS max_score FROM flights")
    max_score = cursor.fetchone()["max_score"]

    cursor.close()
    conn.close()

    return render_template(
        "dashboard.html",
        flights=flights,
        total_flights=total_flights,
        anomalies=anomalies,
        normal=normal,
        max_score=max_score
    )



if __name__ == "__main__":
    app.run(debug=True)
