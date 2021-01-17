file_to_work = open("noman.txt", "r")
content = file_to_work.read()
print(content)
file_to_work.close()


print("\n\n\n\n\n")


file_to_work = open("noman.txt", "r")
just_one_character = file_to_work.read(1)
print(just_one_character)

remaining_four_characters = file_to_work.read(4)
print(remaining_four_characters)

rest_of_the_file = file_to_work.read()
print(rest_of_the_file)

file_to_work.close()
