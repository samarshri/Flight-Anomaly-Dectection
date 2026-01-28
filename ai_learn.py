import pandas as pd
from sklearn.ensemble import IsolationForest

# ----------------------------
# 1. Load flight data
# ----------------------------
print("Loading flight data...")
df = pd.read_csv("data/flights.csv")

# ----------------------------
# 2. Create smart features
# ----------------------------
print("Creating smart features...")
df['delay_ratio'] = df['delay'] / df['duration']
df['speed_per_min'] = df['speed'] / df['duration']

# ----------------------------
# 3. Prepare features for AI
# ----------------------------
features = df[['speed', 'altitude', 'duration', 'delay',
               'delay_ratio', 'speed_per_min']]

# ----------------------------
# 4. Train AI model
# ----------------------------
print("Training AI model...")
model = IsolationForest(contamination=0.2, random_state=42)

# AI output:  1 = normal, -1 = anomaly
df['ai_flag'] = model.fit_predict(features)

# Convert to human-friendly flag
# 1 = anomaly, 0 = normal
df['ai_flag'] = df['ai_flag'].map({1: 0, -1: 1})

# ----------------------------
# 5. Analyze ONE flight (rules + AI)
# ----------------------------
def analyze(row):
    score = 0
    reasons = []

    # Human rule: delay is too high
    if row['delay_ratio'] > 0.8:
        score += 40
        reasons.append("High delay")

    # Human rule: speed is too low
    if row['speed_per_min'] < 5:
        score += 30
        reasons.append("Low speed")

    # AI opinion
    if row['ai_flag'] == 1:
        score += 30
        reasons.append("ML detected abnormal pattern")

    return score, ", ".join(reasons)

def get_severity(score):
    if score >= 60:
        return "High"
    elif score >= 30:
        return "Medium"
    else:
        return "Low"

df[['anomaly_score', 'explanation']] = df.apply(
    lambda r: analyze(r), axis=1, result_type='expand'
)

df['severity'] = df['anomaly_score'].apply(get_severity)


# ----------------------------
# 7. Final decision
# ----------------------------
df['final_anomaly'] = (df['anomaly_score'] >= 60).astype(int)

# ----------------------------
# 8. Show final result
# ----------------------------
print("\nFinal AI result:")
print(df[['flight_id', 'anomaly_score', 'final_anomaly', 'explanation']])

df.to_csv("data/final_ai_output.csv",index=False)
