-- =====================================
-- DATABASE AND TABLE CREATION
-- =====================================

-- 1. First, create the database.
CREATE DATABASE health_app;

-- 2. Select the database to work with.
USE health_app;

-- 3. Create the users table.
CREATE TABLE users (
user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL UNIQUE,
password VARCHAR(255)
);

-- =====================================
-- INSERT COMMANDS
-- =====================================

-- INSERT is used to add data (rows)
-- into a table.

-- =====================================
-- 1. INSERT DATA INTO ALL COLUMNS
-- =====================================

-- When inserting values into all columns,
-- the values must follow the same order
-- as the columns in the table.

INSERT INTO health_app.users
VALUES ('ABDULLAH', '[ABDULLAH4@GMAIL.COM](mailto:ABDULLAH4@GMAIL.COM)', '1234');

-- =====================================
-- 2. INSERT DATA INTO SPECIFIC COLUMNS
-- =====================================

-- We can specify which columns
-- we want to insert data into.

-- Columns that are not specified will
-- receive their DEFAULT value, or NULL
-- if NULL is allowed.

INSERT INTO health_app.users (name, email)
VALUES ('amit', '[amit@gmail.com](mailto:amit@gmail.com)');

-- =====================================
-- 3. INSERT MULTIPLE ROWS
-- =====================================

-- We can insert multiple rows
-- using a single INSERT statement.

INSERT INTO health_app.users
VALUES
(NULL, 'abdullah', '[abdullah22@gmail.com](mailto:abdullah22@gmail.com)', '1234'),
(NULL, 'abdullah2', '[abdullah222@gmail.com](mailto:abdullah222@gmail.com)', '1234'),
(NULL, 'abdullah3', '[abdullah224@gmail.com](mailto:abdullah224@gmail.com)', '1234'),
(NULL, 'abdullah4', '[abdullah225@gmail.com](mailto:abdullah225@gmail.com)', '1234');




-- =====================================================
-- Too Select/Show the complete data of the table 
-- =====================================================

-- BOTH COMMANDS DID THIS 
-- SELECTING ALL THE ROWS

SELECT * FROM health_app.smartphones WHERE 1;
SELECT * FROM health_app.smartphones;


-- =====================================
-- SELECTING SPECIFIC COLUMNS
-- =====================================

-- SELECT is used to retrieve specific
-- columns from a table.

SELECT model, price, rating
FROM health_app.smartphones;



-- =====================================
-- COLUMN ALIAS
-- =====================================

-- AS is used to give a temporary name
-- (alias) to a column in the query result.

-- It does NOT permanently rename the
-- column in the table.

SELECT
os AS 'operating system',
price,
rating
FROM health_app.smartphones;

-- Here:
-- os → original column name
-- operating system → temporary column name

-- The actual column in the table is still:
-- os

-- Only the result displays:
-- operating system | price | rating





-- =====================================
-- MATHEMATICAL OPERATIONS
-- =====================================

-- We can perform mathematical calculations
-- using columns in a SELECT statement.

-- Calculate PPI (Pixels Per Inch):

SELECT
model,
SQRT(
resolution_width * resolution_width
+ resolution_height * resolution_height
) / screen_size AS 'ppi'
FROM health_app.smartphones;


SELECT rating / 10 AS 'rating'
FROM health_app.smartphones;

-- The value of rating is divided by 10.
-- AS 'rating' gives the calculated result
-- a temporary column name.





-- =====================================
-- ADDING A CONSTANT COLUMN
-- =====================================

-- We can add a new column to the result
-- with the same constant value for every row.

SELECT
model,
'smartphone' AS 'type'
FROM health_app.smartphones;

-- This does NOT create a permanent column
-- in the table.

-- =====================================
-- DISTINCT
-- =====================================

-- DISTINCT is used to remove duplicate values
-- from the result.

SELECT DISTINCT brand_name AS 'All brands'
FROM health_app.smartphones;


-- =====================================
-- DISTINCT WITH MULTIPLE COLUMNS
-- =====================================

-- When DISTINCT is used with multiple columns,
-- it returns unique combinations of those columns.

SELECT DISTINCT
brand_name,
processor_brand
FROM health_app.smartphones;

-- For example:

-- brand_name | processor_brand
-- -----------|----------------
-- Apple      | Bionic
-- Samsung    | Exynos
-- Samsung    | Snapdragon
-- Xiaomi     | Snapdragon
--------------------------

-- If the same combination appears multiple times,
-- DISTINCT removes the duplicate combination.



-- =====================================
-- WHERE CLAUSE
-- =====================================

-- WHERE is used to filter rows
-- based on a specific condition.

-- In simple words:
-- "Give me only the rows that
-- satisfy this condition."

-- =====================================
-- 1. FILTER BY TEXT VALUE
-- =====================================

SELECT *
FROM health_app.smartphones
WHERE brand_name = 'apple';

-- This returns only the smartphones
-- whose brand_name is 'apple'.

-- =====================================
-- 2. FILTER BY NUMERIC VALUE
-- =====================================

SELECT *
FROM health_app.smartphones
WHERE price > 100000;

-- This returns only the smartphones
-- whose price is greater than 100000.

-- =====================================
-- COMMON COMPARISON OPERATORS
-- =====================================

-- =     → Equal to
-- >     → Greater than
-- <     → Less than
-- >=    → Greater than or equal to
-- <=    → Less than or equal to
-- <>    → Not equal to
-- !=    → Not equal to (also supported by MySQL)



