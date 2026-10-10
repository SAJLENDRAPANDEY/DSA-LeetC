# Write your MySQL query statement below
WITH rn AS (
SELECT 
    d.name AS Department,
    e.name AS Employee,
    salary,
    DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS rnk
FROM Employee e 
JOIN Department d
ON e.departmentId=d.id
)
SELECT 
    Department,
    Employee,
    salary
FROM rn 
WHERE rnk=1;

