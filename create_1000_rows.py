import pandas as pd 
import random
cities = ['Dhaka', 'Khulna', 'Chittagong', 'Rajshahi', '  dhaka  ', 'KHULNA', None]
customers = ['Rahim', 'Karim', 'Sakib', '  rina  ', 'ANIKA', None]
data = []
for i in range(1000):
    data.append({
        'OrderId': 1000+i if random.random()>0.05 else None,
        'Customer': random.choice(customers),
        'City': random.choice(cities),
        'Amount': random.choice([25, 75, 300, 1200, '25$', 'N/A', None, 5000])
    })
df = pd.DataFrame(data)
df.to_csv('messy_1000.csv',index=False)
print(f"Created 1000 rows: {df.shape}")
print(df.head(10))
print(f"Nulls: {df.isnull().sum().to_dict()}")