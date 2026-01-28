import pandas as pd
import mysql.connector

# ----------------------------
# Helper function to clean values
# ----------------------------
def clean(val):
    """
    Converts NaN / 'nan' / None to None so MySQL can store NULL.
    """
    if val is None:
        return None
    if isinstance(val, float) and pd.isna(val):
        return None
    if isinstance(val, str) and val.lower() == "nan":
        return None
    return val


# ----------------------------
# Load final AI output
# ----------------------------
df = pd.read_csv("data/final_ai_output.csv")

# ----------------------------
# Connect to MySQL
# ----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="flightuser",
    password="flightpass",
    database="flight_anomaly"
)

cursor = conn.cursor()

# ----------------------------
# Clear old data (important)
# ----------------------------
# ----------------------------
# Ensure table exists
# ----------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        flight_id VARCHAR(50),
        speed FLOAT,
        altitude FLOAT,
        duration FLOAT,
        delay FLOAT,
        anomaly_score FLOAT,
        final_anomaly INT,
        explanation TEXT
    )
""")

# ----------------------------
# Clear old data (important)
# ----------------------------
cursor.execute("DELETE FROM flights")

# ----------------------------
# Insert rows one by one
# ----------------------------
for _, row in df.iterrows():
    sql = """
        INSERT INTO flights
        (flight_id, speed, altitude, duration, delay,
         anomaly_score, final_anomaly, explanation)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        clean(row['flight_id']),
        clean(row['speed']),
        clean(row['altitude']),
        clean(row['duration']),
        clean(row['delay']),
        clean(row['anomaly_score']),
        clean(row['final_anomaly']),
        clean(row['explanation'])
    )

    cursor.execute(sql, values)

# ----------------------------
# Commit & close
# ----------------------------
conn.commit()
conn.close()

print("AI results saved to database successfully.")
