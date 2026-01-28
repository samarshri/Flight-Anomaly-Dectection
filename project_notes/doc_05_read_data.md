# 📄 Deep Dive: read_data.py (The "Hello World" of Data)

**Role**: A simple utility script. It demonstrates how to open a file and do basic math on it using Python. It doesn't talk to the database or the live internet. Use this to test your data logic.

## Key Sections Explained

### 1. Loading Data (Line 5)
```python
import pandas as pd
df = pd.read_csv("data/flights.csv")
```
*   **`pd.read_csv`**: This is the most common command in Data Science. It takes a text file (Comma Separated Values) and turns it into a **DataFrame** (`df`).
*   **DataFrame**: Think of this as a programmable Excel spreadsheet that lives in your computer's memory.

### 2. Feature Engineering (Line 11-12)
```python
df['delay_ratio'] = df['delay'] / df['duration']
df['speed_per_min'] = df['speed'] / df['duration']
```
*   **Smart Features**: Raw data isn't always enough.
    *   Example: A 10-minute delay on a 1-hour flight is annoying (16%). A 10-minute delay on a 10-hour flight is nothing (1.6%).
    *   By dividing `delay / duration`, we create a *new* number (`delay_ratio`) that represents the "Annoyance Factor" much better than raw minutes.
    *   **Lesson**: Good AI starts with good math, not just raw data.

### 3. Printing (Line 15)
```python
print(df)
```
*   Shows the table in your terminal. Useful for debugging to check "Did my math work?".
