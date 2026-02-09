# Programming Fundamentals - From Zero to Hero

> A complete guide to understanding every programming concept used in this project

---

## 📌 How to Use This Guide

This guide assumes **ZERO prior programming knowledge**. We'll build your understanding from the ground up, explaining every single concept before using it.

**Learning Method**:
1. Read each section carefully
2. Try the examples in Python
3. Do the practice exercises
4. Move to the next section

---

## Part 1: The Very Basics

### What is a Program?

A program is simply a **list of instructions** that a computer follows, one by one.

**Real-world analogy**: A recipe
```
Recipe for making tea:
1. Boil water
2. Put tea bag in cup
3. Pour hot water in cup
4. Wait 3 minutes
5. Remove tea bag
6. Add sugar
7. Drink
```

A computer program works the same way - step by step instructions!

---

### What is Python?

Python is a **programming language** - a way for humans to write instructions that computers can understand.

**Why Python?**
- Reads like English
- Great for beginners
- Powerful for professionals
- Huge community & libraries

---

### Your First Python Program

```python
print("Hello, World!")
```

**What happens?**
1. You type this code
2. Python reads it
3. Python shows "Hello, World!" on screen

**Try it!**
1. Open PowerShell/Terminal
2. Type `py` and press Enter (this opens Python)
3. Type `print("Hello, World!")` and press Enter
4. See your message!
5. Type `exit()` to leave Python

---

## Part 2: Variables - Storing Information

### What is a Variable?

A variable is a **named box** that stores information.

**Visual Example**:
```
┌────────────────┐
│  speed = 850   │  ← Variable named "speed" holding value 850
└────────────────┘

┌──────────────────────┐
│  name = "John"       │  ← Variable named "name" holding text "John"
└──────────────────────┘
```

### Creating Variables in Python

```python
# Storing numbers
speed = 850
altitude = 10000
delay = 45

# Storing text (called "strings")
flight_id = "UAL123"
airport = "JFK"

# Storing True/False (called "booleans")
is_delayed = True
is_landed = False
```

**Rules for Variable Names**:
- ✅ Can contain letters, numbers, underscores: `flight_speed`, `speed2`
- ✅ Should be descriptive: `delay` is better than `d`
- ❌ Can't start with number: `2fast` is invalid
- ❌ Can't have spaces: `flight speed` is invalid (use `flight_speed`)
- ❌ Can't use reserved words: `print`, `if`, `for`

### Using Variables

```python
# Store value
speed = 850

# Use value
print(speed)  # Shows: 850

# Do math with variables
double_speed = speed * 2
print(double_speed)  # Shows: 1700

# Change value
speed = 900
print(speed)  # Shows: 900 (new value)
```

**Practice Exercise**:
```python
# Create these variables:
flight_number = "AA101"
passengers = 150
fuel_level = 75.5

# Print them
print(flight_number)
print(passengers)
print(fuel_level)
```

---

## Part 3: Data Types - Different Kinds of Information

### The Main Data Types

Python has different **types** of data, like how objects in real life are different:

| Type | Python Name | Examples | Used For |
|------|-------------|----------|----------|
| Whole Numbers | `int` | 10, 850, -5 | Counting, IDs |
| Decimal Numbers | `float` | 3.14, 850.5, 0.25 | Measurements |
| Text | `str` (string) | "Hello", "UAL123" | Names, messages |
| True/False | `bool` (boolean) | True, False | Yes/no questions |
| Nothing | `None` | None | Missing data |

### Detailed Examples

#### Integers (int)
```python
passengers = 150
seat_number = 23
delay_minutes = -10  # negative means early!

# Math with integers
total = 100 + 50  # Addition: 150
difference = 100 - 30  # Subtraction: 70
product = 10 * 5  # Multiplication: 50
quotient = 100 / 4  # Division: 25.0 (becomes float!)
```

#### Floats (float)
```python
fuel_level = 75.5
temperature = -12.3
pi = 3.14159

# Math with floats
ratio = 45.0 / 180.0  # 0.25
percentage = ratio * 100  # 25.0
```

**⚠️ Important**: Dividing always gives a float!
```python
10 / 2  # Result: 5.0 (not 5)
```

#### Strings (str)
```python
name = "John Smith"
airport = 'JFK'  # Single or double quotes work
flight = "UA" + "123"  # Combines: "UA123"

# String operations
message = "Flight UAL123"
print(len(message))  # Length: 13 characters
print(message.upper())  # "FLIGHT UAL123"
print(message.lower())  # "flight ual123"
```

**String Formatting** (Super useful!):
```python
flight_id = "UAL123"
speed = 850

# Method 1: f-strings (modern, best)
message = f"Flight {flight_id} is traveling at {speed} km/h"
print(message)  # "Flight UAL123 is traveling at 850 km/h"

# Method 2: .format()
message = "Flight {} is traveling at {} km/h".format(flight_id, speed)

# Method 3: Concatenation (old way)
message = "Flight " + flight_id + " is traveling at " + str(speed) + " km/h"
```

