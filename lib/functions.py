#!/usr/bin/env python3

def greet_programmer():
     print("Hello, programmer!")

name='Guido'

def greet(name):
    print(f"Hello, {name}!") 
    return


def greet_with_default(name="programmer"):
     print(f"Hello, {name}!")
     return

def add(num1, num2):
    return num1 + num2
     
def halve(number):
    if not isinstance(number, (int,float)):  # Check if the number is of type int
        return None
    else:
        return number / 2

