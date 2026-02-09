# Quick Reference Cheat Sheet

## 🚀 Essential Commands

### Starting the Project

```powershell
# Navigate to project folder
cd "d:\New folder (6)"

# Start the web dashboard (Terminal 1)
py app.py

# Start live data stream (Terminal 2 - Optional)
py stream_data.py
```

### Accessing the Dashboard
```
Browser URL: http://127.0.0.1:5000
```

### Stopping the Server
```
Press: Ctrl + C
```

---

## 📦 Installation & Setup

### Install Dependencies
```powershell
py -m pip install -r requirements.txt
```

### Database Setup
```powershell
# Run SQL setup (one-time)
mysql -u root -pYourPassword < setup_database.sql

# Or create manually in MySQL:
mysql -u root -p
CREATE DATABASE flight_anomaly;
CREATE USER 'flightuser'@'localhost' IDENTIFIED BY 'flightpass';
GRANT ALL PRIVILEGES ON flight_anomaly.* TO 'flightuser'@'localhost';
FLUSH PRIVILEGES;
exit
```

### Load Initial Data
```powershell
py save_to_db.py
```

---

## 🗄️ Database Commands

### Connect to MySQL
```powershell
mysql -u flightuser -pflightpass flight_anomaly
```

### Useful SQL Queries
```sql
-- See all flights
SELECT * FROM flights;

-- Count total flights
SELECT COUNT(*) FROM flights;

-- See only anomalies
SELECT * FROM flights WHERE final_anomaly = 1;

-- Top 10 highest risk flights
SELECT flight_id, anomaly_score, explanation 
FROM flights 
ORDER BY anomaly_score DESC 
LIMIT 10;

-- Clear all data
DELETE FROM flights;

-- Check table structure
DESCRIBE flights;
```

---

## 🐍 Python Basics Cheat Sheet

### Variables
```python
speed = 850.5          # Float (decimal number)
altitude = 10000       # Integer (whole number)
flight_id = "UAL123"   # String (text)
is_anomaly = True      # Boolean (True/False)
```

### Lists
```python
flights = ["UAL123", "DAL456", "AAL789"]
print(flights[0])      # UAL123 (first item)
print(len(flights))    # 3 (count items)
flights.append("SWA111")  # Add item
```

### Dictionaries
```python
flight = {
    "id": "UAL123",
    "speed": 850.5,
    "altitude": 10000
}
print(flight["speed"])  # 850.5
```

### Functions
```python
def calculate_delay_ratio(delay, duration):
    return delay / duration

result = calculate_delay_ratio(45, 180)
print(result)  # 0.25
```

### Conditionals
```python
if score >= 60:
    print("High risk!")
elif score >= 30:
    print("Medium risk")
else:
    print("Normal")
```

### Loops
```python
# For loop
for flight in flights:
    print(flight)

# While loop
count = 0
while count < 10:
    print(count)
    count += 1
```

---

## 📊 Pandas Quick Reference

```python
import pandas as pd

# Read CSV
df = pd.read_csv("data/flights.csv")

# View first 5 rows
print(df.head())

# View column names
print(df.columns)

# Get specific column
speeds = df['speed']

# Create new column
df['delay_ratio'] = df['delay'] / df['duration']

# Filter data
high_risk = df[df['anomaly_score'] >= 60]

# Loop through rows
for index, row in df.iterrows():
    print(row['flight_id'], row['speed'])
```

---

## 🌐 Flask Quick Reference

```python
from flask import Flask, render_template

app = Flask(__name__)

# Route: Homepage
@app.route("/")
def home():
    return "Hello World!"

# Route: With parameter
@app.route("/flight/<flight_id>")
def flight_detail(flight_id):
    return f"Flight: {flight_id}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🔍 Debugging Tips

### Print Statements
```python
print("Value of speed:", speed)
print("Type:", type(speed))
print("Length:", len(flights))
```

### Check Variable Type
```python
type(speed)       # <class 'float'>
type(flight_id)   # <class 'str'>
```

### Try-Except (Error Handling)
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
```