#### Booleans (bool)
```python
is_delayed = True
is_on_time = False
has_landed = True

# Boolean operations
print(True and True)   # True (both must be True)
print(True and False)  # False
print(True or False)   # True (at least one is True)
print(not True)        # False (opposite)
```

### Checking Types

```python
speed = 850
name = "John"

print(type(speed))  # <class 'int'>
print(type(name))   # <class 'str'>

# Convert between types
number_as_string = "123"
number_as_int = int(number_as_string)  # 123
number_as_float = float(number_as_string)  # 123.0
```

**Practice Exercise**:
```python
# What type are these?
a = 42
b = 3.14
c = "Hello"
d = True
e = None

# Check with type()
print(type(a))
print(type(b))
# ... do the rest
```

---

## Part 4: Operators - Doing Math and Comparisons

### Arithmetic Operators

```python
a = 10
b = 3

# Basic math
print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333...
print(a // b)  # Floor division: 3 (rounds down)
print(a % b)   # Modulo (remainder): 1
print(a ** b)  # Exponent (10^3): 1000
```

**Real example from project**:
```python
delay = 45  # minutes
duration = 180  # minutes

# Calculate delay as percentage
delay_ratio = delay / duration  # 0.25
delay_percentage = delay_ratio * 100  # 25.0

print(f"Flight was delayed {delay_percentage}% of total time")
```

### Comparison Operators

These compare values and return `True` or `False`:

```python
speed = 850
max_speed = 900

print(speed == max_speed)  # Equal to: False
print(speed != max_speed)  # Not equal: True
print(speed > 800)         # Greater than: True
print(speed < 900)         # Less than: True
print(speed >= 850)        # Greater or equal: True
print(speed <= 900)        # Less or equal: True
```

**⚠️ Common Mistake**:
```python
# WRONG - assigns value
speed = 850

# RIGHT - compares value
speed == 850
```

### Logical Operators

Combine multiple conditions:

```python
speed = 850
altitude = 10000

# AND - both must be True
if speed > 800 and altitude > 9000:
    print("Fast and high!")  # This runs

# OR - at least one must be True
if speed > 1000 or altitude > 9000:
    print("Either fast OR high")  # This runs

# NOT - opposite
is_slow = not (speed > 800)  # False
```

**Practice Exercise**:
```python
delay = 60
duration = 120
speed = 750

# Calculate
delay_ratio = delay / duration

# Check if delay is more than 50% AND speed is low
if delay_ratio > 0.5 and speed < 800:
    print("Problem flight!")
```

---

## Part 5: Conditionals - Making Decisions

### The if Statement

Programs need to make decisions based on data:

```python
speed = 850

if speed > 900:
    print("Too fast!")
```

**Visual Flow**:
```
┌─────────────────┐
│  speed = 850    │
└────────┬────────┘
         │
         ↓
    ┌────────────┐
    │ speed > 900? │  ← Check condition
    └──┬──────┬──┘
       │ No   │ Yes
       ↓      ↓
    [Skip]  [Print "Too fast!"]
```

### if-else

```python
speed = 850

if speed > 900:
    print("Too fast!")
else:
    print("Speed is OK")
```

**In this case**: Since 850 is NOT > 900, it prints "Speed is OK"

### if-elif-else (Multiple Conditions)

```python
score = 75

if score >= 90:
    print("Excellent!")
elif score >= 70:
    print("Good!")
elif score >= 50:
    print("OK")
else:
    print("Needs improvement")
```

