USE freelance_db;

# 1. RANK cities by total sales
SELECT City, SUM(Amount) as total, RANK() OVER (ORDER BY SUM(Amount) DESC) as city_rank
FROM cleaned_1000_v2 GROUP BY City ORDER BY total DESC;

# 2. ROW_NUMBER - Top orders per city
SELECT City, OrderId, Amount, ROW_NUMBER() OVER (PARTITION BY City ORDER BY Amount DESC) as rn FROM cleaned_1000_v2;

# 3. LAG - Compare to previous order in same city 
SELECT OrderId, City, Amount, LAG(Amount) OVER (PARTITION BY City ORDER BY OrderId) as prev_amount,
Amount - LAG(Amount) OVER (PARTITION BY City ORDER BY OrderId) as diff
FROM cleaned_1000_v2 WHERE City='Dhaka' ORDER BY OrderId;

# 4. Running total per city
SELECT OrderId, City, Amount, SUM(Amount) OVER (PARTITION BY City ORDER BY OrderId ROWS UNBOUNDED PRECEDING) as running_total
FROM cleaned_1000_v2 WHERE City='Dhaka' ORDER BY OrderId;