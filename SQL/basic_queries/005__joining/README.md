# Join Query

A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

There are server types of `join`, they are:
- Inner join
- Left join
- Right join
- Full join
- Self join
- Cross join

To demonastrate `join` query, let's create 2 tables **`Student`** and **`Result`** like below.


```
CREATE TABLE IF NOT EXISTS Student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    roll VARCHAR(255)
)
```
**`Student`** table will hold data of `id` which is primary key and will be automatically increment, `name`, `roll` which are character varying with maximum length of 255 character.

```
CREATE TABLE IF NOT EXISTS Result (
    id SERIAL PRIMARY KEY,
    student_id INT,
    course_name VARCHAR(255),
    gpa DECIMAL(3, 2),
    FOREIGN KEY (student_id) REFERENCES Student(id)
);
```
**`Result`** table will hold data of `id` which is auto incremented primary key, `student_id` which is foreign key referencing **`Student`** table and on deleting record from **`Student`**, all records from **`Result`** will be deleted where that same student is refered, `course_name` which is character varying field with maximum 255 character, `gpa` which is decimal allowing maximum 3 digits and 2 decimal places.

---
> **_NOTE:_**
For auto incremented integer field `serial` is used in **PostgreSQL**, if you are using **MySQL** then use `AUTO_INCREMENT` keyword instead of `serial`.
---

## Inner Join
Run the query below:
```
SELECT student.id, student.name, student.roll, result.gpa
FROM student
INNER JOIN result
ON student.id = result.student_id;
```
This query will return records that have matching values in both tables means those record are in **`Student`**, **`Result`** table will be returned.

## Left Join
Run the query below:
```
SELECT student.id, student.name, student.roll, result.gpa
FROM student
LEFT JOIN result
ON student.id = result.student_id;
```
This query will return all records from the **`Student`** table, regardless of whether there are matching records in the **``Result``** table. If there are matching records in the **``Result``** table, the corresponding `gpa` value will be included, if there are no matching record then `NULL` will be set for the `gpa` column.