**How it works**:
1. Check first condition (score >= 90)? No
2. Check second condition (score >= 70)? Yes! ✓
3. Print "Good!" and **stop checking** (doesn't check the rest)

**Real Example from Project**:
```python
anomaly_score = 75

if anomaly_score >= 60:
    severity = "High"
elif anomaly_score >= 30:
    severity = "Medium"
else:
    severity = "Low"

print(f"Risk Level: {severity}")  # "Risk Level: High"
```

### Nested if Statements

```python
is_delayed = True
delay_minutes = 120

if is_delayed:
    if delay_minutes > 60:
        print("Major delay!")
    else:
        print("Minor delay")
else:
    print("On time")
```

**Practice Exercise**:
```python
speed = 850
altitude = 10000

# Write code that:
# - If speed > 900 AND altitude > 12000, print "Danger!"
# - If speed > 900 OR altitude > 12000, print "Warning"
# - Otherwise print "Normal"
```

---

## Part 6: Lists - Storing Multiple Values

### What is a List?

A list is a **container** that holds multiple values in order.

**Visual**:
```
flights = ["UAL123", "DAL456", "AAL789"]

Index:      0         1         2
         ┌────────┬────────┬────────┐
         │ UAL123 │ DAL456 │ AAL789 │
         └────────┴────────┴────────┘
```

**⚠️ Important**: Python counts from 0, not 1!

### Creating Lists

```python
# Empty list
empty = []

# List of numbers
speeds = [850, 920, 780, 865]

# List of strings
airlines = ["United", "Delta", "American"]

# Mixed types (allowed but not common)
mixed = [123, "Hello", True, 3.14]
```

### Accessing List Items

```python
flights = ["UAL123", "DAL456", "AAL789"]

# Get items by index (position)
first = flights[0]    # "UAL123"
second = flights[1]   # "DAL456"
last = flights[-1]    # "AAL789" (negative counts from end)

print(first)  # UAL123
```

### List Operations

```python
flights = ["UAL123", "DAL456"]

# Add to end
flights.append("AAL789")
print(flights)  # ["UAL123", "DAL456", "AAL789"]

# Insert at position
flights.insert(1, "SWA111")  # Insert at index 1
print(flights)  # ["UAL123", "SWA111", "DAL456", "AAL789"]

# Remove item
flights.remove("DAL456")
print(flights)  # ["UAL123", "SWA111", "AAL789"]

# Get length
count = len(flights)  # 3

# Check if item exists
if "UAL123" in flights:
    print("Found it!")
```

### Slicing Lists

```python
numbers = [10, 20, 30, 40, 50]

# Get subset
first_three = numbers[0:3]  # [10, 20, 30] (start:stop)
middle = numbers[1:4]        # [20, 30, 40]
from_third = numbers[2:]     # [30, 40, 50] (from index 2 to end)
first_two = numbers[:2]      # [10, 20] (from start to index 2)
```

**Real Example from Project**:
```python
# Get top 10 flights from API
all_flights = data['states']  # Might have 100+ flights
top_10 = all_flights[:10]     # Just first 10
```

**Practice Exercise**:
```python
scores = [85, 92, 78, 65, 90, 88]

# 1. Print the first score
# 2. Print the last score
# 3. Add score 95 to the end
# 4. Print the length
# 5. Print scores from index 1 to 3
```

---

## Part 7: Dictionaries - Named Values

### What is a Dictionary?

A dictionary stores **key-value pairs** - like a real dictionary where you look up a word (key) to get its definition (value).

**Visual**:
```
flight = {
    "id": "UAL123",
    "speed": 850,
    "altitude": 10000
}

        KEY  →  VALUE
        ───     ─────
        "id"    "UAL123"
        "speed" 850
        "altitude" 10000
```

### Creating Dictionaries

```python
# Empty dictionary
empty = {}

# Flight information
flight = {
    "id": "UAL123",
    "speed": 850,
    "altitude": 10000,
    "delayed": False
}

# Person information
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

### Accessing Values

```python
flight = {
    "id": "UAL123",
    "speed": 850,
    "altitude": 10000
}

# Get value by key
flight_id = flight["id"]       # "UAL123"
speed = flight["speed"]        # 850

# Safer way (doesn't crash if key missing)
altitude = flight.get("altitude")  # 10000
passengers = flight.get("passengers", 0)  # 0 (default)

print(f"Flight {flight_id} traveling at {speed} km/h")
```

### Modifying Dictionaries

```python
flight = {"id": "UAL123", "speed": 850}

# Add new key-value pair
flight["altitude"] = 10000

# Change existing value
flight["speed"] = 900

# Remove key
del flight["altitude"]

print(flight)  # {"id": "UAL123", "speed": 900}
```

### Dictionary Methods

```python
flight = {
    "id": "UAL123",
    "speed": 850,
    "altitude": 10000
}

# Get all keys
keys = flight.keys()  # ["id", "speed", "altitude"]

# Get all values
values = flight.values()  # ["UAL123", 850, 10000]

# Get all key-value pairs
items = flight.items()  # [("id", "UAL123"), ("speed", 850), ...]

# Check if key exists
if "speed" in flight:
    print("Has speed data")
```

**Real Example from Project**:
```python
# MySQL returns rows as dictionaries when we use dictionary=True
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM flights LIMIT 1")
flight = cursor.fetchone()

# Now we can access like this:
print(flight["flight_id"])
print(flight["speed"])
print(flight["anomaly_score"])
```

**Practice Exercise**:
```python
# Create a dictionary for yourself
person = {
    "name": "Your Name",
    "age": 25,
    "city": "Your City"
}

# 1. Print your name
# 2. Add a "country" key
# 3. Change your age
# 4. Print all keys
```

---

## Part 8: Loops - Repeating Actions

### What is a Loop?

A loop repeats code multiple times automatically.

**Real-world analogy**:
```
For each dirty dish:
    - Wash dish
    - Rinse dish
    - Put in rack
```

### The for Loop

**Looping through a list**:
```python
flights = ["UAL123", "DAL456", "AAL789"]

for flight in flights:
    print(f"Processing {flight}")

# Output:
# Processing UAL123
# Processing DAL456
# Processing AAL789
```

**How it works**:
```
Step 1: flight = "UAL123" → Run code block
Step 2: flight = "DAL456" → Run code block  
Step 3: flight = "AAL789" → Run code block
Step 4: No more items → Stop
```

**Looping through a range of numbers**:
```python
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4
```

```python
for i in range(1, 6):  # Start at 1, stop before 6
    print(i)

# Output: 1, 2, 3, 4, 5
```

```python
for i in range(0, 10, 2):  # Start, Stop, Step
    print(i)

# Output: 0, 2, 4, 6, 8
```

**Looping through dictionary**:
```python
flight = {"id": "UAL123", "speed": 850, "altitude": 10000}

# Loop through keys
for key in flight:
    print(key)  # id, speed, altitude

# Loop through values
for value in flight.values():
    print(value)  # UAL123, 850, 10000

# Loop through both
for key, value in flight.items():
    print(f"{key}: {value}")
    # id: UAL123
    # speed: 850
    # altitude: 10000
```

**Real Example from Project**:
```python
# Process each flight from API
live_flights = fetch_live_flights()

for f in live_flights:
    # Calculate features
    delay_ratio = f['delay'] / f['duration']
    
    # Run AI analysis
    ai_prediction = model.predict(...)
    
    # Save to database
    cursor.execute(sql, (...))
```

### The while Loop

Repeats **while** a condition is True:

```python
count = 0

while count < 5:
    print(count)
    count = count + 1  # or count += 1

# Output: 0, 1, 2, 3, 4
```

**Real Example - Infinite Loop for Server**:
```python
while True:  # Forever!
    live_flights = fetch_live_flights()
    process_flights(live_flights)
    time.sleep(10)  # Wait 10 seconds
    # Repeat...
```

### Loop Control: break and continue

**break** - Stop loop immediately:
```python
for i in range(10):
    if i == 5:
        break  # Stop when i is 5
    print(i)

# Output: 0, 1, 2, 3, 4
```

**continue** - Skip to next iteration:
```python
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)

