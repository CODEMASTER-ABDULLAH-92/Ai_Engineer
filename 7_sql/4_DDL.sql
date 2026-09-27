-- DDL stands for Data Definition Language.
-- It is a part of SQL used to define and change the structure of a database.

-- | Command  | Purpose                                            |
-- | -------  | -------------------------------------------------- |
-- | CREATE   | Creates a database object                          |
-- | ALTER    | Changes its structure                              |
-- | DROP     | Completely removes the object                      |
-- | TRUNCATE | Removes all rows while keeping the table structure |



-- ==============================
-- Creating the database 
-- ==============================

-- Syntax 
-- CREATE DATABASE db_name 

code 
CREATE DATABASE health_app

--Better way to do this 
CREATE DATABASE IF NOT EXISTS health_app

-- ===========================
-- Drop database
-- ===========================
-- Syntax 
-- DROP DATABASE db_name

-- CODE 
DROP DATABASE health_app

-- Better way to this 
DROP DATABASE IF EXISTS health_app

-- ===================================
-- Creating the table 
-- ===================================

-- USE db_name
-- CREATE TABLE table_name()

USE health_app
CREATE TABLE user(
    user_id INTEGER,
    name  VARCHAR(255),
    email VARCHAR(255)
)

-- ==============================
-- How to TRUNCATE a table
-- ==============================

-- It is used to remove ALL rows/data from a table
-- while keeping the table itself and its structure.

-- How to empty the table
-- Syntax:
-- TRUNCATE TABLE table_name;


-- IMPORTANT:

-- TRUNCATE removes the DATA,
-- but it does NOT remove the TABLE.

--==================================
-- Easy way to remember:
--==================================

-- DROP     → Destroy the table
-- TRUNCATE → Empty the table
-- DELETE   → Remove rows

-- Drop the table 

DROP TABLE IF EXISTS user

-- ==============================
-- NOT NULL Constraint
-- ==============================
-- NOT NULL is a constraint in SQL.

-- It means:
-- A column cannot contain NULL values.

-- Example:
-- name → NOT NULL
-- Every student must have a name.


-- Here in the above table we are adding only the not null 
CREATE TABLE user(
    user_id INTEGER NOT NULL,
    name  VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL

    -- Another way to write constraints
    CONSTRAINT user_email_unique NOT NULL (email)
)

-- ==============================
-- UNIQUE Constraint
-- ==============================

-- UNIQUE is a constraint in SQL.

-- It ensures that values in a column
-- are not duplicated.

-- In simple words:
-- UNIQUE
-- "No duplicate values are allowed."

CREATE TABLE user(
    user_id INTEGER NOT NULL UNIQUE,
    name  VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE

    CONSTRAINT user_name_email_unique UNIQUE (name, email)
)

-- ==============================
-- UNIQUE vs PRIMARY KEY
-- ==============================

-- PRIMARY KEY:
--    → Uniquely identifies each row.
--    → Cannot contain NULL.
--    → One Primary Key constraint per table.

-- UNIQUE:
--    → Prevents duplicate values.
--    → NULL handling depends on the DBMS
--      and schema.
--    → A table can have multiple UNIQUE constraints.


-- ==============================
-- PRIMARY KEY
-- ==============================
-- PRIMARY KEY is a constraint in SQL.
-- It is used to uniquely identify
-- each row in a table.

-- In simple words:
-- PRIMARY KEY
-- "Every row must have a unique identity."

-- Rules of PRIMARY KEY:
-- 1. Values must be UNIQUE.
-- 2. It cannot contain NULL.
-- 3. A table can have only ONE PRIMARY KEY constraint.
-- 4. A PRIMARY KEY can contain one column
--    or multiple columns (Composite Primary Key).

-- Example:

CREATE TABLE students (
student_id INT PRIMARY KEY,
name VARCHAR(100)

CONSTRAINT students_student_id_pk PRIMARY KEY (student_id)
);

-- Here, student_id is the PRIMARY KEY.
-- Each student must have a different student_id.
-- student_id cannot be NULL.
-- It uniquely identifies each student.


-- ==============================
-- AUTO_INCREMENT
-- ==============================

-- AUTO_INCREMENT is a MySQL feature
-- used to automatically generate a number
-- for a column when a new row is inserted.

-- In simple words:
-- AUTO_INCREMENT
--       ↓
-- "MySQL automatically gives the next number."
-- It is commonly used with a PRIMARY KEY.

-- Example:

CREATE TABLE students (
student_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100)

CONSTRAINT students_student_id_auto_increment AUTO INCREMENT (student_id)
);

-- Now we do not need to manually provide
-- the student_id when inserting a student.

