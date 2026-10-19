#!/usr/bin/env python3

input = int(input("How many Fibonacci numbers do you want to print? "))

a = 0
b = 1

while input > 0:
    c = a + b
    print(a, end=" ")
    a = b
    b = c
    input -= 1
