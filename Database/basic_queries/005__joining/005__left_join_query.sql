SELECT student.id, student.name, student.roll, result.gpa
FROM student
LEFT JOIN result
ON student.id = result.student_id;