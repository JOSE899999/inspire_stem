#This is a program to solve the quadratic equation
#Date : 20 /2/2024
#name : Ephraim

import math 

a =  float(input("enter coefficient of first term :"))
b = float(input("Enter coefficient of second term :"))
c = float(input("enter constant : "))

d=  (b**2) - (4 * a * c )

x_1 = ((-b + math.sqrt(d)) / 2 * a)
x_2 = ((-b - math.sqrt(d)) / 2 * a)

print("The solution of quadratic equation:",x_1)
print("The solution of quadratic equation:",x_2)

