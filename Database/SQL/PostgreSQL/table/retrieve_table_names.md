# Retrive Table Names

Enter into your psql shell and then execute the query below.

```
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'schema_name'
ORDER BY table_name;
```

Replace 'schema_name' with your schema name.