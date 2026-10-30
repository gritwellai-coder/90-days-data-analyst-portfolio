import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df = pd.read_sql("SELECT City, Amount, RANK() OVER(ORDER BY Amount DESC) as Sales_Rank FROM orders",con=engine)
print(df)
df.to_csv('ranked_sales.csv', index=False)
print("Saved: ranked_sales.csv - Ready for dashboard")