---

## 🛠️ Common Problems & Solutions

| Problem | Solution |
|---------|----------|
| Port 5000 already in use | Kill the process: `netstat -ano \| findstr :5000` then `taskkill /PID <PID> /F` |
| MySQL won't start | `net start MySQL80` (as Administrator) |
| Module not found | `py -m pip install <module-name>` |
| Database connection error | Check MySQL is running, check credentials |
| Import error | Make sure you're in the correct directory |

---

## 📁 Project File Summary

| File | Purpose | Run It? |
|------|---------|---------|
| `app.py` | Web dashboard | ✅ Yes (main) |
| `stream_data.py` | Live data fetcher | ✅ Yes (optional) |
| `save_to_db.py` | Load CSV to database | ✅ Once (setup) |
| `ai_learn.py` | Train AI on CSV | ⚠️ Optional |
| `read_data.py` | Utility script | ⚠️ Optional |
| `setup_database.sql` | Database schema | ✅ Once (setup) |
| `requirements.txt` | Dependencies list | 📄 Reference |
| `dashboard.html` | Web page template | 📄 Used by Flask |

---

## 🎯 Key Concepts

### Routes (Flask)
```python
@app.route("/")        # Homepage
@app.route("/about")   # About page
```

### SQL Operations
- **SELECT**: Get data
- **INSERT**: Add data
- **UPDATE**: Modify data
- **DELETE**: Remove data
- **CREATE**: Make table/database

### HTTP Methods
- **GET**: Retrieve data (viewing a page)
- **POST**: Send data (submitting a form)

### Data Types
- **VARCHAR**: Text with max length
- **INT**: Whole numbers
- **FLOAT**: Decimal numbers
- **TEXT**: Unlimited text

---

## 💻 VS Code Tips

### Keyboard Shortcuts
- `Ctrl + /` - Comment/uncomment line
- `Ctrl + S` - Save file
- `Ctrl + F` - Find in file
- `Ctrl + Shift + F` - Find in all files
- `Ctrl + ` ` - Open terminal
- `F5` - Run debugger

---

## 🌐 Useful URLs

- **Dashboard**: http://127.0.0.1:5000
- **OpenSky API**: https://opensky-network.org/api/states/all
- **MySQL Docs**: https://dev.mysql.com/doc/
- **Flask Docs**: https://flask.palletsprojects.com/
- **Pandas Docs**: https://pandas.pydata.org/docs/

---

## 📝 Git Commands (Version Control)

```bash
# Initialize repository
git init

# Check status
git status

# Stage files
git add .

# Commit changes
git commit -m "Your message here"

# View history
git log

# Create new branch
git branch feature-name
git checkout feature-name
```

---

## 🎓 Learning Path Checklist

### Week 1: Python Basics
- [ ] Variables, data types, operators
- [ ] Conditionals (if/else)
- [ ] Loops (for/while)
- [ ] Functions
- [ ] Lists and dictionaries

### Week 2: Working with Data
- [ ] Reading/writing CSV files
- [ ] Pandas basics
- [ ] Data cleaning
- [ ] Basic calculations

### Week 3: Databases
- [ ] SQL basics (SELECT, INSERT, UPDATE, DELETE)
- [ ] Creating tables
- [ ] Connecting Python to MySQL
- [ ] Queries from Python

### Week 4: Web Development
- [ ] HTML basics
- [ ] Flask routing
- [ ] Templates
- [ ] Passing data to templates

### Week 5: Machine Learning
- [ ] What is ML?
- [ ] Supervised vs Unsupervised learning
- [ ] Anomaly detection concepts
- [ ] Using scikit-learn

### Week 6: APIs & Integration
- [ ] HTTP requests
- [ ] Working with JSON
- [ ] API authentication
- [ ] Real-time data processing

---

**Keep this cheat sheet handy while coding!** 🚀
