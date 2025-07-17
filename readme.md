# To-Do List Application in Python

This project is a simple yet functional application for managing daily tasks, written entirely in an Object-Oriented style using Python.

## About This Project

This project was developed as a practical exercise to learn and deeply master the key concepts of Object-Oriented Programming (OOP). The main goal was to apply software engineering principles to build a real, tangible application from scratch.

## Features

* Add new tasks to the list.
* Display all tasks along with their completion status.
* Mark a task as "completed".
* Multi-file structure for better code organization.

## Core Concepts Implemented

This project serves as a demonstration of the following skills:

* **Object-Oriented Programming (OOP):** The entire application is designed and implemented based on OOP principles.
* **Classes and Objects:** Utilizes `Task` and `TodoList` classes to model the application's logic.
* **Constructor (`__init__`):** For initializing objects with a default state.
* **Magic Methods (`__str__`):** To provide a clean and readable string representation of objects.
* **Composition:** The `TodoList` class acts as a manager that contains and controls a list of `Task` objects.
* **Working with Modules:** The project is split into separate files (`Task.py`, `TodoList.py`, `main.py`) to improve readability and maintainability.
* **Error Handling:** Validates user input to prevent potential errors.

## How to Run

1.  Ensure all three files (`Task.py`, `TodoList.py`, and `main.py`) are in the same directory.
2.  In your terminal, run the following command:
    ```bash
    python main.py
    ```

## Future Improvements

* Implement features to delete and edit tasks.
* Add data persistence by saving tasks to a file (JSON or CSV) so data is not lost when the program closes.
* Add a priority or due date feature for tasks.