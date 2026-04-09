#Write a python program to find remainder when a number is divided by z.

a= int(input("Enter Dividend: "))
b= int(input("Enter Divisor: "))
q = a//b
r= a - (b*q)
print("The remainder is ",r)