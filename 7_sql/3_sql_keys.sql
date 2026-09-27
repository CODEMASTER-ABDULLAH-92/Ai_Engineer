-- =========================
-- SQL Keys 
-- =========================

-- A key is used to identify records (rows) in a table and/or create relationships between tables.

-- There are 7 different types of the keys which are given below.

-- Super Key
-- Candidate Key
-- Primary Key
-- Alternative Key
-- Composite Key
-- Surrogate Key
-- Foreign Key



-- =========================
-- Super Key
-- =========================

-- A Super Key is one or more columns that can uniquely identify a row in a table.
-- Let's imagine we have a Student table:
-- STUDENT

-- ┌────────────┬──────────────┬───────────────────┬────────────┐
-- │ student_id │ name         │ email             │ phone      │
-- ├────────────┼──────────────┼───────────────────┼────────────┤
-- │ 101        │ Abdullah     │ abd@gmail.com     │ 030012345 │
-- │ 102        │ Ali          │ ali@gmail.com     │ 030067890 │
-- │ 103        │ Ahmed        │ ahmed@gmail.com   │ 030098765 │
-- └────────────┴──────────────┴───────────────────┴────────────┘

-- Suppose:
-- student_id is unique
-- email is unique
-- phone is unique

-- Then all of these can identify a student.

-- =================================
-- Super Keys could be:
-- =================================

-- {student_id}
-- {name, student_id}
-- {email}
-- {email, name}
-- {phone}
-- {student_id, email}
-- {student_id, name, email, phone}


-- Why?
-- Because each combination can still uniquely identify one row.

-- =========================
-- Candidate  Key
-- =========================

-- A Candidate key us a minimal super key because it has no redundant attribute.
-- Means the super key is the combination of the some unique attributes but the candidate key is the one single attribute from the super key that can uniquely identify the record.

-- Example

STUDENT

-- ┌────────────┬──────────────┬───────────────────┐
-- │ student_id │ name         │ email             │
-- ├────────────┼──────────────┼───────────────────┤
-- │ 101        │ Abdullah     │ abd@gmail.com     │
-- │ 102        │ Ali          │ ali@gmail.com     │
-- │ 103        │ Ahmed        │ ahmed@gmail.com   │
-- └────────────┴──────────────┴───────────────────┘

-- Both are unique

-- student_id → unique
-- email      → unique
-- then one we use as candidate key to uniquely identify the record 

-- ===================
-- Primary Key 
-- ===================

-- A Primary Key:
-- 1.uniquely identifies each row
-- 2.cannot contain duplicate values
-- 3.normally cannot contain NULL
-- 4.there is one primary-key constraint per table
-- 5.can consist of one column or multiple columns
-- 6.it should be numeric
-- 7.it should be small
-- 8.it should be constant 

-- ==========================
-- Alternative key 
-- ==========================

-- A Candidate Key that was not selected as the Primary Key.
-- candidate key - primary key = Alternative key 


-- ===================
-- Composite key 
-- ===================
-- Sometimes one column alone cannot uniquely identify a row.
-- We need multiple columns together.
-- Here the composite key come in action.


-- Consider a university enrollment table:
-- ENROLLMENT
-- ┌────────────┬───────────┬────────────┐
-- │ student_id │ course_id │ semester   │
-- ├────────────┼───────────┼────────────┤
-- │ 101        │ CS101     │ Fall       │
-- │ 101        │ CS102     │ Fall       │
-- │ 102        │ CS101     │ Fall       │
-- │ 102        │ CS102     │ Fall       │
-- └────────────┴───────────┴────────────┘


-- =====================
-- Surrogate Key 
-- =====================

-- Sometimes the real-world data doesn't have a convenient key.
-- For example:

-- CUSTOMER
-- ┌──────────────┬──────────────┬────────────────┐
-- │ name         │ email        │ phone          │
-- ├──────────────┼──────────────┼────────────────┤
-- │ Abdullah     │ abd@gmail.com│ 030012345      │
-- │ Ali          │ ali@gmail.com│ 030067890      │
-- └──────────────┴──────────────┴────────────────┘

-- We could use email as an identifier.
-- But perhaps we don't want our database identity to depend on business information.
-- So we create an artificial ID:
-- customer_id

-- For example:
-- ┌─────────────┬──────────────┬────────────────┐
-- │ customer_id │ name         │ email          │
-- ├─────────────┼──────────────┼────────────────┤
-- │ 1           │ Abdullah     │ abd@gmail.com  │
-- │ 2           │ Ali          │ ali@gmail.com  │
-- │ 3           │ Ahmed        │ ahmed@gmail.com│
-- └─────────────┴──────────────┴────────────────┘

-- Here:
-- 1
-- 2
-- 3
-- are generated specifically for database identification.
-- This is a:
-- Surrogate Key


-- ======================
-- 7. Foreign Key
-- ======================

-- Now we reach one of the most important keys for relationships between tables.
-- A Foreign Key connects one table to another table.
-- The primary key of the main table is used in the other table as the foreign key 
-- Suppose we have:

-- CUSTOMER
-- ┌─────────────┬───────────┐
-- │ customer_id │ name      │
-- ├─────────────┼───────────┤
-- │ 1           │ Abdullah  │
-- │ 2           │ Ali       │
-- │ 3           │ Ahmed     │
-- └─────────────┴───────────┘

-- And:
-- ORDER
-- ┌──────────┬─────────────┬────────────┐
-- │ order_id │ customer_id │ product    │
-- ├──────────┼─────────────┼────────────┤
-- │ 501      │ 1           │ Laptop     │
-- │ 502      │ 2           │ Keyboard   │
-- │ 503      │ 1           │ Mouse      │
-- └──────────┴─────────────┴────────────┘


-- The customer_id in ORDER refers to the customer_id in CUSTOMER.

-- Therefore:

-- CUSTOMER.customer_id
--         │
--         │ referenced by
--         ▼
-- ORDER.customer_id
-- The customer_id in the ORDER table is a:
-- Foreign Key





-- | Key                 | Simple Meaning                                   
-- | ------------------- | ------------------------------------------------ 
-- | **Super Key**       | One or more columns that uniquely identify a row 
-- | **Candidate Key**   | Minimal Super Key                                
-- | **Primary Key**     | Candidate Key selected as the main identifier    
-- | **Alternative Key** | Candidate Key not selected as Primary Key        
-- | **Composite Key**   | Key made from multiple columns                   
-- | **Surrogate Key**   | Artificial/generated identifier                  
-- | **Foreign Key**     | Column that references a key in another table    
