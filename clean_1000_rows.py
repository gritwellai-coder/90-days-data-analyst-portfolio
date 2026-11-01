import pandas as pd 
df = pd.read_csv('messy_1000.csv')
print(f"BEFORE: {df.shape}")
print(f"Nulls BEFORE: {df.isnull().sum().to_dict()}")

# Step 1: Clean strings
df['Customer'] = df['Customer'].astype(str).str.strip().str.title()
df['City'] = df['City'].astype(str).str.strip().str.title()

# Step 2: Clean Amount
df['Amount'] = df['Amount'].astype(str).replace('[\$,A-Z]', '', regex=True)
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

# Step 3: Remove rows with no OrderId
df = df.dropna(subset=['OrderId'])

# Step 4: Handle Duplicates
df = df.drop_duplicates(subset=['OrderId'], keep='first')

# Step 5: Handle Outliers
median_amount = df['Amount'].median()
print(f"Median Amount: {median_amount}")
df['Amount'] = df['Amount'].clip(upper=1200)

# Step 6: Fill remaining nulls with 0 or Unknown
df['Customer'] = df['Customer'].replace('None', 'Unknown').replace('Nan', 'Unknown')
df['City'] = df['City'].replace('None', 'Unknown').replace('Nan', 'Unknown')
df['Amount'] = df['Amount'].fillna(0)

print(f"\nAFTER: {df.shape}")
print(f"Nulls AFTER: {df.isnull().sum().to_dict()}")
print(df.head())

df.to_csv('cleaned_1000.csv', index=False)
print("\nSaved: cleaned_1000.csv -Ready for client!")

# Step 7 Summary stats - what clients love
print(f"\nSales by City: \n{df.groupby('City')['Amount'].sum()}")