# Flight Anomaly Detection - Complete Beginner's Guide

> A comprehensive learning guide for understanding every aspect of this AI-powered real-time flight monitoring system.

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Key Technologies Explained](#key-technologies-explained)
3. [Project Architecture](#project-architecture)
4. [Database Setup & Concepts](#database-setup--concepts)
5. [Code Walkthrough](#code-walkthrough)
6. [Machine Learning Concepts](#machine-learning-concepts)
7. [How to Run the Project](#how-to-run-the-project)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Learning Resources](#learning-resources)

---

## 🎯 Project Overview

### What Does This Project Do?

This project is a **real-time flight anomaly detection system** that:
- Fetches live flight data from the OpenSky Network API (real flights currently in the air)
- Uses AI to detect unusual flight patterns
- Displays results on a web dashboard
- Stores all data in a MySQL database

### Real-World Use Case

Airlines, air traffic controllers, and aviation security teams could use this to:
- Identify flights with unusual delays
- Detect abnormal speed or altitude patterns
- Monitor potential safety concerns in real-time
- Generate alerts for investigation

---

## 🛠️ Key Technologies Explained

### 1. **Python** 
**What**: A programming language  
**Why**: Easy to learn, powerful for data science and web development  
**In this project**: Used for everything - backend logic, AI, data processing

### 2. **Flask**
**What**: A lightweight web framework for Python  
**Why**: Makes it easy to create websites with Python  
**In this project**: Powers the web dashboard at `http://127.0.0.1:5000`

**Key Concept - Routes:**
```python
@app.route("/")
def dashboard():
    # This runs when you visit http://127.0.0.1:5000
```

### 3. **MySQL**
**What**: A database system (stores data in organized tables)  
**Why**: Reliable, industry-standard, handles lots of data efficiently  
**In this project**: Stores all flight information

**Key Concepts:**
- **Database**: Like a filing cabinet (`flight_anomaly`)
- **Table**: Like a folder in the cabinet (`flights`)
- **Row**: One entry (one flight)
- **Column**: One piece of info (like `speed`, `altitude`)

### 4. **Pandas**
**What**: Python library for working with data tables  
**Why**: Makes data manipulation super easy  
**In this project**: Loads CSV files, processes data before sending to AI

### 5. **Scikit-learn**
**What**: Python's machine learning library  
**Why**: Contains pre-built AI algorithms  
**In this project**: Used for `IsolationForest` algorithm to detect anomalies

### 6. **Requests**
**What**: Python library for making HTTP requests  
**Why**: Gets data from websites/APIs  
**In this project**: Fetches live flight data from OpenSky Network

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER'S WEB BROWSER                       │
│              (Visits http://127.0.0.1:5000)                 │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                     FLASK WEB APP                           │
│                      (app.py)                               │
│  • Receives requests from browser                           │
│  • Queries database for flight data                         │
│  • Renders HTML template with data                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                   MYSQL DATABASE                            │
│                 (flight_anomaly)                            │
│  • Stores all flight records                                │
│  • Updated by stream_data.py every 10 seconds               │
└────────────────────────┬────────────────────────────────────┘
                         ↑
                         │
┌─────────────────────────────────────────────────────────────┐
│              LIVE DATA STREAM                               │
│              (stream_data.py)                               │
│  1. Fetches live flights from OpenSky API                   │
│  2. Runs AI analysis on each flight                         │
│  3. Saves results to database                               │
│  4. Repeats every 10 seconds                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 💾 Database Setup & Concepts

### Understanding the Database Structure

#### Connection Credentials
```python
host="localhost"        # Database is on your computer
user="flightuser"       # Username we created
password="flightpass"   # Password for security
database="flight_anomaly"  # Name of our database
```

#### The `flights` Table Schema

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| `flight_id` | VARCHAR(50) | Flight identifier | "UAL123" |
| `speed` | FLOAT | Speed in km/h | 850.5 |
| `altitude` | FLOAT | Altitude in meters | 10000.0 |
| `duration` | FLOAT | Flight duration in minutes | 180.5 |
| `delay` | FLOAT | Delay in minutes | 45.0 |
| `anomaly_score` | FLOAT | AI-calculated risk score (0-100) | 70.0 |
| `final_anomaly` | INT | Is it an anomaly? (0=No, 1=Yes) | 1 |
| `explanation` | TEXT | Why flagged | "High delay, AI Pattern Alert" |

### SQL Commands You Used

```sql
-- Create the database
CREATE DATABASE IF NOT EXISTS flight_anomaly;

-- Create the user account
CREATE USER IF NOT EXISTS 'flightuser'@'localhost' IDENTIFIED BY 'flightpass';

-- Give permissions to the user
GRANT ALL PRIVILEGES ON flight_anomaly.* TO 'flightuser'@'localhost';

-- Create the table
CREATE TABLE IF NOT EXISTS flights (
    flight_id VARCHAR(50),
    speed FLOAT,
    altitude FLOAT,
    duration FLOAT,
    delay FLOAT,
    anomaly_score FLOAT,
    final_anomaly INT,
    explanation TEXT
);
```

---

## 📝 Code Walkthrough

### File Structure
```
d:\New folder (6)\
├── app.py                  # Main web application
├── stream_data.py          # Live data fetcher + AI
├── save_to_db.py          # Saves CSV data to database
├── ai_learn.py            # Trains AI on historical data
├── read_data.py           # Utility to read data
├── setup_database.sql     # Database setup script
├── requirements.txt       # Python packages needed
├── data/
│   ├── flights.csv        # Historical training data
│   └── final_ai_output.csv # AI results
├── templates/
│   └── dashboard.html     # Web page template
└── learning_materials/    # This guide!
```

---

### app.py - The Web Dashboard

This file creates the website you see in your browser.

**Key functions:**
- `get_db_connection()` - Connects to MySQL database
- `dashboard()` - Main page that shows flight data

**How it works:**
1. User visits http://127.0.0.1:5000
2. Flask calls `dashboard()` function
3. Function connects to database
4. Queries flights table for data
5. Calculates statistics (total flights, anomalies, etc.)
6. Renders HTML template with data
7. Sends page to browser

---

### stream_data.py - Live Data Engine

This is the "heart" of the real-time system!

**What it does:**
1. **Training** (once at startup):
   - Loads historical flight data
   - Trains IsolationForest AI model
   
2. **Forever Loop** (continuous):
   - Fetches live flights from OpenSky API
   - For each flight:
     - Calculates features (delay_ratio, speed_per_min)
     - Gets AI prediction
     - Applies human rules (delay checks, speed checks)
     - Calculates anomaly score
     - Saves to database
   - Waits 10 seconds
   - Repeats

**Scoring System:**
- Delay > 80% of duration: +40 points
- Speed too low: +30 points
- AI detects pattern: +30 points
- **Total >= 60 points = Anomaly!**

---

## 🤖 Machine Learning Concepts

### What is Anomaly Detection?

Finding unusual patterns in data.

**Example:**
- Normal flights: 800-900 km/h at 10,000m
- Anomaly: 200 km/h at 2,000m → Suspicious!

### Isolation Forest Algorithm

**Simple explanation:**
- Normal data points cluster together
- Anomalies stand out alone
- Algorithm tries to "isolate" each point
- If easy to isolate (few cuts needed) → Anomaly!

### Feature Engineering

Creating helpful new columns from existing data:

```python
# Original data
delay = 45 minutes
duration = 180 minutes

# Engineered feature (more meaningful!)
delay_ratio = 45 / 180 = 0.25 (25%)
```

This helps the AI understand "25% of flight was delayed" rather than trying to compare raw numbers.

---

## 🚀 How to Run the Project

### Step-by-Step Guide

#### 1. Install Dependencies
```powershell
cd "d:\New folder (6)"
py -m pip install -r requirements.txt
```

#### 2. Set Up Database
```powershell
mysql -u root -pYourPassword -e "CREATE DATABASE flight_anomaly; CREATE USER 'flightuser'@'localhost' IDENTIFIED BY 'flightpass'; GRANT ALL PRIVILEGES ON flight_anomaly.* TO 'flightuser'@'localhost'; FLUSH PRIVILEGES;"
```

#### 3. Load Initial Data
```powershell
py save_to_db.py
```

#### 4. Start Web Dashboard
```powershell
py app.py
```
Visit: http://127.0.0.1:5000

#### 5. (Optional) Start Live Stream

Open a **new terminal**:
```powershell
cd "d:\New folder (6)"
py stream_data.py
```

---

## 🔧 Troubleshooting Guide

### Problem: "Access denied for user 'flightuser'"

**Solution:**
```sql
CREATE USER 'flightuser'@'localhost' IDENTIFIED BY 'flightpass';
GRANT ALL PRIVILEGES ON flight_anomaly.* TO 'flightuser'@'localhost';
FLUSH PRIVILEGES;
```

### Problem: "No module named 'requests'"

**Solution:**
```powershell
py -m pip install requests
```

### Problem: "Can't connect to MySQL server"

**Solution:**
```powershell
# Start MySQL service
net start MySQL80
```

### Problem: Port 5000 already in use

**Solution:**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill it (replace PID with actual number)
taskkill /PID <PID> /F
```

---

## 📚 Learning Resources

### Python
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)

### Flask
- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### MySQL
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [W3Schools SQL](https://www.w3schools.com/sql/)

### Pandas
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### Machine Learning
- [Scikit-learn Tutorial](https://scikit-learn.org/stable/tutorial/index.html)
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)

### APIs
- [OpenSky Network Docs](https://openskynetwork.github.io/opensky-api/)

---

## 🎓 What You've Learned

By completing this project, you now understand:

✅ **Python Programming**  
✅ **Web Development** with Flask  
✅ **Database Design** and SQL  
✅ **Machine Learning** fundamentals  
✅ **API Integration**  
✅ **Real-time Data Processing**  

---

## 🚀 Next Steps

### Beginner Projects
1. Add charts to the dashboard (Chart.js)
2. Create email alerts for high-risk flights
3. Add search functionality

### Intermediate Challenges
1. User authentication system
2. Export reports to PDF
3. Real-time dashboard updates (WebSockets)

### Advanced Topics
1. Deploy to cloud (AWS/Azure/Heroku)
2. Use deep learning instead of Isolation Forest
3. Scale to handle millions of flights

---

**Keep learning and building!** 🎉

Every expert was once a beginner. The key is to keep coding and experimenting!
