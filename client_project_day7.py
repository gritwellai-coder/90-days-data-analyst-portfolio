import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

print("=== CLEINT PROJECT DAY 7 - Mac ===")

# Step 1: Read messy client file 
df = pd.read_csv('messy_orders.csv')
print("\n1. Raw Client File: ")
print(df.head())

# Step 2: Clean it
df['Customer'] = df['Customer'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()
df['Amount'] = df['Amount'].replace('[\$,A-Z]', '', regex=True)
df['Amount'] = pd.to_numeric(df['Amount'],errors='coerce')
df = df.dropna(subset=['OrderId', 'Customer'])
df['Amount'] = df['Amount'].fillna(0)

print("\n2. Cleaned File:")
print(df.head())

# Step 3: Load to MySQL
engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df.to_sql('client_project_final', con=engine, if_exists='replace',index=False)
print("\n3. Loaded to MySQL table: client_project_final")

# Step 4: Analyze with SQL via Python
result = pd.read_sql("SELECT City, SUM(Amount) as Total_Sales FROM client_project_final GROUP BY City", con=engine)
print("\n4. Analysis - Sales by City:")
print(result)

# Step 5 Dashboard
plt.figure(figsize=(8,4))
result.plot(kind='bar', x='City', y='Total_Sales', color='purple')
plt.title('Client Project Day 7 - Sales by City - Mac')
plt.savefig('client_project_dashboard_day7.png')
print("\n5. Dashboard saved: client_project_dashboard_day7.png")
print("\n=== PROJECT COMPLETE - READY TO SEND TO CLIENT ===")