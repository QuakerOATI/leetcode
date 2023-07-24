-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | employee_id   | int     |
-- | team_id       | int     |
-- +---------------+---------+
-- employee_id is the primary key for this table.
-- Each row of this table contains the ID of each employee and their respective team.
-- 
-- Write an SQL query to find the team size of each of the employees.
-- 
-- Return result table in any order.

-- Good on memory usage, shitty on runtime
SELECT emp1.employee_id, emp2.num_players as team_size
FROM Employee as emp1
LEFT JOIN (SELECT team_id, COUNT(*) as num_players from Employee GROUP BY team_id) as emp2
ON emp1.team_id = emp2.team_i


-- Here's a better solution:
SELECT employee_id, team_size

FROM Employee AS e

JOIN (SELECT team_id, COUNT(employee_id) AS team_size

      FROM Employee

      GROUP BY team_id) AS teams

ON e.team_id = teams.team_id
