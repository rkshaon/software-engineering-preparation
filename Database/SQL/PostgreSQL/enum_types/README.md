# PostgreSQL: Enum Types
Enum types are one of PostgreSQL’s most underrated features. They let you define a fixed set of values for a column — perfect for things like `status`, `priority`, or `user_role`.

## 🧠 What Is an ENUM Type in PostgreSQL?

An `ENUM (short for enumerated type)` defines a static list of valid values.
For example, imagine we have a table to track interview results:
```sql
CREATE TYPE interviewresult AS ENUM (
  'PENDING',
  'COMPLETED',
  'FAILED',
  'CANCELLED',
  'RESCHEDULED',
  'PASSED'
);
```

You can then use it in a table like this:

```sql
CREATE TABLE lead_interviews (
  id SERIAL PRIMARY KEY,
  result interviewresult NOT NULL DEFAULT 'PENDING'
);
```

## 🔍 How to View All ENUM Types in PostgreSQL
### Option 1: Using `psql`

If you’re inside the PostgreSQL CLI (`psql`), run:
```sql
\dT
```

This lists all user-defined types, including your enums.

To see more details about one specific type:
```sql
\dT+ interviewresult
```

### Option 2: Using SQL Query (Recommended)

Here’s a clean query that lists all enum types and their values:
```sql
SELECT n.nspname AS schema,
       t.typname AS type_name,
       e.enumlabel AS value
FROM pg_type t
JOIN pg_enum e ON t.oid = e.enumtypid
JOIN pg_catalog.pg_namespace n ON n.oid = t.typnamespace
ORDER BY schema, type_name, e.enumsortorder;
```

#### ✅ Output Example:
```sql
 schema |   type_name     |   value
--------+-----------------+-----------
 public | interviewresult | PENDING
 public | interviewresult | COMPLETED
 public | interviewresult | FAILED
 public | interviewresult | CANCELLED
 public | interviewresult | RESCHEDULED
 public | interviewresult | PASSED
```

### Option 3: View a Single Enum’s Values

If you just want to inspect one specific type:
```sql
SELECT enumlabel
FROM pg_enum
JOIN pg_type ON pg_enum.enumtypid = pg_type.oid
WHERE pg_type.typname = 'interviewresult'
ORDER BY enumsortorder;
```

#### Output:
```sql
  enumlabel
--------------
 PENDING
 COMPLETED
 FAILED
 CANCELLED
 RESCHEDULED
 PASSED
```

## ⚙️ How to Add a New Value to an ENUM
Let’s say we want to add `NO_SHOW` to our `interviewresult` type.
You can use the `ALTER TYPE` command:
```sql
ALTER TYPE interviewresult ADD VALUE 'NO_SHOW' AFTER 'PASSED';
```

This adds the new enum label after the existing PASSED value.
(If you skip AFTER, it gets added to the end.)

**_⚠️ Note_**: You can only add enum values, not remove or reorder them directly. To remove or rename enums, you’d need to recreate the type.
