import pandas as pd
import matplotlib.pyplot as plt 
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:2534@localhost/freelance_db')
df = pd.read_sql("SELECT City, SUM(Amount) as Total_Sales FROM cleaned_1000 GROUP BY City", con=engine)
df.plot(kind='bar', x='City', y='Total_Sales', color='orange')
plt.title('Day 8 - M4 Mac - 1000 Rows Sales by City - Cleaned')
plt.savefig('dashboard_1000_M4.png')
print("Dashboard saved: dashboard_1000_M4.png")