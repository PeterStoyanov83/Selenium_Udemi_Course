"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""


class Calculator:

    def add(self, a, b) -> None:
        return a + b

    def substract(self, a, b) -> None:
        return a - b

    def multiply(self, a, b) -> None:
        return a * b

    def divide(self, a, b) -> None:
        return a / b


calculator = Calculator()
print(calculator.add(2, 3))
print(calculator.substract(2, 3))
print(calculator.multiply(2, 3))
print(calculator.divide(2, 4))

