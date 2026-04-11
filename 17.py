# Take 5 numbers from user and store in a list. Print the largest.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

numbers=[a, b, c, d, e]
print(numbers)
print(f"The greatest number in list {numbers} is: ", max(numbers))
    
