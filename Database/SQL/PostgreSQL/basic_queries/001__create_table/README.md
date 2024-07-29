# Create Table

### Basic Table Create
```sql
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
```sql
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
```sql
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

### With Default Value
```sql
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10,2) DEFAULT 0,
    StockQuantity INT DEFAULT 0
);
```
The ***Products*** table will store data ProductID, ProductName, Price, StockQuantity and while inserting data if StockQuantity is not provided then this will set value 0.

### Unique Constraint
````sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE
);
````
The ***Customers*** table will store data CustomerID, FirstName, LastName, Email and will ensure that the Email is always unique and prevdent duplicate Email.

### Primary Key
```sql
CREATE TABLE Orders (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID)
);
```
The ***Orders*** table will store data OrderID, ProductID, Quantity and in this table the combination of OrderID and ProductID is a composite primary key and will always unique in the table.

### Auto Incremented Primary Key
```sql
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    Username VARCHAR(50),
    Password VARCHAR(50)
);
```
The ***Users*** table will store data UserID, Username, Password of an User, where UserID will be auto incremented.

### With Check Constraint
```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Grade CHAR(1),
    CHECK (Age >= 18 AND Age <= 60),
    CHECK (Grade IN ('A', 'B', 'C', 'D', 'F'))
);
```
The ***Students*** table will hold information with data type specifications, primary key for unique identification, and check constraints to maintain data integrity and enforce specific rules like the value of Age will be between 18 to 60 and the value of Grade will be one of ('A', 'B', 'C', 'D', 'F').

### Date Time Field
```sql
CREATE TABLE Events (
    EventID INT PRIMARY KEY,
    EventName VARCHAR(100),
    EventDate DATE,
    StartTime TIME,
    EndTime TIME,
    EventDateTime TIMESTAMP
);
```
The ***Events*** table will store data of EventID, EventName, EventDate which is a Date type field, StartTime, EndTime where both is Time type field, EventDateTime which is a Timestamp type field.

### Indexing
```sql
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10,2),
    INDEX idx_price (Price)
);
```
The index on the Price column will help optimize queries involving price-related operations.
