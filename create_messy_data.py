import pandas as pd
import numpy as np
data = {
    'OrderId': [101, 102, None, 104, 105, 106, 107],
    'Customer': [' rahim ', 'KARIM', 'Sakib', None, 'Rina', '  anika  ', 'Rahim' ],
    'Amount': ['1200', '25$', '75', '300', 'N/A', '1200', '25$'],
    'City': ['Dhaka', 'khulna', 'DHAKA', 'Chittagong', 'Dhaka', None, 'Khulna'],
    'OrderDate': ['2024-01-01', '01/02/2024', '2024.03.01', '2024-01-04', None, '2024-01-06', '2024-01-07']
}
df = pd.DataFrame(data)
df.to_csv('messy_orders.csv', index=False)
print("Messy file creatd - Like real client file!")
print(df)