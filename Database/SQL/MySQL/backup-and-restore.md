# Backup/Restore or Export/Import
## Backup and Restore Database
### Backup database
```bash
mysqldump -u root -p company_db > company_db.sql
```

### Restore database
```bash
mysql -u root -p company_db < company_db.sql
```

## Import and Export SQL Files
### Import
```bash
mysql -u root -p database_name < backup.sql
```

### Export
```bash
mysqldump -u root -p database_name > backup.sql
```

## Difference between `backup/export` and `restore/import`
In `MySQL`, the terms backup/export and restore/import are often used interchangeably, but there are practical differences in meaning and purpose.

### Backup vs Export
| Topic    | Backup                                                       | Export                           |
| -------- | ------------------------------------------------------------ | -------------------------------- |
| Purpose  | Disaster recovery                                            | Move/share data                  |
| Scope    | Usually full database/server                                 | Usually selected data/tables     |
| Includes | Data, schema, users, routines, triggers, configs (sometimes) | Mostly schema and/or data        |
| Format   | SQL dump, binary backup, snapshot                            | Usually SQL/CSV/JSON             |
| Use Case | Recover after crash                                          | Transfer/reporting/migration     |
| Tools    | `mysqldump`, `mysqlpump`, Percona XtraBackup                 | `mysqldump`, SELECT INTO OUTFILE |

### Restore vs Import
| Topic    | Restore                      | Import                  |
| -------- | ---------------------------- | ----------------------- |
| Purpose  | Recover system/database      | Load external data      |
| Source   | Backup files                 | Exported files          |
| Goal     | Return to previous state     | Insert or migrate data  |
| Scope    | Usually full recovery        | Often partial data load |
| Examples | Recover after server failure | Import CSV into table   |

## Real-World Understanding
### Backup/Restore
Think of this as: *“Save everything so we can recover later.”*

#### Example:
```bash
mysqldump -u root -p company_db > company_db_backup.sql
```

Later:
```bash
mysql -u root -p company_db < company_db_backup.sql
```

This restores the database after:
- server crash
- accidental deletion
- corruption
- failed deployment

### Export/Import

Think of this as:
*“Move or share data.”*

#### Example export to CSV:
```sql
SELECT * FROM employees
INTO OUTFILE '/tmp/employees.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

Later import:
```sql
LOAD DATA INFILE '/tmp/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

This is commonly used for:
- reporting
- analytics
- migrations
- Excel usage
- sharing datasets
