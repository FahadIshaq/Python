# Number of students in each class
class_students = [32, 45, 51]
  
# Number of groups desired for each class
num_groups = [5, 7, 6]
print("Number of students in each group:")
for i in range(len(class_students)):
    students = class_students[i]
    groups = num_groups[i]
students_per_group = students // groups # Integer division to get the students per group
leftover = students % groups # Modulo operation to find the leftover students
print(f"Class {i + 1}: {students_per_group}")
print("\nNumber of students leftover:")
for i in range(len(class_students)):
    students = class_students[i]
    groups = num_groups[i]
    students_per_group = students // groups
    leftover = students % groups
    print(f"Class {i + 1}: {leftover}")