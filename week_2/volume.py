#This is a program to calculate volume
#Date :20/2/2024
#Name :Ephraim

#Volume of a cylinder

import math

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
pi = float(math.pi)

b = (r * h * pi **2 )

print("The volume of cylinder ",b)

#Volume of sphere
import math
r = float(input("Enter the radius : "))
pi = float(math.pi)
c = float((4/3))

s = (r * c * pi **3)

print("The volume of sphere ",s)

#Volume of cone
import math 

r = float(input("Enter the radius : "))
pi = float(math.pi)
c = float(1/3)
h = float(input("Enter the height"))

v =(c * pi * r** 2 * h)
print("The volume of cone",v)

