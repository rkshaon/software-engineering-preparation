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
