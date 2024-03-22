SELECT student.id, student.name, student.roll, result.gpa
FROM student
CROSS JOIN result;