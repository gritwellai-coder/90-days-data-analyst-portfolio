import pandas as pd

df = pd.read_csv('messy_1000.csv')
print(f"Original: {len(df)} rows")
print(df['Amount'].describe())

# 1. Clean Amount - force numeric
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

# 2. Cap anythin > 1200 becomes 1200
df.loc[df['Amount'] > 1200, 'Amount'] = 1200

# 3. Fix City/Customer Nulls
df['City'] = df['City'].fillna('Unknown')
df['Customer'] = df['Customer'].fillna('Unknown')

# 4. Fix Amount 0 and Null > median
median_amt = df[df['Amount'] > 0]['Amount'].median()
print(f"Medaian: {median_amt}")
df['Amount'] = df['Amount'].fillna(median_amt)
df.loc[df['Amount'] == 0, 'Amount'] = median_amt

# 5. Remove duplicate OrderId
df = df.drop_duplicates(subset=['OrderId'], keep='first')

print(f"Cleaned: {len(df)} rows")
print(f"Max: {df['Amount'].max()}, Min: {df['Amount'].min()}, Nulls left: {df.isnull().sum().sum()}")
df.to_csv('cleaned_1000_v2.csv')
print("Saved to cleaned_1000_v2.csv")