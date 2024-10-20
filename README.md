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

5.2 The `price_code_for_movie` method is implemented as a classmethod in Movie class. The reason for this are:
  1. Information Expert: The movie class already know all the attributes of a Movie.
  2. Low Coupling: From 1., if the method is implemented somewhere else, it would also needs to know the attributes of a Movie class. Therefore, implementing it in the Movie class will result in the least amount of coupling.