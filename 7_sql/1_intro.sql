-- ============================================================
-- SQL NOTES
-- ============================================================


-- ------------------------------------------------------------
-- 1. WHAT IS SQL?
-- ------------------------------------------------------------

-- SQL stands for Structured Query Language.

-- SQL is a language used to communicate with and manage
-- relational databases.
-- Think of SQL as a way to work with organized data.


-- ------------------------------------------------------------
-- 2. WHY DO WE USE SQL?
-- ------------------------------------------------------------

-- SQL is used to work with data stored in a database.
--
-- SQL allows us to:
--
--    - Store data
--    - Find/retrieve data
--    - Modify data
--    - Delete data
--    - Organize and relate data
--
-- Example:
-- A website may need to store:
--
--    - Users
--    - Products
--    - Orders
--    - Payments
--    - Employees


-- ------------------------------------------------------------
-- 3. WHAT IS A DATABASE?
-- ------------------------------------------------------------

-- A database is an organized collection of data.
-- A database can contain multiple tables.


-- ------------------------------------------------------------
-- 4. WHAT IS A TABLE?
-- ------------------------------------------------------------

-- A table is a structure used to organize data into
-- columns and rows.
--
-- Think of a table like an Excel spreadsheet.

--      +----+---------+-----+------------+
--      | ID | Name    | Age | Email      |
--      +----+---------+-----+------------+
--      |  1 | Ali     | 22  | ali@...    |
--      |  2 | Ahmed   | 24  | ahmed@...  |
--      |  3 | Hassan  | 21  | hassan@... |
--      +----+---------+-----+------------+


-- 5. WHAT IS AN ATTRIBUTE?
-- ------------------------------------------------------------
-- An attribute is a column of a table.
-- Attribute = Column = Property of an entity


-- ------------------------------------------------------------
-- 6. WHAT IS A ROW?
-- ------------------------------------------------------------

-- A row represents one complete record in a table.
-- Row = Record = Tuple
-- One row describes one instance/entity.



-- 7. ATTRIBUTE VS ROW
-- ------------------------------------------------------------
--
--                  USERS TABLE
--
--        ID     Name     Age     Email
--        |       |        |        |
--        v       v        v        v
--      COLUMN  COLUMN   COLUMN   COLUMN
--
--      +----+---------+-----+------------+
--      |  1 | Ali     | 22  | ali@...    | <- ROW
--      |  2 | Ahmed   | 24  | ahmed@...  | <- ROW
--      |  3 | Hassan  | 21  | hassan@... | <- ROW
--      +----+---------+-----+------------+
--
--
-- Column -> What information do we store?
-- Row    -> Whose/which information are we storing?


-- 8. WHAT IS DEGREE?
-- ------------------------------------------------------------
-- Degree means the number of attributes (columns)
-- in a table.
--
-- Example:
--      +----+---------+-----+------------+
--      | ID | Name    | Age | Email      |
--      +----+---------+-----+------------+
--      Number of columns = 4
--      Therefore:
--      Degree = 4
--
-- Formula:
--      Degree = Number of Columns


-- 9. WHAT IS CARDINALITY?
-- ------------------------------------------------------------
-- Cardinality means the number of rows (records)
-- in a table.
--
-- Example:
--      +----+---------+-----+------------+
--      | ID | Name    | Age | Email      |
--      +----+---------+-----+------------+
--      |  1 | Ali     | 22  | ali@...    |
--      |  2 | Ahmed   | 24  | ahmed@...  |
--      |  3 | Hassan  | 21  | hassan@... |
--      |  4 | Usman   | 25  | usman@...  |
--      +----+---------+-----+------------+
--
--      Number of rows = 4
--      Therefore:
--      Cardinality = 4
-- Formula:
--      Cardinality = Number of Rows



-- SQL          -> Structured Query Language
-- Database     -> Organized collection of data

-- MOST IMPORTANT:
--      TABLE = COLUMNS + ROWS
--      COLUMN = ATTRIBUTE
--      ROW = RECORD
--      DEGREE = NUMBER OF COLUMNS
--      CARDINALITY = NUMBER OF ROWS