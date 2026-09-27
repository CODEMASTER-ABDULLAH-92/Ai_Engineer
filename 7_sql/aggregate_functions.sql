-- =====================================
-- AGGREGATE FUNCTIONS
-- =====================================

-- Aggregate functions perform a calculation
-- on multiple rows and return a single result.

-- Common aggregate functions:
-- MAX()      → Finds the maximum value
-- MIN()      → Finds the minimum value
-- AVG()      → Calculates the average
-- SUM()      → Calculates the total
-- COUNT()    → Counts rows/values
-- STD()      → Calculates standard deviation
-- VARIANCE() → Calculates variance

-- =====================================
-- MAX()
-- =====================================

SELECT MAX(price)
FROM health_app.smartphones;

-- Returns the highest price.

-- =====================================
-- MIN()
-- =====================================

SELECT MIN(price)
FROM health_app.smartphones;

-- Returns the lowest price.

-- =====================================
-- AVG()
-- =====================================

SELECT AVG(price)
FROM health_app.smartphones
WHERE brand_name = 'apple';

-- Returns the average price
-- of Apple smartphones.

-- =====================================
-- SUM()
-- =====================================

SELECT SUM(price)
FROM health_app.smartphones
WHERE brand_name = 'apple';

-- Returns the total price of
-- all Apple smartphones.

-- =====================================
-- COUNT()
-- =====================================

SELECT COUNT(*)
FROM health_app.smartphones
WHERE brand_name = 'apple';

-- Counts the number of rows
-- where brand_name is 'apple'.

-- =====================================
-- COUNT(DISTINCT)
-- =====================================

SELECT COUNT(DISTINCT brand_name)
FROM health_app.smartphones;

-- Counts the number of unique brands.

-- Example:
-- Apple
-- Samsung
-- Apple
-- Xiaomi
-- Samsung
----------

-- COUNT(DISTINCT brand_name)
-- gives:
-- 3

-- =====================================
-- STANDARD DEVIATION
-- =====================================

SELECT STD(screen_size)
FROM health_app.smartphones;

-- STD() calculates the standard deviation
-- of screen_size.

-- =====================================
-- VARIANCE
-- =====================================

SELECT VARIANCE(screen_size)
FROM health_app.smartphones;

-- VARIANCE() calculates how much the
-- screen_size values vary from their average.







-- =====================================
-- SCALAR FUNCTIONS
-- =====================================

-- Scalar functions operate on individual
-- values and return a result for each value.

-- Common scalar functions:

-- ABS()   → Returns the absolute value
-- ROUND() → Rounds a number
-- CEIL()  → Rounds a number upward
-- FLOOR() → Rounds a number downward

-- =====================================
-- ABS()
-- =====================================

SELECT ABS(-25);

-- Result:
-- 25

-- =====================================
-- ROUND()
-- =====================================

SELECT ROUND(15.678);

-- Result:
-- 16

-- =====================================
-- CEIL()
-- =====================================

SELECT CEIL(15.2);

-- Result:
-- 16

-- CEIL() always rounds upward.

-- =====================================
-- FLOOR()
-- =====================================

SELECT FLOOR(15.8);

-- Result:
-- 15

-- FLOOR() always rounds downward.



