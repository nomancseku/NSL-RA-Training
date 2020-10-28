file_to_work = open("Test.txt", "r")
lines = file_to_work.readlines()
print(lines)
file_to_work.close()



file_to_work = open("Test.txt", "r")
for my_line in file_to_work:
    print(my_line)
file_to_work.close()
