"""
Write a program that takes an integer input and checks if it's even number.
Prints out 'True' if the number is even and 'False' if the number is not even.

e.g.
Input: 2
Output: 2 is even

Input: 3
Output: 3 is not even
"""

number = float(input("give your number:"))
if number == 0:
    raise ValueError("zero doesn't play!!!")
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is not even")
