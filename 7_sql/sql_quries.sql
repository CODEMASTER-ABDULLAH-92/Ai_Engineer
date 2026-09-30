CREATE DATABASE test;
USE test;


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50),
    signup_date DATE
);


CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    manager_id INT,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

-- ========================
-- Filtering 
-- ========================

-- 1. Retrieve all columns from the `customers` table.

SELECT * 
FROM customers;

SELECT * 
FROM customers WHERE 1;




-- Get only `first_name`, `last_name`, and `email` of all customers

SELECT first_name, last_name, email
FROM customers;


-- List all customers who live in the 'USA'.
SELECT *
FROM customers
WHERE country = 'USA';

-- Find all customers from 'USA' who live in 'New York'.
SELECT * 
FROM customers
WHERE country = 'USA' and city = 'New York';


-- 5. Get all customers who are from either 'USA' or 'Canada'.

SELECT *
FROM customers
WHERE country = 'USA'
or country = 'Canada';

SELECT * 
FROM customers
WHERE country IN ('USA', 'Canada')



-- List all customers who are NOT from 'USA'.
SELECT *
FROM customers
WHERE country NOT IN ('USA')


-- Find all customers from 'USA', 'UK', or 'Germany'.
SELECT *
FROM customers
WHERE country IN ('USA', 'UK', 'Germany')



-- Get all products whose price is between 20 and 100.
SELECT *
FROM products
WHERE price BETWEEN 20 AND 100;

-- Find all customers whose email ends with `@gmail.com`.

SELECT * 
FROM customers
WHERE email LIKE '%@gmail.com'


-- List all products whose name starts with the letter 'S'.
SELECT *
FROM products
WHERE name LIKE 'S%'

-- Find all products whose name contains the word 'phone'.
SELECT *
FROM products
WHERE name LIKE '%phone%'

-- Get all customers whose email is NULL.
SELECT *
FROM customers
WHERE email IS NULL;

-- List all customers whose email is NOT NULL.

SELECT *
FROM customers
WHERE email IS NOT NULL




-- ========================
-- AGGREGATES 
-- ========================

--COUNT Problems

-- 1. Count the total number of customers.
SELECT COUNT(*)
FROM customers

-- 2. Count the total number of products.
SELECT COUNT(*)
FROM products

3. Count the total number of orders.
SELECT COUNT(*)
FROM orders

4. Count how many customers have a non-NULL email.
SELECT COUNT(*)
FROM customers
WHERE email IS NOT NULL

5. Count how many customers have a NULL email.
SELECT COUNT(*)
FROM customers
WHERE email IS NULL

6. Count the number of unique countries in the customers table.
SELECT COUNT(DISTINCT country)
FROM customers

7. Count the number of unique categories in the products table.

SELECT COUNT(DISTINCT category)
FROM products


8. Count the number of unique order statuses.
SELECT COUNT(DISTINCT status)
FROM orders

9. Count the number of orders that have status 'Completed'.
SELECT COUNT(*)
FROM orders
WHERE status = 'Completed'

10. Count the number of orders that are NOT 'Completed'.
SELECT COUNT(*)
FROM orders
WHERE status != 'Completed'








-- ==================================
-- Pending 
-- ================================
-- These questions are pending needs the joins and other concepts

11. Count the number of distinct customers who have placed at least one order.
12. Count the number of distinct products that have been ordered at least once.
13. Count the number of products that have never been ordered.
14. Count the number of customers who have never placed an order.
15. Count how many employees have a manager (non-NULL manager_id).

















-- =============================
-- SUM Problems
-- =============================

-- 16. Find the total revenue from all orders.
SELECT SUM(total_amount)
FROM orders
-- 17. Find the total revenue only from 'Completed' orders.
SELECT SUM(total_amount)
FROM orders
WHERE status = 'Completed'
-- 18. Find the total revenue from 'Cancelled' orders.
SELECT SUM(total_amount)
FROM orders
WHERE status = 'Cancelled'

-- 19. Find the total stock quantity across all products.
SELECT SUM(stock_quantity)
FROM products
-- 20. Find the total quantity of items sold across all order_items.
SELECT SUM(quantity)
FROM order_items
-- 21. Find the total amount spent by customer_id = 1.
SELECT SUM(total_amount)
FROM orders
WHERE customer_id = 1
-- 22. Find the total salary paid to all employees.
SELECT SUM(salary)
from employees
-- 23. Find the total salary paid in the 'Sales' department.
SELECT SUM(salary)
from employees
WHERE department = 'Sales'
-- 24. Find the total sales made in the year 2023.
SELECT SUM(total_amount)
from orders
WHERE YEAR(order_date) = 2023
-- 25. Find the total sales made in the year 2024.

SELECT SUM(total_amount)
from orders
WHERE YEAR(order_date) = 2024


-- ### AVG Problems
-- 26. Find the average price of all products.
SELECT AVG(price)
FROM products
-- 27. Find the average price of products in the 'Electronics' category.
SELECT AVG(price)
FROM products
WHERE category = 'Electronics'
-- 28. Find the average total_amount of all orders.
SELECT AVG(total_amount)
FROM orders
-- 29. Find the average total_amount of only 'Completed' orders.
SELECT AVG(total_amount)
from orders
WHERE status = 'Completed'
-- 30. Find the average salary of all employees.



SELECT AVG(salary)
from employees
-- 31. Find the average salary in the 'Sales' department.

SELECT AVG(salary)
from employees
WHERE department = 'Sales'
-- 32. Find the average stock_quantity across all products.
SELECT AVG(stock_quantity)
FROM products
-- 33. Find the average quantity ordered per order_item.
SELECT AVG(quantity)
FROM order_items;
-- 34. Find the average unit_price across all order_items.
SELECT AVG(unit_price)
FROM order_items

-- Pending 
-- 35. Find the average order value per customer (overall, not per customer).



-- MIN / MAX Problems
-- 36. Find the cheapest product price.
SELECT MIN(price)
FROM products
-- 37. Find the most expensive product price.
SELECT MAX(price)
FROM products
-- 38. Find the product name of the cheapest product.
SELECT product_name
FROM products
WHERE price = (SELECT MIN(price) FROM products)
-- 39. Find the product name of the most expensive product.

SELECT product_name
FROM products
WHERE price = (SELECT MAX(price) 
FROM products)



-- These questions are also pending 



-- 40. Find the earliest order date.
-- 41. Find the latest order date.
-- 42. Find the lowest salary in the employees table.
-- 43. Find the highest salary in the employees table.
-- 44. Find the minimum total_amount in the orders table.
-- 45. Find the maximum total_amount in the orders table.

-- =================
-- Sorting 
-- =================
