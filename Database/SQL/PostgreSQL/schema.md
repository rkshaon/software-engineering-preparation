# Schema

A schema is a named collection of database objects, including tables, views, indexes, functions, and other objects. Schemas provide a way to organize database objects into logical groups, making it easier to manage permissions, and avoid name conflicts.

## What is a Schema?

In `PostgreSQL`, a schema is a namespace that contains named objects. Schemas allow you to group objects and manage them more easily. Each database in PostgreSQL contains a default schema named `public`, and you can create additional schemas as needed.

## What Does a Schema Do?

Schemas provide several key benefits:
- **Organization**: Group related objects together for better organization.
- **Permission Management**: Assign different permissions to different schemas, allowing for finer control over access.
- **Avoid Name Conflicts**: Objects in different schemas can have the same name, avoiding naming conflicts.

## How Does a Schema Work?

When you create a new object in PostgreSQL, it is placed in a schema. If no schema is specified, the object is placed in the `public` schema by default. You can reference objects in other schemas by prefixing the object name with the schema name (e.g., `schema_name.table_name`).

## Switching Schemas

While working in PostgreSQL, you can switch between schemas by setting the `search_path`. The `search_path` determines the order in which schemas are searched when you reference an object without specifying a schema.

### Setting the Search Path

To set the search path to a specific schema, use the `SET search_path` command:

```sql
SET search_path TO schema_name;
```

To search on multiple schema execute the command below:
```sql
SET search_path TO schema1, public;
```

To reset to default execute the command below:
```sql
SET search_path TO default;
```

### Show Search Path

To see the schema list use the `SHOW search_path` command:
```sql
SHOW search_path;
```

This will display something like below:
```sql
your_database=# SHOW search_path;
 search_path
-------------
 public
 schema1
(2 row)
```

### Show the schema list

To see the schema list use `\dn` command:
```sql
\dn
```

This will display like below:
```sql
       List of schemas
  Name   |       Owner       
---------+-------------------
 public  | pg_database_owner
 tenant3 | sale_dev
 tenant4 | sale_dev
 tenant5 | sale_dev
 tenant6 | sale_dev
(5 rows)
```

### Schema Session

When you set the search_path in a PostgreSQL session, it only affects that session. If you close the shell and open a new one, the search_path will reset to its default value, which typically includes the public schema.

#### Default Behavior
- **Session-Specific Setting**: The `SET search_path` command only applies to the current session. Once you disconnect and reconnect, the search path will revert to its default setting.
- **Default Search Path**: By default, the search path usually includes the `public` schema. You can confirm this by using the `SHOW search_path;` command after reconnecting.

## Modify Search Path

If you want to change the `search_path` permanently for all sessions or for a specific role, you can modify the PostgreSQL configuration or use role-based settings.

### For All Sessions
#### Open `postgresql.conf`
```
sudo nano /etc/postgresql/<version>/main/postgresql.conf
```

#### Modify the `search_path`
```bash
search_path = 'schema1, public'
```

#### Restart PostgreSQL
```bash
sudo systemctl restart postgresql
```

### For Specific Role

Set the search path for a specific role using the `ALTER ROLE` command.

#### Connect and Apply ALTER ROLE command
```sql
ALTER ROLE your_role SET search_path TO schema1, public;
```

## Drop Schema
To drop a schema in `PostgreSQL`, you can use the `DROP SCHEMA` command.
```sql
DROP SCHEMA schema_name;
```
For making more sure check if schema exist.
```sql
DROP SCHEMA IF EXISTS schema_name CASCADE;
```

### Drop Schema Options
#### CASCADE
Use this option if you want to drop the schema along with all objects (like tables, views, etc.) contained within it.
```sql
DROP SCHEMA schema_name CASCADE;
```

***Note***: Be cautious when using `CASCADE`, as it will remove all objects within the schema, which is irreversible unless you have backups.


#### RESTRICT
This is the default behavior. It will prevent the schema from being dropped if it contains any objects. You’ll need to remove all objects first to drop the schema.
```sql
DROP SCHEMA schema_name RESTRICT;
```

