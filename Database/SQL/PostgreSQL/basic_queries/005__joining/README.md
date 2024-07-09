# Join Query

A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

There are server types of `join`, they are:
- Inner join
- Left join
- Right join
- Full join
- Cross join
- Self join


To demonastrate `inner join`, `left join`, `right join`, `full join`, `cross join` query, let's create 2 tables **`Student`** and **`Result`** like below.


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

![Inner Join](./images/img_inner_join.png)

## Left Join
Run the query below:
```
SELECT student.id, student.name, student.roll, result.gpa
FROM student
LEFT JOIN result
ON student.id = result.student_id;
```
Returns all records from the left table **``Student``**, and the matched records from the right table **``Result``**. The result is NULL from the right side if there is no match.

![Left Join](./images/img_left_join.png)


# Right Join
Run the query below:
```
SELECT student.id, student.name, student.roll, result.gpa
FROM student
RIGHT JOIN result
ON student.id = result.student_id;
```
Returns all records from the right table **``Result``**, and the matched records from the left table **``Student``**. The result is `NULL` from the left side when there is no match.

![Right Join](./images/img_right_join.png)

## Full Join / Full Outer Join
Run the query below:
```
SELECT student.id, student.name, student.roll, result.gpa
FROM student
FULL OUTER JOIN result
ON student.id = result.student_id;
```
Returns all records when there is a match in either left **``Student``** or right **``Result``** table records.

![Full Join](./images/img_full_outer_join.png)

## Cross Join
Run the query below:
```
SELECT student.id, student.name, student.roll, result.gpa
FROM student
CROSS JOIN result;
```
Returns all records where each row from the **`Student`** table is combined with each row from the **`Result`** table. Returned result will be consiste of `m` x `n` rows where `m` is the number of row in **`Student`**, `n` is the number of row in **`Result`**.


To demonastrate `self join`, let's create a table **`Employee`** like below.

```
CREATE TABLE Employee (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employee(employee_id) ON DELETE CASCADE
);
```
**`Employee`** table will holds data of auto incremented primary key `id`, 255 characters maximum limited character varying `employee_name`, self refered foreign key `manager_id` which is on delete cascade.

## Self Join
Run the query below:
```
SELECT e1.employee_name AS Employee, e2.employee_name AS Manager
FROM Employee e1, Employee e2
WHERE e1.manager_id = e2.employee_id;
```
A self join is a regular join, but the table is joined with itself.
