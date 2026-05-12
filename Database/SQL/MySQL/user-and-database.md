# User & Database

## Database
### Show the Database List
```bash
SHOW DATABASES;
```

### Use Database
```bash
USE company_db;
```

### Create Database
```bash
CREATE DATABASE company_db;
```

### Delete database
```bash
DROP DATABASE company_db;
```

## User
### Existing Users List
```bash
SELECT user, host FROM mysql.user;
```

### Create User
```bash
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'StrongPassword123!';
```

### Create Remote User
```bash
CREATE USER 'remote_user'@'%' IDENTIFIED BY 'StrongPassword123!';
```

`%` means the user can connect from any host.

### Remove Users
```bash
DROP USER 'app_user'@'localhost';
```

### Change User Password
```bash
ALTER USER 'app_user'@'localhost'
IDENTIFIED BY 'NewStrongPassword!';
```
***Note***: MySQL version `MySQL 8+` required.

## Grant Permissions
### Give all permissions on a database
```bash
GRANT ALL PRIVILEGES ON company_db.* TO 'app_user'@'localhost';
```

### Give read-only access
```bash
GRANT SELECT ON company_db.* TO 'report_user'@'localhost';
```

### Reload privileges
```bash
FLUSH PRIVILEGES;
```

