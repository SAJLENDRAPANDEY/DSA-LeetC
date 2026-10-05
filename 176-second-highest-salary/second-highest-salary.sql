# Write your MySQL query statement below

-- SELECT max(salary) AS SecondHighestSalary
-- FROM Employee
-- WHERE salary<(SELECT MAX(salary) FROM Employee)

-- WITH rn AS (
--     SELECT 
--         salary,
--         DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
--     FROM Employee
-- )

-- SELECT 
--     MAX(CASE WHEN rnk = 2 THEN salary END) AS SecondHighestSalary
-- FROM rn;








SELECT 
    MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary<(SELECT MAX(salary) FROM Employee)
