import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Get data from MySQL using python - Integration
engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df = pd.read_sql('SELECT * FROM orders', con=engine)

# Dashboard 1: Sales by City
plt.figure(figsize=(8,4))
df.groupby('City')['Amount'].sum().plot(kind='bar', color='skyblue')
plt.title('Sales by City - Client Dashboard')
plt.ylabel('Total Sales $')
plt.savefig('sales_by_city.png')
print("Dashboard saved: sales_by_city.png")

# Dashboard 2: Sales by Product
plt.figure(figsize=(8,4))
df.groupby('Product')['Amount'].sum().plot(kind='bar',color='orange')
plt.title('Sales by Product')
plt.savefig('sales_by_product.png')
print("Dashboard saved: sales_by_product.png")
