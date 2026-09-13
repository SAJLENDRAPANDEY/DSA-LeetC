# Write your MySQL query statement below

SELECT
    class
FROM Courses
GROUP BY class
-- ORDER BY COUNT(class) DESC
HAVING COUNT(class)>=5