-- Example:

INSERT INTO students (name)
VALUES ('Ali');

INSERT INTO students (name)
VALUES ('Ahmed');

INSERT INTO students (name)
VALUES ('Abdullah');

-- MySQL automatically generates:

-- student_id | name
-- ------------|---------
-- 1           | Ali
-- 2           | Ahmed
-- 3           | Abdullah





-- ==============================
-- CHECK CONSTRAINT
-- ==============================

-- CHECK is a constraint in SQL.

-- It is used to make sure that
-- a value satisfies a specific condition.

-- In simple words:
-- CHECK
-- "The value must follow this condition."

-- Example:

CREATE TABLE students (
student_id INT PRIMARY KEY,
age INT,
CONSTRAINT students_student_id_pk CHECK (age >= 18)
);

-- Here, age must be 18 or greater.

-- Valid:
-- age = 20
-- age = 18

-- Invalid:
-- age = 17
-- age = 15

--===========================
-- CHECK is useful for:
--===========================
-- age
-- salary
-- marks
-- quantity
-- status
-- prices
-- and other values with specific rules.


-- ==============================
-- DEFAULT CONSTRAINT
-- ==============================

-- DEFAULT is used to provide
-- an automatic value for a column
-- when no value is provided during INSERT.

-- In simple words:
-- DEFAULT
-- "If you don't provide a value,
--  use this value automatically."

-- Example:

CREATE TABLE users (
user_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100),
status VARCHAR(20) DEFAULT 'active'
CONSTRAINT users_status DEFAULT ('Active')
);

-- If we do not provide a value for status:

INSERT INTO users (name)
VALUES ('Ali');

-- MySQL automatically uses:
-- status = 'active'

-- Result:
-- user_id | name | status
-- ---------|------|--------
-- 1        | Ali  | active

-- We can also provide a different value:

INSERT INTO users (name, status)
VALUES ('Ahmed', 'inactive');

-- In this case, DEFAULT is not used.
-- The provided value 'inactive' is stored.

-- DEFAULT is useful for values such as:
-- status
-- country
-- role
-- created_at
-- quantity
-- and other columns with a common initial value.


-- ==============================
-- FOREIGN KEY CONSTRAINT
-- ==============================

-- FOREIGN KEY is a constraint in SQL.

-- It is used to create a relationship
-- between two tables.

-- A FOREIGN KEY refers to a PRIMARY KEY
-- or a suitable UNIQUE key in another table.


CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(100)
);

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id)
);

-- Here:
-- customers = Parent table
-- orders    = Child table
-- customer_id in customers = PRIMARY KEY
-- customer_id in orders    = FOREIGN KEY



-- ===========================================
-- Referential Actions
-- ===========================================


-- ==============================
-- CASCADE
-- ==============================

-- CASCADE is a referential action
-- used with a FOREIGN KEY.

-- It automatically applies certain changes
-- from the parent table to related rows
-- in the child table.

-- In simple words:
-- CASCADE
-- "If the parent changes, automatically
--  make the related child rows follow."

-- CASCADE is mainly used with:
-- ON DELETE CASCADE
-- ON UPDATE CASCADE

-- ==============================
-- ON DELETE CASCADE
-- ==============================

-- If a row is deleted from the parent table,
-- the related rows in the child table
-- are automatically deleted.

-- Example:

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,


FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- ==============================
-- ON UPDATE CASCADE
-- ==============================

-- If the referenced key in the parent table
-- is updated, the related FOREIGN KEY values
-- in the child table are automatically updated.





-- ==============================
-- SET NULL
-- ==============================

-- SET NULL is a referential action
-- used with a FOREIGN KEY.

-- It sets the FOREIGN KEY value to NULL
-- when the referenced row in the parent table
-- is deleted or updated.

-- In simple words:
-- SET NULL
-- "If the parent is deleted or changed,
--  remove the relationship by setting
--  the foreign key to NULL."

-- ==============================
-- ON DELETE SET NULL
-- ==============================

-- If a row is deleted from the parent table,
-- the FOREIGN KEY value in related child rows
-- is automatically changed to NULL.

-- Example:

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,

FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
    ON DELETE SET NULL
    ON UPDATE SET NULL
);




-- =========================================
-- ALter table Commands 
-- =========================================


-- ALTER TABLE is a DDL command used to modify the structure of an existing table.
-- In simple words:
-- ALTER TABLE → Change the structure of a table that already exists.
-- You can use it to add, modify, rename, or remove columns and constraints.


-- Syntax of the alter.
-- alter table table_name add column password varchar(255) not null
ALTER TABLE orders ADD COLUMN password VARCHAR(255) NOT NULL