SELECT student.id, student.name, student.roll, result.gpa
FROM student
JOIN result ON student.id = result.student_id;


SELECT student.id, student.name, student.roll, result.gpa
FROM student
INNER JOIN result
ON student.id = result.student_id;