# Output: 0, 1, 3, 4 (skipped 2)
```

**Real Example**:
```python
for raw in data['states']:
    altitude = raw[7]
    
    # Skip flights with missing data
    if altitude is None:
        continue  # Skip this one, go to next
    
    # Process flight
    process_flight(altitude)
```

**Practice Exercise**:
```python
speeds = [850, 920, 780, 500, 865]

# 1. Print each speed
# 2. Print only speeds > 800
# 3. Count how many speeds are > 800
# 4. Find the maximum speed
```

---

## Part 9: Functions - Reusable Code Blocks

### What is a Function?

A function is a **named block of code** you can run multiple times.

**Real-world analogy**: A button on your phone
- "Call Mom" button → Runs the calling code
- You don't rewrite the code each time, just press the button!

### Creating Functions

```python
def greet():
    print("Hello!")
    print("Welcome!")

# Call the function
greet()
greet()

# Output:
# Hello!
# Welcome!
# Hello!
# Welcome!
```

### Functions with Parameters

Parameters are **inputs** to the function:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("John")   # Hello, John!
greet("Sarah")  # Hello, Sarah!
```

**Multiple parameters**:
```python
def calculate_delay_ratio(delay, duration):
    ratio = delay / duration
    return ratio

result = calculate_delay_ratio(45, 180)
print(result)  # 0.25
```

### Return Values

Functions can **give back** results using `return`:

```python
def add(a, b):
    result = a + b
    return result  # Send back the answer

total = add(10, 20)
print(total)  # 30

# Can use directly
print(add(5, 7))  # 12
```

**Important**: Without `return`, function gives back `None`:
```python
def greet(name):
    print(f"Hello, {name}")
    # No return!

result = greet("John")
print(result)  # None
```

### Real Examples from Project

**Database connection function**:
```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flightuser",
        password="flightpass",
        database="flight_anomaly"
    )

# Use it anywhere
conn = get_db_connection()
cursor = conn.cursor()
```

**Data cleaning function**:
```python
def clean(val):
    """Convert NaN/None to None for database"""
    if val is None:
        return None
    if isinstance(val, float) and pd.isna(val):
        return None
    if isinstance(val, str) and val.lower() == "nan":
        return None
    return val

# Use it
clean_speed = clean(speed)
clean_altitude = clean(altitude)
```

