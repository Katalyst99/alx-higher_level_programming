# 0x0C. Python - Almost a circle

## Table of Contents
* [Description](#description)
* [Learning Objectives](#learning-objectives)
* [Files](#files)
* [Python Scripts](#python-scripts)
* [Python Unit Tests](#python-unit-tests)
* [Authors](#authors)

## Description
In this project, one implements various aspects of object-oriented programming in Python. The project involves creating a base class called `Base`, along with two other subclasses `Rectangle` and `Square`. These classes represent shapes and methods are implemented to calculate area, display shapes, serialize and deserialize objects, and deal with different features of inheritance. Tests were created implementing unittesting.

## Learning Objectives
* Understand the principles of Object-Oriented Programming (OOP) in Python
* Implement classes and inheritance
* Utilize private attributes, getter/setter methods, class methods, and static methods
* Implement unit tests using the `unittest` module
* Serialize and deserialize objects using JSON
* Handle and use *args and **kwargs in functions
* Write and read JSON files

## Files
* `tests/test_models/`: Folder containing unit tests for the classes.
* `test_base`: File containing unit tests for `Base` class.
* `test_rectangle`: File containing unit tests for `Rectangle` class.
* `Models/`: Folder containing classes for the project.
* `__init__.py`: With this file, the folder will become a Python package
* `base.py`: File containing `Base` class and its attributes, The class will the “base” of all other classes in this project.
* `rectangle.py`: File containing `Rectangle` class that inherits from `Base` 

## Python Scripts
* All Python scripts are executable.
* Use `pycodestyle` for code style compliance.
* Modules, classes, and functions should be documented according to the provided specifications.

## Python Unit Tests
* All test files are located in the `tests/` folder and start with `test_`.
* Use the `unittest` module for writing unit tests.
* Test files and folders organization should match the project structure.
* Unit tests must be in: tests/test_models/test_base.py
* Execute all tests using `python3 -m unittest tests/test_models/test_base.py`.

## Authors
* Katleho Lekale(https://github.com/Katalyst99) - @katleho_lekale(https://twitter.com/katleho_lekale)

