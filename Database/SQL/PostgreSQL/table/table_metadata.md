# Table Metadata
## Column-level details (data type, default, nullable, etc.)
```sql
SELECT
    c.ordinal_position,
    c.column_name,
    c.data_type,
    c.udt_name AS internal_type,
    c.character_maximum_length,
    c.numeric_precision,
    c.numeric_scale,
    c.is_nullable,
    c.column_default,
    c.collation_name
FROM information_schema.columns c
WHERE c.table_schema = 'public'
  AND c.table_name = 'your_table_name'
ORDER BY c.ordinal_position;
```

This gives you:

- SQL type (`data_type`)

- Internal Postgres type (`udt_name`)

- Default values

- Nullable info

- Length / precision

- Column order

## Primary key & Unique constraints
```sql
SELECT
    tc.constraint_type,
    tc.constraint_name,
    kcu.column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
WHERE tc.table_schema = 'public'
  AND tc.table_name = 'your_table_name'
ORDER BY tc.constraint_type;
```

## Foreign key relationships (very important)
```sql
SELECT
    tc.constraint_name,
    kcu.column_name,
    ccu.table_name AS referenced_table,
    ccu.column_name AS referenced_column,
    rc.update_rule,
    rc.delete_rule
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
JOIN information_schema.referential_constraints rc
  ON rc.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_schema = 'public'
  AND tc.table_name = 'your_table_name';
```

## Indexes (including unique & partial indexes)
```sql
SELECT
    i.relname AS index_name,
    a.attname AS column_name,
    ix.indisunique AS is_unique,
    ix.indisprimary AS is_primary,
    pg_get_indexdef(ix.indexrelid) AS index_definition
FROM pg_class t
JOIN pg_index ix ON t.oid = ix.indrelid
JOIN pg_class i ON i.oid = ix.indexrelid
JOIN pg_attribute a ON a.attrelid = t.oid AND a.attnum = ANY(ix.indkey)
WHERE t.relname = 'your_table_name'
ORDER BY i.relname;
```

## Check constraints
```sql
SELECT
    conname AS constraint_name,
    pg_get_constraintdef(oid) AS definition
FROM pg_constraint
WHERE conrelid = 'your_table_name'::regclass
  AND contype = 'c';
```

## One-liner: Show full CREATE TABLE
```sql
SELECT pg_get_tabledef('your_table_name'::regclass);
```

⚠️ If your Postgres version doesn’t support `pg_get_tabledef`, use:

```sql
SELECT pg_get_tabledef(oid)
FROM pg_class
WHERE relname = 'your_table_name';
```
