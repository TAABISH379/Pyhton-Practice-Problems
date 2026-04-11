# Write a program to sum a list with 4 numbers.

numbers=[]

for i in range(1,5):
    number=int(input(f"Enter number {i}: "))
    numbers.append(number)

print(f"Sum of list {numbers} is: ", sum(numbers))