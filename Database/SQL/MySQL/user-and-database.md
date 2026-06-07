# User & Database

## Database
### Show the Database List
```sql
SHOW DATABASES;
```

### Use Database
```sql
USE company_db;
```

### Create Database
```sql
CREATE DATABASE company_db;
```

### Delete database
```sql
DROP DATABASE company_db;
```

### Show tables
```sql
SHOW TABLES;
```

### Describe table
```sql
DESCRIBE employees;
```
or
```sql
DESC employees;
```

## User
### Existing Users List
```sql
SELECT user, host FROM mysql.user;
```

### Create User
```sql
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'StrongPassword123!';
```

### Create Remote User
```sql
CREATE USER 'remote_user'@'%' IDENTIFIED BY 'StrongPassword123!';
```

`%` means the user can connect from any host.

### Remove Users
```sql
DROP USER 'app_user'@'localhost';
```

### Change User Password
```sql
ALTER USER 'app_user'@'localhost'
IDENTIFIED BY 'NewStrongPassword!';
```
***Note***: MySQL version `MySQL 8+` required.

### Show current user
```sql
SELECT CURRENT_USER();
```

## Grant Permissions
### Give all permissions on a database
```sql
GRANT ALL PRIVILEGES ON company_db.* TO 'app_user'@'localhost';
```

### Give read-only access
```sql
GRANT SELECT ON company_db.* TO 'report_user'@'localhost';
```

### Give required permissions
```sql
GRANT SELECT, INSERT, UPDATE, DELETE
ON crm_db.* TO 'crm_user'@'localhost';
```

### Reload privileges
```sql
FLUSH PRIVILEGES;
```

## Example Complete Initial Setup
```sql
CREATE DATABASE example_db;

CREATE USER 'example_user'@'localhost'
IDENTIFIED BY 'StrongPassword123!';

GRANT ALL PRIVILEGES ON example_db.* TO 'example_user'@'localhost';

FLUSH PRIVILEGES;
```

Now connect using:
```bash
mysql -u crm_user -p
```


## Table
### See all the tables
```sql
SHOW TABLES;
```

### Search tables by using name
```sql
SHOW TABLES LIKE '%searchword%';
```

or 
```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'schema_name'
AND table_name LIKE '%searchword%';
```
or
```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'schema_name'
AND LOWER(table_name) LIKE '%searchword%';
```
for case sensitive search.

### See all columns of the table
```sql
DESCRIBE table_name;
```

or shorter
```sql
DESC table_name;
```
 or
 ```sql
SHOW COLUMNS FROM table_name;
```

or
```sql
SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'schema_name'
AND table_name = 'table_name';
```
this will show only column names.

or detail strcuture
```sql
SHOW CREATE TABLE table_name;
```
Example
```sql
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | bigint       | NO   | PRI | NULL    | auto_increment |
| name       | varchar(255) | YES  |     | NULL    |                |
| created_at | datetime     | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
```
