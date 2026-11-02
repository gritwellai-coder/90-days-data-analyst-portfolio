import pandas as pd
import pymysql
df = pd.read_csv('cleaned_1000_v2.csv')
df = df.dropna(subset=['OrderId'])
conn = pymysql.connect(host='localhost', user='root', password='2534', database='freelance_db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS cleaned_1000_v2")
cursor.execute("CREATE TABLE cleaned_1000_v2 (OrderId INT, Customer VARCHAR(255), City VARCHAR(255), Amount DOUBLE)")
for _, row in df.iterrows():
    cursor.execute("INSERT INTO cleaned_1000_v2 VALUES (%s,%s,%s,%s)", (int(row['OrderId']), str(row['Customer']), str(row['City']), float(row['Amount'])))
conn.commit()
cursor.execute("SELECT COUNT(*), MAX(Amount) FROM cleaned_1000_v2")
print(cursor.fetchone())