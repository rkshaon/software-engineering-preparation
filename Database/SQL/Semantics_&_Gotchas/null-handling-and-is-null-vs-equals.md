# `= NULL` vs `IS NULL` in `SQL`: A Small Difference That Breaks Big Systems

If you’ve ever written a SQL query like this:
```sql
SELECT * FROM users WHERE deleted_at = NULL;
```

…and wondered why it returned zero rows, this article is for you.

The difference between `= NULL` and `IS NULL` is subtle, easy to miss, and responsible for **countless production bugs**, especially in **multi-tenant systems**, **soft-delete logic**, and **ORM-based applications**.

Let’s break it down properly.

## What Does `NULL` Really Mean?

In SQL, NULL does not mean:
- 0
- empty string ''
- false

It means:

> ***“Unknown / no value”***

Because the value is unknown, SQL **cannot compare it** using normal comparison operators like `=` or `!=`.

## SQL Uses Three-Valued Logic

Unlike most programming languages, SQL uses three-valued logic:
| Value   | Meaning                        |
| ------- | ------------------------------ |
| TRUE    | Condition is true              |
| FALSE   | Condition is false             |
| UNKNOWN | Condition cannot be determined |

Any comparison involving `NULL` results in `UNKNOWN`.

## Why field = NULL Does Not Work

Consider this query:
```sql
SELECT * FROM users WHERE last_login = NULL;
```

### What SQL actually evaluates:
```sql
last_login = UNKNOWN
```

And since **WHERE** clauses only return rows when the condition is **TRUE**, all rows are excluded.

### Result:

**❌ Always returns zero rows**

Even if `last_login` is actually `NULL`.

## The Correct Way: IS NULL

SQL provides special operators to handle NULL values:
```sql
IS NULL
IS NOT NULL
```

### Correct query:
```sql
SELECT * FROM users WHERE last_login IS NULL;
```

### Result:

✅ Returns all rows where `last_login` has no value.

## Comparison Summary

| Expression          | Result         |
| ------------------- | -------------- |
| `field = NULL`      | ❌ Always fails |
| `field != NULL`     | ❌ Always fails |
| `field IS NULL`     | ✅ Correct      |
| `field IS NOT NULL` | ✅ Correct      |

## NULL Truth Table (Simplified)

| Expression         | Result  |
| ------------------ | ------- |
| `NULL = NULL`      | UNKNOWN |
| `NULL != NULL`     | UNKNOWN |
| `NULL IS NULL`     | TRUE    |
| `NULL IS NOT NULL` | FALSE   |


## Real-World Bug Example (Multi-Tenant Systems)

Imagine a system where:
- `company_id = NULL` → global data
- `company_id = 5` → company-specific data

### ❌ Buggy Query
```sql
SELECT * FROM statuses
WHERE company_id = NULL OR company_id = 5;
```

This query **never returns global rows.**

### ✅ Correct Query
```sql
SELECT * FROM statuses
WHERE company_id IS NULL OR company_id = 5;
```

This is a **very common mistake** in SaaS and CRM systems.

## ORM Perspective (SQLAlchemy Example)

Many bugs come from developers assuming ORM comparisons behave like `Python`.

### ❌ Wrong
```python
query.filter(Model.company_id == None)
```

### ✅ Correct
```python
query.filter(Model.company_id.is_(None))
```

Or:
```python
query.filter(Model.company_id.isnot(None))
```

SQLAlchemy correctly translates these into:
```python
company_id IS NULL
company_id IS NOT NULL
```

## Special Note: NULL in `UNIQUE` Constraints

In most databases (PostgreSQL, MySQL):
- `NULL != NULL`
- Multiple `NULL` values are allowed in a `UNIQUE` column

This is why **partial unique indexes** are often required when dealing with defaults:
```sql
CREATE UNIQUE INDEX uq_default_per_company
ON statuses (company_id)
WHERE is_default = TRUE;
```

## Key Takeaways

- ✔ `NULL` is not a value — it’s the absence of a value
- ✔ Never use `=` or `!=` with `NULL`
- ✔ Always use `IS NULL` or `IS NOT NULL`
- ✔ This mistake silently breaks queries (no errors, just wrong data)
- ✔ ORM users must use framework-specific NULL checks

## Final Rule to Remember

> If you are checking for `NULL`, use `IS`, not `=`

One character difference.

Massive impact.
