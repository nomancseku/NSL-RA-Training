file_to_work = open("write.txt", "w")
file_to_work.write("I am writing!!!")
file_to_work.close()

file_to_work = open("write.txt", "r")
print(file_to_work.read())
file_to_work.close()



file_to_work = open("testing.txt", "w")
is_writing_done = file_to_work.write("I am writing in file!!!")
#print(is_writing_done)
if is_writing_done:
    print("Yes, {0} byte(s) has been written!".format(is_writing_done))
file_to_work.close()
