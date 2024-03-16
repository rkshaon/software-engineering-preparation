# Create Table

### Basic Table Create
```
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    DepartmentID INT
);
```
This creates a table named ***Employees*** to store information about employees, including their unique ID, first name, last name, age, and department ID.

### With Foreign Key
```
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
```
The ***Departments*** table stores information about departments (department ID and department name).
The ***Employees*** table stores information about employees (employee ID, first name, last name, age, and department ID). The department ID in the Employees table links each employee to a specific department in the ***Departments*** table.

### With Foreign Key On Delete Cascade
```
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE CASCADE
);
```
The ***Departments*** table stores information about departments (department ID and department name).
The ***Employees*** table stores information about employees (employee ID, first name, last name, age, and department ID). The department ID in the Employees table links each employee to a specific department in the ***Departments*** table and foreign key constraint that enforces data integrity and manages related data deletion using ON DELETE CASCADE.
