# SOLID Principles

The SOLID principles are a set of five design principles in object-oriented programming that aim to create more **understandable**, **flexible**, and **maintainable code**.
SOLID principles were first introduced by *[Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)* in his 2000 paper ***[Design Principles and Design Patterns](https://staff.cs.utu.fi/~jounsmed/doos_06/material/DesignPrinciplesAndPatterns.pdf)***.

SOLID principles creates:
+ More understandable and maintainable code
+ Greater flexibility and easier extension
+ Robust and reliable software

Each letter in the SOLID acronym stands for a different principle.

### Single Responsibility Principle (SRP)
A class should have only one reason to change. This means that each class should have a single, well-defined responsibility and should not be concerned with anything else. This principle helps to reduce the complexity of your code and makes it easier to understand and maintain.
+ One class, one reason to change.
+ Clear and focused responsibilities for each class.
+ Reduced complexity and improved maintainability.

### Open-Closed Principle (OCP)
Software entities (classes, modules, functions) should be open for extension, but closed for modification. This means that you should be able to add new functionality to your code without having to modify existing code. This principle helps to keep your code clean and modular, and makes it easier to add new features in the future.
+ Extend functionality without modifying existing code.
+ New features added through extension, not modification.
+ Promotes clean, modular code with easy future updates.

### Liskov Substitution Principle (LSP)
Objects of a superclass should be replaceable with objects of its subtypes without altering the correctness of the program. This means that if you have a function that takes a superclass as an argument, you should be able to pass any object of a subtype to that function without any problems. This principle helps to ensure that your code is robust and reliable.
+ Subtypes seamlessly replace base types in code.
+ Superclass functions work correctly with any subtype object.
+ Ensures robust and reliable code behavior.

### Interface Segregation Principle (ISP)
Clients should not be forced to depend on interfaces they do not use. This means that you should break down large interfaces into smaller, more specific interfaces. This principle helps to reduce the amount of code that your classes need to depend on, making them more modular and reusable.
+ Clients only depend on interfaces they actually use.
+ Large interfaces split into smaller, specific ones.
+ Improves modularity and reusability of classes.

### Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions. This means that your code should be designed in a way that is independent of the specific implementation details of the objects it uses. This principle helps to make your code more flexible and easier to test.
+ High-level modules depend on abstractions, not low-level details.
+ Abstractions don't rely on concrete details, details depend on abstractions.
+ Enhances code flexibility and simplifies testing.
