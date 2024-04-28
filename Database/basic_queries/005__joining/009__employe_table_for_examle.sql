CREATE TABLE Employee (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employee(employee_id) ON DELETE CASCADE
);
