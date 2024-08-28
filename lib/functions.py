#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    
greet_programmer()

def greet(name):
    print(f'Hello, {name}!')

greet('Kim')

def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')
    
greet_with_default()

def add(num1, num2):
    return(num1+num2)
    
y=add(3,5)
print(y)

def halve(number):
    if type(number) == int or type(number) == float:
        return number/2
    else:
        return None

print(halve(12.88))