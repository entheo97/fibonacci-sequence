#!/usr/bin/env python3


input = int(input("How many Fibonacci numbers do you want to print? "))

a = 0 
b = 1 

while input > 0:
    c = a + b
    print(a, end=" ") # print on one line 
    a = b 
    b = c 
    input -= 1 # the loop runs infinitely without this 

# this chart shows the values of a, b, and c over  10 rounds

# r1  a = 0,  b = 1,  c = 1
# r2  a = 1,  b = 1,  c = 2
# r3  a = 1,  b = 2,  c = 3
# r4  a = 2,  b = 3,  c = 5 
# r5  a = 3,  b = 5,  c = 8
# r6  a = 5,  b = 8,  c = 13
# r7  a = 8,  b = 13, c = 21
# r8  a = 13, b = 21, c = 34
# r9  a = 21, b = 34, c = 55
# r10 a = 34, b = 55, c = 89
