# 📄 Deep Dive: stream_data.py (The "Radar")

**Role**: The Input System. It runs forever in the background.

## Key Sections Explained

### 1. The Setup
```python
import time, requests, pandas, mysql.connector
from sklearn.ensemble import IsolationForest
```
*   **Why these imports?**
    *   `requests` is vital for talking to the OpenSky API.
    *   `IsolationForest` is our specific Anomaly Detection algorithm. It works by "isolating" points. If a point is easy to isolate (needs few cuts), it's an anomaly.

### 2. Model Training (Line 15-22)
```python
df_history = pd.read_csv("data/flights.csv")
model.fit(df_history[features])
```
*   **The Concept**: Before we can judge *live* flights, we need to know what a flight *is*.
*   We load `flights.csv` (historical data).
*   `model.fit()`: The AI studies this old data to learn the mathematical shape of "Normal".
*   *Note*: This happens once every time you start the script.

### 3. The API Call (Line 42)
```python
URL = "https://opensky-network.org/api/states/all?lamin=49.0..."
response = requests.get(URL, timeout=10)
```
*   **The URL parameters**: `lamin`, `lomin`, etc. define a **Bounding Box**. We are looking at a square over the UK/France.
*   **Timeout**: We set `timeout=10`. If OpenSky doesn't answer in 10 seconds, we give up instead of freezing the program forever.

### 4. Data Parsing (Line 52-78)
The API gives us a messy list. We clean it.
```python
velocity = raw[9]  # API gives velocity in meters/second
speed = velocity * 3.6  # We convert to km/h for human readability
```
*   **Missing Data**: Real sensors are imperfect. Some planes don't report speed.
    *   `if altitude is None or velocity is None: continue`
    *   We **skip** these planes. Bad data is worse than no data.

### 5. The Scoring Logic (Line 115-133)
We combine AI with Human Rules (Heuristics).
```python
score = 0
if ai_raw == -1: score += 30      # AI Vote
if delay_ratio > 0.8: score += 40 # Human Rule (Delay)
```
*   **Why both?**
    *   AI is good at weird patterns humans miss.
    *   Humans are good at hard rules ("If delay is huge, it's bad").
    *   By summing them (`score`), we get a nuanced Risk Score (0-100) instead of just Yes/No.

### 6. Database Insertion (Line 144)
```python
sql = "INSERT INTO flights ... VALUES (%s, ...)"
cursor.execute(sql, (val1, val2...))
```
*   We use **Transactions**. The changes aren't real until `conn.commit()` is called. This ensures we don't save half a flight if the script crashes mid-write.
