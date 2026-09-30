-- 14. Sort all products by price in ascending order.

SELECT price
FROM products
ORDER BY price ASC

-- 15. Sort all products by price in descending order.
SELECT price
FROM products
ORDER BY price DESC


-- 16. Sort customers by country (A–Z), then by last name (A–Z).
SELECT country, last_name
FROM customers
ORDER BY country ASC, last_name ASC

-- 17. Get the top 5 most expensive products.
SELECT product_name, price
FROM products 
ORDER BY price DESC LIMIT 5

-- 18. Get products ranked 6th to 10th by price (pagination).
SELECT product_name, price
FROM products 
ORDER BY price ASC LIMIT 5, 5;

-- 19. List all unique countries from the customers table.
SELECT DISTINCT(country)
FROM customers 
ORDER BY country ASC

-- 20. List all unique combinations of country and city.
SELECT DISTINCT country, city
FROM customers 
ORDER BY country ASC, city ASC;

-- 21. Count the total number of customers.
SELECT COUNT(*)
FROM customers

-- 22. Count how many customers have a non-null email.
SELECT COUNT(*)
FROM customers
WHERE email is NOT NULL
-- 23. Find the total revenue from all orders.
SELECT SUM(total_amount)
FROM orders

-- 24. Find the average price of all products.
SELECT AVG(price)
FROM products

-- 25. Find the cheapest and most expensive product prices.
SELECT  
MIN(price) AS min_price,
MAX(price) AS max_price
FROM products

-- 26. Find the average product price rounded to 2 decimals.
SELECT ROUND(AVG(price), 2)
from products

-- 27. Get the count, average, minimum, and maximum price of products in one result.
SELECT  
MIN(price) AS min_price,
MAX(price) AS max_price,
COUNT(*) AS count,
ROUND(AVG(price)) as avg_price
FROM products

-- 28. Count how many customers exist per country.
SELECT country, COUNT(*) AS customer_count
FROM customers
GROUP BY country;

-- 29. For each product category, show count of products, average price, and total stock.

SELECT 
    category AS product_category,
    COUNT(product_name) AS product_count,
    ROUND(AVG(price)) AS avg_price,
    SUM(stock_quantity) AS total_stock
FROM products
GROUP BY category;


-- 30. Show only countries that have more than 5 customers.
SELECT country
FROM customers
GROUP BY country HAVING COUNT(*) > 5