# Write your MySQL query statement below
WITH salary_by_month AS (
    SELECT 
        s.*,
        DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month,
        e.department_id
    FROM Salary s
    LEFT JOIN Employee e
    ON s.employee_id = e.employee_id
),

department_average_salary AS (
    SELECT 
        pay_month,
        department_id,
        AVG(amount) AS departement_average
    FROM salary_by_month
    GROUP BY 1,2
),

company_avearge_salary AS (
    SELECT 
        pay_month,
        AVG(amount) AS company_average
    FROM salary_by_month
    GROUP BY 1
)

SELECT 
    d.pay_month,
    d.department_id,
    CASE 
        WHEN d.departement_average = c.company_average THEN 'same'
        WHEN d.departement_average > c.company_average THEN 'higher'
        WHEN d.departement_average < c.company_average THEN 'lower'
    END AS comparison
FROM department_average_salary d
LEFT JOIN company_avearge_salary c
ON d.pay_month = c.pay_month
ORDER BY department_id, pay_month
