roles = ("Admin", "Operator", "User")   
# Or following line will create the same Tuple
# roles = "Admin", "Operator", "User" 

print(roles[0])

permissions = (("Admin", "Operator", "Customer"), ("Developer", "Tester"), [1, 2, 3], {"Stage": "Development"})

print(permissions[3]["Stage"])


numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

#this is interesting
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
