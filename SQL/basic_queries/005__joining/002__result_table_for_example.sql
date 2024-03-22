CREATE TABLE IF NOT EXISTS Result (
    id SERIAL PRIMARY KEY,
    student_id INT,
    course_name VARCHAR(255),
    gpa DECIMAL(3, 2),
    FOREIGN KEY (student_id) REFERENCES Student(id)
);