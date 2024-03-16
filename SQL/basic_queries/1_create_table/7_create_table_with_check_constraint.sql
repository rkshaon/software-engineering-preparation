CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Grade CHAR(1),
    CHECK (Age >= 18 AND Age <= 60),
    CHECK (Grade IN ('A', 'B', 'C', 'D', 'F'))
);
