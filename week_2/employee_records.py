#This is a program to show an employees salary before and after increase
#Date : 21 /2 /2024
#Name : Ephraim

f_name = input("Enter your first name : ")
s_name =  input("Enter your second name : ")
salary = float(input("Enter your salary : "))
bonus = float(input("Enter your bonus : "))
s1= (salary + bonus)

print("My name is",f_name+s_name)
print("The original salary and bonus is ",s1)

p = salary
r =float(input("Enter the rate : "))
b =float(input("Enter the bonus change : "))

h = (p + (p * (r / 100)))
ns =(h + (bonus + b ))
print("My name is",f_name+s_name)
print("the new salary and bonus is",ns)
