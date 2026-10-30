import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('economic_orders.csv')
print("CSV Read:")
print(df)

engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df.to_sql('orders', con=engine, if_exists='replace',index=False)
print("\nSUCCESS: Data loaded t MySQL table 'orders' ")

