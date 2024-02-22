#This is a program to calculate hire purchase
#Date : 21 /2 /2024
#Name : Ephraim

import math

p = float(input("Enter the principle"))
r =float(input("Enter the rate"))
n = float(input("Enter the time"))

h = (p *((1 + (r / 100))**n))

print("the hire purchase price is",h)
