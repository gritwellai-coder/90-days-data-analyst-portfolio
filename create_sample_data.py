import pandas as pd
data = {
    'OrderID': [101,102,103,104],
    'Customer': ['Rahim', 'Karim', 'Sakib', 'Rina'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Amount': [1200, 25, 75, 300],
    'City': ['Dhaka', 'Khulna', 'Dhaka', 'Chittagong']
}

df = pd.DataFrame(data)
df.to_csv('economic_orders.csv', index=False)
print("CSV created: ecommerce_orders.csv")