-- =====================================
-- BETWEEN OPERATOR
-- =====================================

-- BETWEEN is used to filter values
-- within a specific range.

-- In simple words:
-- BETWEEN
-- "Give me values from this range."

-- =====================================
-- USING AND
-- =====================================

SELECT *
FROM health_app.smartphones
WHERE price > 50000
AND price < 100000;

-- This returns smartphones whose price is:
-- greater than 50000
-- AND
-- less than 100000.

-- =====================================
-- USING BETWEEN
-- =====================================

SELECT *
FROM health_app.smartphones
WHERE price BETWEEN 10000 AND 20000;






-- =====================================
-- IN OPERATOR
-- =====================================

-- IN is used to check whether a value
-- matches any value from a given column.

-- In simple words:
-- IN
-- "Is this value one of these values?"

SELECT *
FROM health_app.smartphones
WHERE city IN ('LHR', 'KHR', 'MUL');

-- This returns smartphones where city is:
-- LHR OR KHR OR MUL.

-- =====================================
-- IN WITH AND
-- =====================================

SELECT *
FROM health_app.smartphones
WHERE processor_brand IN ('exynos', 'bionic')
AND brand_name IN ('samsung', 'apple');

-- Here both conditions must be TRUE:

-- processor_brand must be:
-- exynos OR bionic
-------------------

-- AND

-- brand_name must be:
-- samsung OR apple

-- =====================================
-- WITHOUT IN
-- =====================================

-- Without IN, we would need to write
-- multiple OR conditions:

SELECT *
FROM users
WHERE city = 'Lahore'
OR city = 'Islamabad'
OR city = 'Karachi';

-- Using IN makes the query shorter:

SELECT *
FROM users
WHERE city IN ('Lahore', 'Islamabad', 'Karachi');

-- Both queries mean the same thing.

-- =====================================
-- NOT IN
-- =====================================

-- NOT IN is used to exclude values
-- from a given list.

-- In simple words:
-- NOT IN
-- "Give me values that are NOT in this list."

-- Select users whose city is NOT
-- Lahore or Karachi:

SELECT *
FROM users
WHERE city NOT IN ('Lahore', 'Karachi');

-- =====================================
-- NOT IN WITH AND
-- =====================================

SELECT *
FROM health_app.smartphones
WHERE processor_brand IN ('exynos', 'bionic')
AND brand_name NOT IN ('samsung', 'apple');



-- =====================================
-- UPDATE COMMAND
-- =====================================

-- UPDATE is used to modify existing
-- data (rows) in a table.

-- In simple words:
-- UPDATE
-- "Change existing data."

-- =====================================
-- DISABLE SAFE UPDATE MODE
-- =====================================

SET SQL_SAFE_UPDATES = 0;

-- SQL_SAFE_UPDATES is a MySQL safety feature.
-- When it is enabled, MySQL may prevent
-- UPDATE or DELETE statements that could
-- accidentally affect many rows.
---------------------------------

-- Setting it to 0 disables this protection.

-- Use this carefully, especially with
-- UPDATE and DELETE commands.

-- =====================================
-- UPDATE A COLUMN
-- =====================================

UPDATE health_app.smartphones
SET brand_name = 'apple'
WHERE brand_name = 'samsung';

-- This changes brand_name from 'samsung'
-- to 'apple' only for rows where
-- brand_name is currently 'samsung'.

-- =====================================
-- UPDATE MULTIPLE COLUMNS
-- =====================================

UPDATE health_app.users
SET
name = 'ABDULLAH',
password = '1234666'
WHERE email = '[abdullah22@gmail.com](mailto:abdullah22@gmail.com)';

-- This updates two columns:
-- name     → ABDULLAH
-- password → 1234666
---------------------

-- Only the row whose email is
-- '[abdullah22@gmail.com](mailto:abdullah22@gmail.com)' is updated.

-- =====================================
-- IMPORTANT
-- =====================================

-- Always be careful with WHERE.

-- UPDATE without WHERE:
-- UPDATE health_app.users
-- SET name = 'ABDULLAH';
-- This would update the name of
-- EVERY row in the table.

-- Therefore:
-- WHERE → specifies which rows to update.




-- =====================================
-- DELETE COMMAND
-- =====================================

-- DELETE is used to remove existing rows
-- from a table.

-- In simple words:
-- DELETE
-- "Remove rows that match a condition."

-- =====================================
-- DELETE ROWS USING A CONDITION
-- =====================================

DELETE FROM health_app.smartphones
WHERE price > 200000;

-- This deletes all smartphones
-- whose price is greater than 200000.

-- =====================================
-- DELETE USING MULTIPLE CONDITIONS
-- =====================================

DELETE FROM health_app.smartphones
WHERE primary_camera_rear > 150
AND brand_name = 'samsung';

## -- This deletes only the rows where:

-- primary_camera_rear > 150
--        AND
-- brand_name = 'samsung'
-------------------------

-- Both conditions must be TRUE.

-- =====================================
-- IMPORTANT
-- =====================================

-- Always be careful with the WHERE clause.

-- DELETE without WHERE:

-- DELETE FROM health_app.smartphones;
-- This deletes ALL rows from the table.
-- The table itself is NOT deleted.


-- Therefore:
-- DELETE + WHERE
-- Delete specific rows.

-- DELETE without WHERE
-- Delete all rows.
