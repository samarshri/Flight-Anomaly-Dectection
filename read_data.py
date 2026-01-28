import pandas as pd

print("Reading flight data...")

df = pd.read_csv("data/flights.csv")

print("\nOriginal data:")
print(df)

#smart features
df['delay_ratio']=df['delay']/df['duration']
df['speed_per_min']=df['speed']/df['duration']

print("after adding smart features:")
print(df)
