-- 31. Show each product category with its average price.
SELECT category,
ROUND(AVG(price)) as avg_price
FROM products
GROUP BY category

-- 32. For each country, show the number of customers, sorted by count descending.
SELECT country,
       COUNT(*) AS number_of_customers
FROM customers
GROUP BY country
ORDER BY number_of_customers DESC;

-- 33. For each order status, show the count of orders and total revenue.
SELECT status,
    COUNT(*) AS count_of_orders,
    SUM(total_amount) AS total_amount
FROM orders
GROUP BY status

-- 34. Show categories where the average product price is above 100.
SELECT category 
ROUND(AVG(price)) as avg_price
FROM products
GROUP BY category 
HAVING avg_price > 100

-- 35. Show countries that have at least 3 customers AND average order value above 200.
SELECT country,
ROUND(AVG(total_amount)) AS avg_price
FROM customers
GROUP BY country
HAVING COUNT(*) > 3 AND avg_price > 200

-- 36. For each customer, count how many orders they placed.
SELECT 
-- 37. For each product, find the total quantity sold across all orders.
-- 38. Show each year and total sales made in that year.
-- 39. Show each month (across all years) and total sales in that month.
-- 40. Find categories that have more than 10 products in stock.
-- 41. For each city, find the number of customers and sort by count descending, showing only cities with more than 2 customers.
-- 42. Show each order status with its average order value, only where average > 100.
-- 43. For each employee department, show the count of employees and average salary.
-- 44. Show departments where the total salary exceeds 500,000.
-- 45. For each product category, show min price, max price, and the price range (max − min).
