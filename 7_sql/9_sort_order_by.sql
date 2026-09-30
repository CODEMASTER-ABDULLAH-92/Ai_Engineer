-- ==============================
-- ORDER BY in SQL
-- ==============================

-- ORDER BY is used to sort the result rows of a query.
-- Think of it like arranging data in a specific order.

-- "highest"       → DESC
-- "largest"       → DESC
-- "most expensive"→ DESC
-- "newest"        → DESC
-- "latest"        → DESC
-- "top"           → DESC

-- "lowest"        → ASC
-- "smallest"      → ASC
-- "cheapest"      → ASC
-- "oldest"        → ASC
-- "earliest"      → ASC
-- "bottom"        → ASC



-- | Question says        | Think                                 |
-- | -------------------- | ------------------------------------- |
-- | highest              | ORDER BY ... DESC                   |
-- | lowest               | ORDER BY ... ASC                    |
-- | largest              | ORDER BY ... DESC                   |
-- | smallest             | ORDER BY ... ASC                    |
-- | maximum              | ORDER BY ... DESC                   |
-- | minimum              | ORDER BY ... ASC                    |
-- | most expensive       | ORDER BY price DESC                 |
-- | cheapest             | ORDER BY price ASC                  |
-- | oldest               | ORDER BY date ASC                   |
-- | newest               | ORDER BY date DESC                  |
-- | latest               | ORDER BY date DESC                  |
-- | earliest             | ORDER BY date ASC                   |
-- | top                  | usually ORDER BY ... DESC + LIMIT |
-- | bottom               | usually ORDER BY ... ASC + LIMIT  |
-- | alphabetical         | ORDER BY name ASC                   |
-- | reverse alphabetical | ORDER BY name DESC                  |

-- Basic syntax


SELECT *
FROM products
ORDER BY price;


-- By default, SQL sorts in ascending order (ASC).

-- Ascending — smallest to largest

SELECT *
FROM products
ORDER BY price ASC;

-- Descending — largest to smallest


SELECT *
FROM products
ORDER BY price DESC;



-- You can also sort by text:


SELECT *
FROM customers
ORDER BY name ASC;
This sorts names alphabetically.

-- Important: ORDER BY does not change the actual data in the table. It only changes the order in which the result is displayed.

select model, screen_size
from health_app.smartphones
where brand_name = 'apple'
order by screen_size desc limit 5;

select model, num_front_cameras + num_rear_cameras AS 'total_cameras'
from smartphones 
order by total_cameras desc;


select model, 
round(sqrt(resolution_width * resolution_width + resolution_height + resolution_height) / screen_size) as 'ppi'
from smartphones
order by ppi desc;







select model, battery_capacity
from smartphones 
order by battery_capacity desc limit 1,1

-- At here the the first digit says how many rows i left 
-- and second digit says how many rows i print 
-- if the limit is like this 
-- limit 5, 10

-- then the 0,1,2,3,4 is left and printing start from 5 and stop after the 10 rows 

limit 1,1


-- =====================================================
-- LIMIT in SQL
-- =====================================================

-- LIMIT is used to control how many rows are returned.

-- Syntax:
-- LIMIT offset, count

-- offset = number of rows to skip
-- count  = number of rows to return/print

-- Example:
LIMIT 1, 1;

-- Skip 1 row, then return 1 row.
-- If rows are ordered:
-- Row 0 → skipped
-- Row 1 → returned

-- Example:
LIMIT 5, 10;
-- LIMIT 5, 1 means "skip 5 rows and return 1 row",
-- Skip the first 5 rows:
-- 0, 1, 2, 3, 4
-- Then return the next 10 rows:
-- 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

-- Common examples:
LIMIT 0, 1;   -- Return the 1st row
LIMIT 1, 1;   -- Return the 2nd row
LIMIT 2, 1;   -- Return the 3rd row
LIMIT 5, 10;  -- Skip 5, return 10 rows



-- 2nd lowest battery_capacity phone 

select model, battery_capacity
from smartphones 
order by battery_capacity ASC limit 1,1



SELECT model, rating
FROM smartphones
WHERE brand_name = 'apple'
ORDER BY rating ASC LIMIT 1



-- Sort the two columns
SELECT * 
FROM smartphones
ORDER BY brand_name ASC, price DESC













-- =====================================================
-- GROUP BY
-- =====================================================


-- GROUP BY is used to logically group rows
-- that have the same value.

-- Wherever a column contains repeated values
-- that can define groups, we can use GROUP BY.

-- Examples:
-- department
-- category
-- brand_name
-- customer_id
-- city
-- etc.


-- GROUP BY does NOT create permanent physical groups.
-- It only creates logical groups during the query.
-- The original table remains unchanged.