**Analysis function**:
```python
def analyze_flight(speed, altitude, delay, duration):
    score = 0
    reasons = []
    
    delay_ratio = delay / duration
    if delay_ratio > 0.8:
        score += 40
        reasons.append("High delay")
    
    if speed < 700:
        score += 30
        reasons.append("Low speed")
    
    return score, reasons

# Use it
score, reasons = analyze_flight(650, 10000, 150, 180)
print(f"Score: {score}, Reasons: {reasons}")
```

### Default Parameters

Give parameters default values:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("John")   # Hello, John!
greet()         # Hello, Guest! (uses default)
```

**Practice Exercise**:
```python
# Create a function that:
# - Takes speed and max_speed as parameters
# - Returns True if speed > max_speed
# - Returns False otherwise

def is_speeding(speed, max_speed):
    # Your code here
    pass

# Test it
print(is_speeding(900, 850))  # Should be True
print(is_speeding(800, 850))  # Should be False
```

---

## Part 10: Working with Files

### Reading Text Files

```python
# Open and read entire file
file = open("data.txt", "r")  # "r" = read mode
content = file.read()
print(content)
file.close()  # Always close!

# Better way - automatically closes
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File automatically closed here
```

### Reading Line by Line

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes \n
```

### Writing to Files

```python
# Write mode - creates new or overwrites existing
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Append mode - adds to end
with open("output.txt", "a") as file:
    file.write("Added line\n")
```

### Working with CSV Files (Using Pandas)

CSV = Comma Separated Values

**Example CSV**:
```
flight_id,speed,altitude
UAL123,850,10000
DAL456,920,11000
```

**Read with Pandas**:
```python
import pandas as pd

# Read CSV into DataFrame
df = pd.read_csv("data/flights.csv")

# See first 5 rows
print(df.head())

# Access column
speeds = df['speed']
print(speeds)

# Access row by index
first_row = df.iloc[0]  # First row
```

**Real Example from Project**:
```python
# Load historical flight data
df_history = pd.read_csv("data/flights.csv")

# Create new calculated columns
df_history['delay_ratio'] = df_history['delay'] / df_history['duration']

# Save results
df.to_csv("data/final_ai_output.csv", index=False)
```

---

## Part 11: Understanding Database Concepts

### What is a Database?

A database is an **organized collection of data** stored electronically.

**Visual**:
```
DATABASE: flight_anomaly
│
└─ TABLE: flights
   │
   ├─ ROW 1: UAL123, 850, 10000, ...
   ├─ ROW 2: DAL456, 920, 11000, ...
   └─ ROW 3: AAL789, 780, 9500, ...
   
   COLUMNS: flight_id, speed, altitude, ...
```

### Why Use a Database Instead of CSV?

| Feature | CSV File | Database |
|---------|----------|----------|
| Speed (large data) | Slow | Fast |
| Multiple users | Problems | Great |
| Search | Read entire file | Instant |
| Relationships | Hard | Easy |
| Data integrity | None | Built-in |

### SQL Basics

SQL = Structured Query Language (how we talk to databases)

**SELECT - Get Data**:
```sql
-- Get all columns, all rows
SELECT * FROM flights;

-- Get specific columns
SELECT flight_id, speed FROM flights;

-- Filter with WHERE
SELECT * FROM flights WHERE speed > 900;

-- Sort results
SELECT * FROM flights ORDER BY speed DESC;

-- Limit results
SELECT * FROM flights LIMIT 10;

-- Count rows
SELECT COUNT(*) FROM flights;
```

**INSERT - Add Data**:
```sql
INSERT INTO flights (flight_id, speed, altitude)
VALUES ('UAL123', 850, 10000);
```

**UPDATE - Modify Data**:
```sql
UPDATE flights 
SET speed = 900 
WHERE flight_id = 'UAL123';
```

**DELETE - Remove Data**:
```sql
DELETE FROM flights WHERE flight_id = 'UAL123';
```

### Using MySQL from Python

```python
import mysql.connector

# Connect
conn = mysql.connector.connect(
    host="localhost",
    user="flightuser",
    password="flightpass",
    database="flight_anomaly"
)

# Create cursor
cursor = conn.cursor(dictionary=True)

# Execute query
cursor.execute("SELECT * FROM flights WHERE speed > 900")

# Get results
results = cursor.fetchall()  # All rows
# or
result = cursor.fetchone()   # One row

# Print results
for row in results:
    print(row["flight_id"], row["speed"])

# Close
cursor.close()
conn.close()
```

**Inserting Data Safely** (prevents SQL injection):
```python
# BAD - vulnerable to attacks
flight_id = "UAL123"
cursor.execute(f"SELECT * FROM flights WHERE flight_id = '{flight_id}'")

# GOOD - use placeholders
cursor.execute("SELECT * FROM flights WHERE flight_id = %s", (flight_id,))

# Insert with placeholders
sql = "INSERT INTO flights (flight_id, speed) VALUES (%s, %s)"
cursor.execute(sql, ("UAL123", 850))
conn.commit()  # Save changes
```

