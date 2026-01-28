import time
import requests
import pandas as pd
import mysql.connector
import random
from sklearn.ensemble import IsolationForest

# ----------------------------
# 1. Setup & Train Model (The "Brain")
# ----------------------------
print("Initializing AI System...")
print("Training Anomaly Detection Model on historical data...")

# Load historical data to teach the model what "normal" looks like
df_history = pd.read_csv("data/flights.csv")
df_history['delay_ratio'] = df_history['delay'] / df_history['duration']
df_history['speed_per_min'] = df_history['speed'] / df_history['duration']
features = ['speed', 'altitude', 'duration', 'delay', 'delay_ratio', 'speed_per_min']

# Train the model
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(df_history[features])
print("Model Trained and Ready.")

# ----------------------------
# 2. Database Connection
# ----------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flightuser",
        password="flightpass",
        database="flight_anomaly"
    )

# ----------------------------
# 3. Live Data Fetching (OpenSky API)
# ----------------------------
# Bounding box for a busy area (London/Europe) to ensure we get data
# min_lat, min_lon, max_lat, max_lon
URL = "https://opensky-network.org/api/states/all?lamin=49.0&lomin=-2.0&lamax=52.0&lomax=1.0"

def fetch_live_flights():
    try:
        print("Scaning skies via OpenSky Network...")
        response = requests.get(URL, timeout=10)
        data = response.json()
        
        if 'states' not in data or data['states'] is None:
            print("No flights found in sector.")
            return []
            
        # Parse the raw API data
        flights = []
        for raw in data['states'][:10]: # Process top 10 flights to stay fast
            # OpenSky Data Structure: 
            # 0: icao24, 1: callsign, 5: longitude, 6: latitude, 7: baro_altitude, 9: velocity
            
            callsign = raw[1].strip()
            if not callsign: callsign = raw[0] # Fallback to ICAO ID
            
            altitude = raw[7]
            velocity = raw[9]
            
            # Skip incomplete data
            if altitude is None or velocity is None:
                continue
                
            # Synthesize missing columns that API doesn't give (Duration/Delay)
            # using random realistic values to allow the model to run
            duration = random.uniform(50, 600) 
            delay = random.uniform(0, 100)
            
            flights.append({
                'flight_id': callsign,
                'speed': velocity * 3.6, # Convert m/s to km/h roughly
                'altitude': altitude,
                'duration': duration,
                'delay': delay
            })
            
        print(f"Detected {len(flights)} aircraft.")
        return flights
    except Exception as e:
        print(f"Radar Error: {e}")
        return []

# ----------------------------
# 4. Main Control Loop
# ----------------------------
print("Starting Real-Time Monitoring Stream...")

while True:
    live_flights = fetch_live_flights()
    
    if live_flights:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        for f in live_flights:
            # Prepare features for AI
            delay_ratio = f['delay'] / f['duration']
            speed_per_min = f['speed'] / f['duration']
            
            # Create DataFrame for prediction (single row)
            feature_row = pd.DataFrame([[f['speed'], f['altitude'], f['duration'], f['delay'], delay_ratio, speed_per_min]], 
                                       columns=features)
            
            # AI Decision
            ai_raw = model.predict(feature_row)[0] # 1 normal, -1 anomaly
            
            # Heuristics + AI Scoring
            score = 0
            reasons = []
            
            if delay_ratio > 0.8:
                score += 40
                reasons.append("Critical Delay")
            
            if speed_per_min < 2: # Adjusted for live data
                score += 30
                reasons.append("Abnormal Low Speed")
                
            if ai_raw == -1:
                score += 30
                reasons.append("AI Pattern Alert")
                
            final_anomaly = 1 if score >= 60 else 0
            explanation = ", ".join(reasons) if reasons else "Normal Operation"
            
            # Database Insert
            sql = """
                INSERT INTO flights 
                (flight_id, speed, altitude, duration, delay, anomaly_score, final_anomaly, explanation)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (f['flight_id'], f['speed'], f['altitude'], f['duration'], f['delay'], 
                                 score, final_anomaly, explanation))
            
            print(f"Logged Flight {f['flight_id']} | Score: {score} | {explanation}")
            
        conn.commit()
        conn.close()
        print("Database Updated.")
    
    print("Waiting 10 seconds for next scan...")
    time.sleep(10)
