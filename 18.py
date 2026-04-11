# Store 6 marks in a list and print them in sorted order.

marks=[]

for i in range(1,7):
    student=int(input(f"Enter marks of student {i}: "))
    marks.append(student)

print("Sorted marks: ", sorted(marks))