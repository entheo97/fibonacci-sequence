#!/usr/bin/env python3

user_input = input("Enter a multi-digit number: ")

total_sum = 0
for digit in user_input:
    total_sum += int(digit)
expression = " + ".join(user_input)
print(f"{expression} = {total_sum}")
