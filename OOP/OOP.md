## Object Oriented Programming
OOP is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

### Structure 
- **Classes**
    - User-defined data types that act as the blueprint for individual objects, attributes and methods
- **Objects**
    - Instances of a class created with specifically defined data 
- **Methods**
    - Functions that are defined inside a class that describe the behaviors of an object
    - Each method contained in class definitions starts with a reference to an instance object
    - The subroutines contained in an object are called instance methods
    - Reusable and keep functionality encapsulated inside one object at a time
- **Attributes**
    - Defined in the class template and represent the state of an object
    - Objects will have data stored in the attributes field. Class attributes belong to the class itself

### Principles
- **Encapsulation**
    - All important information is contained inside an object and only select information is exposed
    - The implementation and state of each object are privately held inside a defined class
    - Other objects do not have access to this class or the authority to make changes
    - They are only able to call a list of public functions or methods
    - This characteristic of data hiding provides greater program security and avoids unintended data corruption
- **Abstraction**
    - Objects only reveal internal mechanisms that are relevant for the use of other objects, hiding any unnecessary implementation code
    - The derived class can have its functionality extended
- **Inheritance**
    - Classes can reuse code from other classes
    - Relationships and subclasses between objects can be assigned, enabling developers to reuse common logic while still maintaining a unique hierarchy
- **Polymorphism**
    - Objects are designed to share behaviors and they can take on more than one form
    - The program will determine which meaning or usage is necessary for each execution of that object from a parent class, reducing the need to duplicate code
    - A child class is then created, which extends the functionality of the parent class
    - Polymorphism allows different types of objects to pass through the same interface.

### Benefits
- **Modularity**: Encapsulation enables objects to be self-contained, making troubleshooting and collaborative development easier.
- **Reusability**: Code can be reused through inheritance, meaning a team does not have to write the same code multiple times.
- **Productivity**: Programmers can construct new programs quicker through the use of multiple libraries and reusable code.
- **Easily upgradable and scalable**: Programmers can implement system functionalities independently.
- **Interface descriptions**: Descriptions of external systems are simple, due to message passing techniques that are used for objects communication.
- **Security**: Using encapsulation and abstraction, complex code is hidden, software maintenance is easier and internet protocols are protected.
- **Flexibility**: Polymorphism enables a single function to adapt to the class it is placed in. Different objects can also pass through the same interface.

### Criticism
- Overemphasizes the data component of software development
- Does not focus enough on computation or algorithms 
- May be more complicated to write
- Take longer to compile

### Alternative methods to OOP
- **Functional programming**
    - Includes Erlang and Scala (used for telecommunications and fault tolerant systems)
- **Structured or modular programming**
    - Includes PHP and C#
- **Imperative programming**
    - Focuses on function rather than models
    - Includes C++ and Java
- **Declarative programming**
    - Involves statements on what the task or desired outcome is but not how to achieve it
    - Include Prolog and Lisp
- **Logical programming** 
    - Based mostly in formal logic and uses languages such as Prolog
    - Contains a set of sentences that express facts or rules about a problem domain
    - It focuses on tasks that can benefit from rule-based logical queries
