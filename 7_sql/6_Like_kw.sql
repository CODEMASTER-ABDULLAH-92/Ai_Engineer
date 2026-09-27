-- =====================================================
-- LIKE & % (Wildcard)
-- =====================================================

-- LIKE is used for pattern matching.
-- It is useful when we want to find values
-- that start with, end with, or contain a pattern.

-- % means: any number of characters (including zero).

-- Starts with 'S'
WHERE product_name LIKE 'S%';

-- Ends with '@gmail.com'
WHERE email LIKE '%@gmail.com';

-- Contains 'phone'
WHERE product_name LIKE '%phone%';

-- Easy rule:
-- 'S%'          → starts with S
-- '%gmail.com'  → ends with gmail.com
-- '%phone%'     → contains phone

-- | Pattern       | Meaning              |
-- | ------------- | -------------------- |
-- | 'S%'          | Starts with S        |
-- | '%gmail.com'  | Ends with gmail.com  |
-- | '%phone%'     | Contains phone       |
-- | 'S'           | Exactly S            |