-- =====================================================
-- WHAT DOES GROUP BY DO?
-- =====================================================

-- Suppose we have:

-- Department
-- ----------------
-- IT
-- IT
-- HR
-- HR
-- Sales
-- Sales
-- Sales

-- GROUP BY department logically creates:

-- IT     → 2 rows
-- HR     → 2 rows
-- Sales  → 3 rows


-- Then an aggregate function can calculate
-- something for each group.

-- GROUP BY       → creates logical groups
-- Aggregate      → calculates something for each group



-- =====================================================
-- AGGREGATE FUNCTIONS WITH GROUP BY
-- =====================================================

-- COUNT() → counts rows
-- SUM()   → adds values
-- AVG()   → calculates average
-- MAX()   → finds maximum value
-- MIN()   → finds minimum value



-- Example:

-- How many employees are in each department?

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;


-- Example:

-- What is the average salary per department?

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;


-- Example:

-- What is the total sales for each category?

SELECT category, SUM(total_amount) AS total_sales
FROM orders
GROUP BY category;



-- =====================================================
-- BIGGEST CLUES FOR GROUP BY
-- =====================================================

-- When reading a SQL question, look for:

-- each
-- per
-- every
-- by
-- for each


-- Examples:

-- How many employees are in EACH department?
-- What is the average salary PER department?
-- Calculate separately for EVERY department?
-- What is the total sales for EACH category?
-- What is the average product price for EACH category?
-- What is the maximum price in EACH category?


-- =====================================================
-- MENTAL MODEL
-- =====================================================

-- Question:
-- How many employees are in each department?

-- "each department"
--       ↓
-- GROUP BY department
--       ↓
-- COUNT(*)
--       ↓
-- count employees inside each department



-- =====================================================
-- GROUP BY WITH MULTIPLE AGGREGATES
-- =====================================================

SELECT
    brand_name,
    COUNT(*) AS num_phones,
    ROUND(AVG(price)) AS avg_price,
    MAX(rating) AS max_rating,
    ROUND(AVG(screen_size), 2) AS avg_screen_size,
    ROUND(AVG(battery_capacity), 2) AS avg_battery_capacity
FROM smartphones
GROUP BY brand_name
ORDER BY num_phones DESC
LIMIT 15;



-- =====================================================
-- GROUP BY WITH has_nfc
-- =====================================================

SELECT
    has_nfc,
    AVG(price) AS avg_price,
    AVG(rating) AS avg_rating
FROM smartphones
GROUP BY has_nfc;


-- This creates groups such as:

-- has_nfc = True
-- has_nfc = False

-- Then AVG() is calculated separately
-- for each group.



-- =====================================================
-- GROUP BY WITH has_5g
-- =====================================================

SELECT
    has_5g,
    AVG(price) AS avg_price,
    AVG(rating) AS avg_rating
FROM smartphones
GROUP BY has_5g;



-- =====================================================
-- GROUP BY ON TWO COLUMNS
-- =====================================================

SELECT
    brand_name,
    processor_brand,
    COUNT(*) AS num_phones,
    ROUND(AVG(primary_camera_resolution)) AS avg_camera_resolution
FROM smartphones
GROUP BY brand_name, processor_brand;


-- GROUP BY brand_name, processor_brand
-- creates groups based on the COMBINATION
-- of both columns.

-- Example:

-- Samsung + Snapdragon
-- Samsung + Exynos
-- Apple + Bionic
-- Xiaomi + Snapdragon

-- Each combination becomes a separate group.



-- =====================================================
-- GROUP BY + ORDER BY + LIMIT
-- =====================================================

-- Top 5 brands by average price:

SELECT
    brand_name,
    ROUND(AVG(price)) AS avg_price
FROM smartphones
GROUP BY brand_name
ORDER BY avg_price DESC
LIMIT 5;


-- Cheapest average brand:

SELECT
    brand_name,
    ROUND(AVG(screen_size)) AS avg_screen_size
FROM smartphones
GROUP BY brand_name
ORDER BY avg_screen_size ASC
LIMIT 1;



-- =====================================================
-- WHERE + GROUP BY
-- =====================================================

-- WHERE filters rows BEFORE GROUP BY.

-- Example:
-- Count phones for each brand where
-- both NFC and IR blaster are available.

SELECT
    brand_name,
    COUNT(*) AS phone_count
FROM smartphones
WHERE has_nfc = 'True'
  AND has_ir_blaster = 'True'
GROUP BY brand_name
ORDER BY phone_count DESC
LIMIT 1;


-- Mental model:

