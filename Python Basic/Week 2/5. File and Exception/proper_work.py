try:
    file_to_work = open("Test.txt", "r")
    content = file_to_work.read()
    print(content)
finally:
    file_to_work.close()

# best practice with file....
with open("Test.txt") as f:
    print(f.read())