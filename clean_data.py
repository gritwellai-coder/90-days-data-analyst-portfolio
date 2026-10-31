import pandas as pd
df = pd.read_csv('messy_orders.csv')
print("BEFORE CLEANING")
print(df)

# Cleaning steps - 
df['Customer'] = df['Customer'].str.strip().str.title() # Remove spaces, proper case
df['City'] = df['City'].str.strip().str.title()
df['Amount'] = df['Amount'].replace('[\$,A-Z]', '', regex=True) # Remove $ and N/A
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce') # Convert to number
df = df.dropna(subset=['OrderId', 'Customer']) # Remove rows with no ID/name

print("\nAFTER Cleaning:")
print(df)
df.to_csv('cleaned_orders.csv', index=False)
print("\nSaved: cleaned_orders.csv - Ready for client!")