-- Table rows
--     ↓
-- WHERE → filter individual rows
--     ↓
-- GROUP BY → create groups
--     ↓
-- COUNT() → calculate for each group



-- =====================================================
-- WHERE + GROUP BY
-- =====================================================

-- Find the average price of Samsung phones
-- separately for NFC = True / False.

SELECT
    has_nfc,
    AVG(price) AS avg_price
FROM smartphones
WHERE brand_name = 'samsung'
GROUP BY has_nfc;



-- =====================================================
-- ORDER BY WITHOUT GROUP BY
-- =====================================================

-- Find the most expensive smartphone:

SELECT
    model,
    price
FROM smartphones
ORDER BY price DESC
LIMIT 1;


-- Here we don't need GROUP BY
-- because we are not calculating something
-- separately for each group.



-- =====================================================
-- HAVING
-- =====================================================

-- HAVING is used to filter GROUPS.

-- WHERE  → filters individual rows
-- HAVING  → filters groups


-- Easy mental model:

-- WHERE
-- → filter rows BEFORE GROUP BY

-- HAVING
-- → filter groups AFTER GROUP BY



-- =====================================================
-- LOGICAL ORDER
-- =====================================================

-- The basic logical flow is:

-- FROM
--   ↓
-- WHERE
--   ↓
-- GROUP BY
--   ↓
-- Aggregate functions
--   ↓
-- HAVING
--   ↓
-- SELECT
--   ↓
-- ORDER BY
--   ↓
-- LIMIT



-- =====================================================
-- HAVING WITH COUNT()
-- =====================================================

-- Find brands that have more than 20 phones.

SELECT
    brand_name,
    COUNT(*) AS phone_count,
    AVG(price) AS avg_price
FROM smartphones
GROUP BY brand_name
HAVING COUNT(*) > 20
ORDER BY avg_price DESC;


-- HAVING checks each brand group.

-- Brand 1 → COUNT = 30 → 30 > 20 → KEEP
-- Brand 2 → COUNT = 15 → 15 > 20 → REMOVE
-- Brand 3 → COUNT = 25 → 25 > 20 → KEEP



-- =====================================================
-- IMPORTANT:
-- USING ALIAS IN HAVING
-- =====================================================

-- In MySQL, this can also work:

SELECT
    brand_name,
    COUNT(*) AS phone_count,
    AVG(rating) AS avg_rating
FROM smartphones
GROUP BY brand_name
HAVING phone_count > 20
ORDER BY avg_rating DESC;


-- But using the aggregate expression directly
-- is often clearer for learning:

SELECT
    brand_name,
    COUNT(*) AS phone_count,
    AVG(rating) AS avg_rating
FROM smartphones
GROUP BY brand_name
HAVING COUNT(*) > 20
ORDER BY avg_rating DESC;



-- =====================================================
-- HAVING WITH COUNT()
-- AND WHERE
-- =====================================================

SELECT
    brand_name,
    AVG(ram_capacity) AS avg_ram
FROM smartphones
WHERE refresh_rate > 90
    AND fast_charging_available = 1
GROUP BY brand_name
HAVING COUNT(*) > 10
ORDER BY avg_ram DESC
LIMIT 3;



-- =====================================================
-- HAVING WITH MULTIPLE CONDITIONS
-- =====================================================

SELECT
    brand_name,
    AVG(price) AS avg_price
FROM smartphones
WHERE has_5g = 'True'
GROUP BY brand_name
HAVING AVG(rating) > 70
   AND COUNT(*) > 10;



-- =====================================================
-- WHERE vs HAVING
-- =====================================================

-- WHERE:
-- Filters individual rows.

-- HAVING:
-- Filters groups.

-- Example:

-- WHERE price > 50000
-- → checks each phone's price.

-- HAVING AVG(price) > 50000
-- → checks each brand's average price.



-- =====================================================
-- VERY IMPORTANT RULE
-- =====================================================

-- If you want to filter INDIVIDUAL ROWS:
-- → use WHERE

-- If you want to filter an AGGREGATE RESULT:
-- → use HAVING

-- Example:

-- Find brands whose average price is greater than 50,000.

SELECT
    brand_name,
    AVG(price) AS avg_price
FROM smartphones
GROUP BY brand_name
HAVING AVG(price) > 50000;


-- We use HAVING because AVG(price)
-- is calculated for each group.


-- =====================================================
-- EASY FORMULA
-- =====================================================

-- WHERE --> Filter rows

-- GROUP BY --> Create logical groups
--
-- COUNT / SUM / AVG / MAX / MIN --> Calculate something for each group
--
-- HAVING --> Filter groups
--
-- ORDER BY -->Sort the final result
--
-- LIMIT -->  Control how many rows are returned

