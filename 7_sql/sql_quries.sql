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

-- =================
-- Sorting 
-- =================
