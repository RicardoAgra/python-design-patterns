# python-design-patterns

[Tuturial](https://www.youtube.com/watch?v=NU_1StN5Tkk)

## Concepts

### Abstraction

Abstration means we should hide unnecessary details in our classes and objects in order to reduce complexity.
The advantages are:

-   Less complexity when using the class due to a smaller API surface.

### Encapsulation

Encapsulation is the devision of a program into disctinct components which have limited interaction.
Advantages of Encapsulation:

-   Easier to test: Each component can be tested seperatly.
-   Modularization: New functionality can be developed based on the existing code base, wihtout the need to right extra code or duplicated code.

### Inheritance

## Design Patterns

### Memento

The memento desing pattern solves the need to go back in the state of an application.

### State Pattern

The state pattern is used when a Class Method's behavior changes based on a Class Property. In order to avoid using logical jumps that can even become nested several layers deep as the class complexity increases, the class property can be converted into a polymorphic class that either implements an interface or extends an abstract class.
The main class can now delegate to the polymorphic property, that is now responsible for handling the event.
