import pandas as pd
df = pd.read_csv('cleaned_1000_v2.csv')
df['City'] = df['City'].str.strip().str.title()
df.to_csv('cleaned_1000_v2.csv', index=False)
print(df['City'].value_counts().head())