---

## Part 12: Understanding Flask & Web Development

### How Websites Work

```
┌─────────────┐                           ┌─────────────┐
│   BROWSER   │  1. Request website       │   SERVER    │
│             │  ──────────────────────>  │             │
│             │                            │             │
│             │  2. Send HTML response    │             │
│             │  <──────────────────────  │             │
└─────────────┘                           └─────────────┘
```

**Example**:
1. You type `google.com` in browser
2. Browser sends request to Google's server
3. Server sends back HTML/CSS/JavaScript
4. Browser displays the page

### Basic Flask App

```python
from flask import Flask

# Create app
app = Flask(__name__)

# Define route (URL)
@app.route("/")
def home():
    return "Hello, World!"

# Run server
if __name__ == "__main__":
    app.run(debug=True)
```

**What happens**:
1. Run the code: `py app.py`
2. Server starts at `http://127.0.0.1:5000`
3. Visit URL in browser
4. Browser requests "/"
5. Flask runs `home()` function
6. Returns "Hello, World!"
7. Browser displays it

### Routes with Parameters

```python
@app.route("/flight/<flight_id>")
def flight_details(flight_id):
    return f"Details for flight {flight_id}"

# Visiting /flight/UAL123 would show:
# "Details for flight UAL123"
```

### Rendering HTML Templates

**app.py**:
```python
from flask import render_template

@app.route("/")
def home():
    flights = ["UAL123", "DAL456", "AAL789"]
    return render_template("home.html", flights=flights)
```

