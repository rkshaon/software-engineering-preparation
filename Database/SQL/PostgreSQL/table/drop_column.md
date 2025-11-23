# PostgreSQL: Drop Column
To drop a column from a table in PostgreSQL here is the commands.

## Command
```sql
ALTER TABLE table_name DROP COLUMN column_name;
```

If the column has constraints (FK, PK), drop them first:
```sql
ALTER TABLE table_name DROP CONSTRAINT constraint_name;
ALTER TABLE table_name DROP COLUMN column_name;
```

If you’re not sure about the constraint name:
```sql
SELECT conname, conrelid::regclass
FROM pg_constraint
WHERE conrelid = 'table_name'::regclass;
```
