SELECT e1.employee_name AS Employee, e2.employee_name AS Manager
FROM Employee e1, Employee e2
WHERE e1.manager_id = e2.employee_id;
