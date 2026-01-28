# 📄 Deep Dive: ai_learn.py (The "Brain")

**Role**: The Logical Core. This script covers the entire Pipeline: Read Data -> Train AI -> Judge Flights -> Save Results. It is the "Offline" version of `stream_data.py`.

## Key Sections Explained

### 1. Feature Selection (Line 20)
```python
features = ['speed', 'altitude', 'duration', 'delay_ratio'...]
```
*   **Columns that matter**: The AI doesn't care about `flight_id` (names don't affect safety). It only cares about *physics*.
*   We filter the data to only include these numerical columns for the "Learning" phase.

### 2. Isolation Forest (Line 27)
```python
model = IsolationForest(contamination=0.2, random_state=42)
```
*   **Data Science Magic**:
    *   `IsolationForest`: Imagine cutting a cake. Identifying a raisin is easy (isolate it with 1 cut). Identifying a specific crumb of flour is hard (needs many cuts). This algorithm assumes "Anomalies are easier to isolate".
    *   `contamination=0.2`: We tell the AI "Assume roughly 20% of the flights are weird". This sets the sensitivity threshold.
    *   `random_state=42`: Computers use "Random" numbers. Setting a "Seed" (42) makes the randomness the *same* every time, so you get reproducible results.

### 3. Prediction & Mapping (Line 30-34)
```python
df['ai_flag'] = model.fit_predict(features)
df['ai_flag'] = df['ai_flag'].map({1: 0, -1: 1})
```
*   `fit_predict`: Trains AND Judges at the same time.
*   **The Switch**:
    *   Scikit-Learn library says: 1 = Good, -1 = Bad.
    *   Humans usually think: 0 = Normal, 1 = Flag/Alert.
    *   The `.map()` function flips these numbers so they make sense for our dashboard (1 means "Danger").

### 4. The `analyze` Function (Line 39-58)
```python
def analyze(row):
    if row['delay_ratio'] > 0.8: ...
```
*   **Explainable AI (XAI)**:
    *   It's not enough to say "flight is bad". We need to know *why*.
    *   This function builds a text explanation (`reasons.append("High delay")`).
    *   This text ends up in the "Explanation" column on your dashboard, helping the human security officer understand the AI's decision.
