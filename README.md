## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
2.1 The code smell that suggest moving `get_price_code` from Movie to Rental is "Feature Envy". Since the price code is moved to Rental, the `get_price_code` method in Movie needs to access the data from Rental.
2.2 The design principle that suggest this refractoring is "Information Expert". Which is to put a method in a class that has the most information needed to perform that method.