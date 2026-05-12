# Query
## Create table
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(150),
    salary DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Insert data
```sql
INSERT INTO employees (name, email, salary)
VALUES ('John Doe', 'john@example.com', 50000);
```

## Retrieve data
```sql
SELECT * FROM employees;
```

## Update data
```sql
UPDATE employees
SET salary = 55000
WHERE id = 1;
```

## Delete data
```sql
DELETE FROM employees
WHERE id = 1;
```
