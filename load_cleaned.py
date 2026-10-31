import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df = pd.read_csv('cleaned_orders.csv')
print(df)
df.to_sql('cleaned_orders', con=engine, if_exists='replace', index=False)
print("Cleaned data loaded to MySQL table 'cleaned_orders'")