import pandas as pd
df = pd.read_csv("2015_1.txt")
print(df)
total = 0

for i in range(1, len(df)):
    if df.Depth.iloc[i] > df.Depth.iloc[i-3]:
        total += 1
    else:
        total = total
print(total)
