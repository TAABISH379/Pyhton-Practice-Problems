# Write a program to accept marks of 6 students and display them in a sorted
# manner

students=[]

for i in range(1,7):
    student=int(input(f"Enter makrs of student {i}: "))
    students.append(student)
students.sort()

print("Shorted marks: ", students)