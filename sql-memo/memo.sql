-- Window Function (RANK, LAG, SUM OVER)
-- Self JOIN
-- CASE WHEN + GROUP BY (pivot)

SELECT * FROM (
    SELECT name, salary, dept_id, DENSE_RANK() OVER (
        PARTITION BY dept_id ORDER BY salary DESC
    ) as salary_rank
    FROM Employee
)
JOIN Department ON Employee.dept_id = Department.id
WHERE salary_rank <= 3;

WITH Numbered AS (
    SELECT user_id, login_date, ROW_NUMBER() OVER (
        PARTITION BY user_id ORDER BY login_date
    ) AS rn FROM
    (SELECT DISTINCT user_id, login_date FROM UserActivity) AS DistinctDates
),
Grouped AS (
    SELECT user_id, login_date, (
        DATE_SUB(login_date, INTERVAL rn DAY)
    ) AS group_id
    FROM Numbered
)
SELECT DISTINCT user_id
FROM Grouped
GROUP BY user_id, group_id
HAVING COUNT(*) >= 3;


WITH MonthlyAmount AS (
    SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(amount) AS total_amount
    FROM Sales
    GROUP BY month
)
SELECT month, total_amount,
    LAG(total_amount, 1, NULL) OVER (ORDER BY month) AS prev_amount,
    ROUND(
        COALESCE((total_amount - prev_amount) / NULLIF(prev_amount, 0) * 100, 0),
        2
    ) AS growth_percentage
FROM MonthlyAmount
ORDER BY month;


SELECT E.name FROM Employee E JOIN Employee M ON E.manager_id = M.id
WHERE E.salary > M.salary;

SELECT sale_date, revenue, SUM(revenue) OVER (
    ORDER BY sale_date ROWS UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total;

SELECT product,
    MAX(CASE WHEN quarter = 'Q1' THEN amount ELSE 0) AS Q1,
    MAX(CASE WHEN quarter = 'Q2' THEN amount ELSE 0) AS Q2,
    MAX(CASE WHEN quarter = 'Q3' THEN amount ELSE 0) AS Q3,
    MAX(CASE WHEN quarter = 'Q4' THEN amount ELSE 0) AS Q4
FROM Sales
GROUP BY product;

SELECT
    customer_id,
    SUM(amount) AS total_amount,
    COUNT(*) AS order_count,
    AVG(amount) AS average_amount
FROM Orders
GROUP BY customer_id
HAVING
    SUM(amount) >= 1000
    AND COUNT(*) >= 3
    AND AVG(amount) >= 300
ORDER BY customer_id;