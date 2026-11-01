import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df = pd.read_csv('cleaned_1000.csv')
print(f"Loading {df.shape[0]} clean rows to MySQL")

df.to_sql('cleaned_1000', con=engine, if_exists='replace', index=False)
print("Loaded to MySQL table: cleaned_1000")

# Verify
result = pd.read_sql("SELECT City, COUNT(*) as Orders, SUM(Amount) as Total_Sales FROM cleaned_1000 GROUP BY City", con=engine)
print("\nVerification - Sales by City from MySQL")
print(result)