**templates/home.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Flights</title>
</head>
<body>
    <h1>Flight List</h1>
    <ul>
        {% for flight in flights %}
            <li>{{ flight }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Result in browser**:
```
Flight List
• UAL123
• DAL456
• AAL789
```

### Understanding {{ }} and {% %}

- `{{ variable }}` - Print variable value
- `{% code %}` - Execute Python-like code (loops, if statements)

```html
<!-- Print variable -->
<h1>{{ title }}</h1>

<!-- If statement -->
{% if user_logged_in %}
    <p>Welcome back!</p>
{% else %}
    <p>Please log in</p>
{% endif %}

<!-- Loop -->
{% for item in items %}
    <p>{{ item }}</p>
{% endfor %}
```

---

## Part 13: Machine Learning Fundamentals

### What is Machine Learning?

**Traditional Programming**:
```
Input + Rules → Output

Example:
If temperature > 30°C → "It's hot"
```

**Machine Learning**:
```
Input + Output → Rules (learned by computer)

Example:
Give computer 1000s of temperature examples
Computer learns: "temperatures > ~30 usually called 'hot'"
```

### Types of Machine Learning

#### 1. Supervised Learning
**You provide**: Input + Correct Answer  
**Computer learns**: Pattern to predict answers

**Example**: Spam detection
- Training: Show emails labeled "spam" or "not spam"
- Computer learns patterns
- Now it can classify new emails

#### 2. Unsupervised Learning
**You provide**: Input only (no answers)  
**Computer finds**: Hidden patterns

**Example**: Customer grouping
- Training: Give customer data (age, purchases, etc.)
- Computer finds groups of similar customers
- You didn't tell it what groups to find!

#### 3. Anomaly Detection (Our Project Uses This!)
**Goal**: Find unusual/abnormal data points

**Visual**:
```
Normal points:  🟢🟢🟢🟢🟢🟢🟢
                🟢🟢🟢🟢🟢🟢🟢
                🟢🟢🟢🟢🟢🟢🟢

Anomaly:                      🔴
```

### Features in Machine Learning

**Features** = Input variables used for prediction

**Example - Predicting House Price**:
```python
Features                    Target (What we predict)
─────────                   ────────────────────────
• Square footage            
• Number of bedrooms    →   House Price: $500,000
• Age of house              
• Location                  
```

**In Our Project**:
```python
Features                    Target (What we predict)
─────────                   ────────────────────────
• speed                     
• altitude                  
• duration                →  Is it an anomaly?
• delay                       (Normal / Abnormal)
• delay_ratio               
• speed_per_min             
```

### Isolation Forest Algorithm (What We Use)

**How it works** (intuitive explanation):

Imagine trying to "isolate" each data point:

**Normal point**:
```
To isolate this point, you need many cuts:
🟢🟢🟢 | 🟢[THIS]🟢 | 🟢🟢🟢
│       │           │
Cut 1   Cut 2      Cut 3   (Many cuts needed)
```

**Anomaly point**:
```
To isolate this point, you need few cuts:
🟢🟢🟢🟢🟢                🔴[THIS]
│
Cut 1   (One cut!)
```

**Conclusion**: Anomalies are **easy to isolate** (few cuts needed)

### Training and Prediction

```python
from sklearn.ensemble import IsolationForest

# Step 1: Create model
model = IsolationForest(contamination=0.2)
# contamination = expected % of anomalies (20%)

# Step 2: Train on historical "normal" data
features = df[['speed', 'altitude', 'duration', 'delay']]
model.fit(features)

# Step 3: Predict on new data
new_flight = [[850, 10000, 180, 45]]  # One flight
prediction = model.predict(new_flight)

# Result:
#  1 = normal
# -1 = anomaly

if prediction[0] == -1:
    print("Anomaly detected!")
```

### Feature Engineering

**Feature Engineering** = Creating new features from existing ones to help the model learn better

**Example in our project**:
```python
# Original features
delay = 45       # minutes
duration = 180   # minutes

# Engineered feature (more meaningful)
delay_ratio = delay / duration  # 0.25 (25%)

# Why better?
# Model can now easily see "25% of flight was delay"
# rather than trying to figure out relationship between 45 and 180
```

**Another example**:
```python
speed = 850
duration = 180

# Engineered feature
speed_per_min = speed / duration  # 4.72

# Meaning: This flight travels 4.72 km per minute
# If this is very low, might indicate hovering or circling (problem!)
```

---

## Part 14: Understanding APIs

### What is an API?

**API** = Application Programming Interface  
**Simple definition**: A way for programs to talk to each other

**Real-world analogy**: Restaurant
- You (program) don't go to kitchen
- You tell waiter (API) what you want
- Waiter brings you food (data)

### REST APIs and HTTP Requests

**HTTP Methods**:
- **GET**: Retrieve data (like reading a book)
- **POST**: Send data (like mailing a letter)
- **PUT**: Update data
- **DELETE**: Remove data

**Example - OpenSky Network API**:

```python
import requests

# Make GET request to API
url = "https://opensky-network.org/api/states/all"
response = requests.get(url)

# Check if successful
if response.status_code == 200:
    data = response.json()  # Convert to Python dictionary
    print(data)
else:
    print("Error:", response.status_code)
```

### API Responses (JSON)

**JSON** = JavaScript Object Notation (looks like Python dictionary)

**Example API Response**:
```json
{
    "time": 1234567890,
    "states": [
        ["abc123", "UAL123", "US", 850, 10000],
        ["def456", "DAL456", "US", 920, 11000]
    ]
}
```

**In Python**:
```python
data = response.json()

# Access nested data
timestamp = data['time']
first_flight = data['states'][0]
flight_id = first_flight[1]  # "UAL123"
```

### Real Example from Project

```python
def fetch_live_flights():
    # API URL with geographic bounds
    URL = "https://opensky-network.org/api/states/all"
    URL += "?lamin=49.0&lomin=-2.0&lamax=52.0&lomax=1.0"
    
    try:
        # Send request
        response = requests.get(URL, timeout=10)
        data = response.json()
        
        # Check if data exists
        if 'states' not in data or data['states'] is None:
            return []
        
        # Process each flight
        flights = []
        for raw in data['states'][:10]:  # First 10
            callsign = raw[1].strip()
            altitude = raw[7]
            velocity = raw[9]
            
            if altitude is None or velocity is None:
                continue  # Skip incomplete data
            
            flights.append({
                'flight_id': callsign,
                'speed': velocity * 3.6,  # m/s to km/h
                'altitude': altitude
            })
        
        return flights
    
    except Exception as e:
        print(f"Error: {e}")
        return []
```

---

## Part 15: Putting It All Together

### How Our Project Works - Complete Flow

```
┌──────────────────────────────────────────────────────────────┐
│ STEP 1: TRAINING (One-time setup)                            │
│ File: ai_learn.py                                            │
├──────────────────────────────────────────────────────────────┤
│ 1. Load historical normal flights from CSV                   │
│ 2. Create engineered features (delay_ratio, speed_per_min)   │
│ 3. Train Isolation Forest model                              │
│ 4. Save results to final_ai_output.csv                       │
└──────────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────┐
│ STEP 2: DATABASE SETUP (One-time)                            │
│ Files: setup_database.sql, save_to_db.py                     │
├──────────────────────────────────────────────────────────────┤
│ 1. Create database and tables                                │
│ 2. Create user with permissions                              │
│ 3. Load initial data from CSV                                │
└──────────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────────┐
│ STEP 3: WEB DASHBOARD (Continuous)                           │
│ File: app.py                                                  │
├──────────────────────────────────────────────────────────────┤
│ 1. Flask server listens on port 5000                         │
│ 2. When user visits http://127.0.0.1:5000:                   │
│    a. Connect to database                                    │
│    b. Query flights table                                    │
│    c. Calculate statistics (total, anomalies, etc.)          │
│    d. Render HTML template with data                         │
│    e. Send to browser                                        │
└──────────────────────────────────────────────────────────────┘
                         
                    (Running in parallel ↓)
                         
┌──────────────────────────────────────────────────────────────┐
│ STEP 4: LIVE DATA STREAM (Continuous)                        │
│ File: stream_data.py                                         │
├──────────────────────────────────────────────────────────────┤
│ INFINITE LOOP:                                                │
│ 1. Fetch live flights from OpenSky API                       │
│ 2. For each flight:                                           │
│    a. Calculate engineered features                          │
│    b. Get AI prediction (IsolationForest)                    │
│    c. Apply human rules (delay checks, speed checks)         │
│    d. Calculate anomaly score                                │
│    e. Determine if anomaly (score >= 60)                     │
│    f. Build explanation string                               │
│    g. Insert into database                                   │
│ 3. Wait 10 seconds                                            │
│ 4. Repeat                                                     │
└──────────────────────────────────────────────────────────────┘
```

### Data Flow Diagram

```
LIVE FLIGHT DATA (OpenSky API)
        │
        │ fetch_live_flights()
        ↓
    [Raw JSON]
        │
        │ Parse & Extract
        ↓
    [Python Dicts]
    {id: UAL123, speed: 850, ...}
        │
        │ Feature Engineering
        ↓
    [Enhanced Features]
    {delay_ratio: 0.25, speed_per_min: 4.7}
        │
        ├─────────────┬─────────────┐
        │             │             │
        ↓             ↓             ↓
    [AI Model]   [Rule 1]      [Rule 2]
    Pattern?     delay>80%?    speed<700?
        │             │             │
        └──────┬──────┴─────────────┘
               │
               ↓
        [Combine Scores]
        AI(30) + Delay(40) = 70
               │
               ↓
        [Make Decision]
        70 >= 60? YES → Anomaly!
               │
               ↓
        [MySQL Database]
        INSERT INTO flights...
               │
               ↓
        [Flask Dashboard]
        SELECT * FROM flights...
               │
               ↓
        [Browser Display]
```

### Key Concepts Review

Here's what you now understand:

✅ **Variables** - Storing data  
✅ **Data Types** - int, float, str, bool  
✅ **Operators** - Math, comparison, logical  
✅ **Conditionals** - if/elif/else decisions  
✅ **Lists** - Ordered collections  
✅ **Dictionaries** - Key-value pairs  
✅ **Loops** - for and while repetition  
✅ **Functions** - Reusable code blocks  
✅ **Files** - Reading/writing data  
✅ **Databases** - SQL queries, connections  
✅ **Flask** - Web routes, templates  
✅ **Machine Learning** - Training, prediction, features  
✅ **APIs** - HTTP requests, JSON responses  
✅ **Integration** - Connecting all pieces

---

## 🎓 Final Practice Project

Create your own simplified version! This reinforces everything:

```python
# mini_flight_checker.py
import pandas as pd

# Step 1: Load some sample flights
flights = [
    {"id": "FL001", "speed": 850, "delay": 20, "duration": 120},
    {"id": "FL002", "speed": 600, "delay": 90, "duration": 100},
    {"id": "FL003", "speed": 920, "delay": 5, "duration": 150},
]

# Step 2: Analyze each flight
def analyze_flight(flight):
    score = 0
    reasons = []
    
    # Check delay ratio
    delay_ratio = flight["delay"] / flight["duration"]
    if delay_ratio > 0.5:
        score += 50
        reasons.append("High delay ratio")
    
    # Check speed
    if flight["speed"] < 700:
        score += 40
        reasons.append("Low speed")
    
    return score, reasons

# Step 3: Check all flights
print("FLIGHT ANALYSIS REPORT")
print("=" * 50)

for flight in flights:
    score, reasons = analyze_flight(flight)
    status = "ANOMALY" if score >= 60 else "NORMAL"
    
    print(f"\nFlight: {flight['id']}")
    print(f"Speed: {flight['speed']} km/h")
    print(f"Delay: {flight['delay']} min")
    print(f"Score: {score}")
    print(f"Status: {status}")
    if reasons:
        print(f"Reasons: {', '.join(reasons)}")

print("\n" + "=" * 50)
```

**Challenge**: Extend this to:
1. Read flights from a CSV file
2. Save results to a new CSV
3. Add more rules
4. Create a function to find the worst flight

---

## 🚀 You're Ready!

You now understand:
- How programming works from first principles
- Every line of code in this project
- How to modify and extend it
- The concepts to learn ANY programming project

**Next steps**:
1. Review sections you found tricky
2. Try the practice exercises
3. Modify the actual project
4. Build your own project!

**Remember**: Programming is learned by **doing**, not just reading. Make mistakes, break things, fix them - that's how you truly learn!

Happy coding! 🎉
