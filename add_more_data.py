import pandas as pd
from sqlalchemy import create_engine
data = {
    'OrderID': [105,106,107,108,109,110],
    'Customer': ['Rahim', 'Karim', 'Anika', 'Rina', 'Sakib', 'Anika'],
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Laptop', 'Mouse'],
    'Amount': [1200, 25, 300, 75, 1200, 25],
    'City': ['Dhaka', 'Khulna', 'Dhaka', 'Chittagong', 'Dhaka', 'Dhaka']
}

df = pd.DataFrame(data)
engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df.to_sql('orders', con=engine, if_exists='append', index=False)
print("6 more orders added!")
