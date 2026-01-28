# 📄 Deep Dive: app.py (The "Server")

**Role**: The Gateway. It takes requests from the outside world (Browsers) and serves data.

## Key Sections Explained

### 1. Flask Initialization
```python
app = Flask(__name__)
```
*   Creates the application object. This object holds all your configuration and routes.

### 2. The Database Connector (Line 6-12)
```python
def get_db_connection():
    return mysql.connector.connect(...)
```
*   **Pattern**: We create a *new* connection for every single request.
*   **Why?** If we kept one connection open forever, it might "time out" or get confused if two users visited the site at the exact same time. Opening/Closing ensures freshness.

### 3. The Dashboard Route (Line 14)
```python
@app.route("/")
def dashboard():
```
*   This matches the root URL (`http://localhost:5000/`).
*   **The Query**:
    ```sql
    SELECT ... FROM flights ORDER BY anomaly_score DESC LIMIT 50
    ```
    *   `ORDER BY anomaly_score DESC`: Ensures the "Riskiest" flights are at the top of the table.
    *   `LIMIT 50`: Performance optimization. Even if the DB has 1 million rows, we only send 50 to the browser to keep it fast.

### 4. Fetching Data
```python
cursor = conn.cursor(dictionary=True)
flights = cursor.fetchall()
```
*   `dictionary=True`: This is critical.
    *   Normally, SQL gives you a list like `['BAW123', 60]`. You have to remember index 0 is ID, 1 is Score.
    *   With `dictionary=True`, SQL gives you `{'flight_id': 'BAW123', 'anomaly_score': 60}`. This allows us to use `f.flight_id` in the HTML, which is much more readable.

### 5. Rendering (Line 43)
```python
return render_template("dashboard.html", flights=flights, ...)
```
*   Passes the Python list `flights` into the HTML template engine.
*   Once this function returns, Flask takes the generated HTML string and sends it over the internet to the user.
