std_class1 = 32
std_class2 = 45
std_class3 = 51

grp_class1 = 5
grp_class2 = 7
grp_class3 = 6

grp_sz_class1 = std_class1 // grp_class1
grp_sz_class2 = std_class2 // grp_class2
grp_sz_class3 = std_class3 // grp_class3


left_class1 = std_class1 % grp_class1
left_class2 = std_class2 % grp_class2
left_class3 = std_class3 % grp_class3

print("Number of students in each group:")
print("Class 1:", grp_sz_class1)
print("Class 2:", grp_sz_class2)
print("Class 3:", grp_sz_class3)

print("Number of students leftover:")
print("Class 1:", left_class1)
print("Class 2:", left_class2)
print("Class 3:", left_class3)
