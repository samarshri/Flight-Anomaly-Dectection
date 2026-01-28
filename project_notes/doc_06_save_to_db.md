# 📄 Deep Dive: save_to_db.py (The "Loader")

**Role**: The Batch Uploader. It takes the results from the AI (CSV) and pushes them into the Database (MySQL). In the V2 real-time system, `stream_data.py` does this automatically, but this script is great for learning how databases work.

## Key Sections Explained

### 1. Cleaning Data (Line 7-17)
```python
def clean(val):
    if pd.isna(val) or val == "nan":
        return None
    return val
```
*   **The Problem**: Python uses `NaN` (Not a Number) for empty empty cells. MySQL uses `NULL`. They are not easier compatible. If you send `NaN` to MySQL, it crashes.
*   **The Fix**: This "Janitor Function" checks every single value. If it's a dirty `NaN`, it swaps it for a clean `None` (which MySQL understands as NULL).

### 2. Table Creation (Line 43-54)
```python
CREATE TABLE IF NOT EXISTS flights (...)
```
*   **Safety First**: Before we save data, we make sure the bucket (Table) exists.
*   `IF NOT EXISTS`: This prevents the script from crashing if you run it twice. It silently skips creation if the table is already there.

### 3. The Loop & Insert (Line 64-83)
```python
for _, row in df.iterrows():
    sql = "INSERT INTO flights VALUES (%s, ...)"
    cursor.execute(sql, (...))
```
*   **Iteration**: We go through the spreadsheet one row at a time.
*   **`%s` (Placeholders)**: We never write `VALUES (` + row['speed'] + `)`. That is dangerous (SQL Injection risk).
*   **Tuples**: `values = (clean(row['id']), ...)` creates a "package" of data that matches the `%s` slots.

### 4. Committing (Line 88)
```python
conn.commit()
```
*   **The Save Button**: SQL implies "Draft Mode" by default. Nothing is actually saved until you shout `commit()`. If you forget this line, your script runs without error, but the database remains empty!
