some_marks = [2, 4, 6, 32, 60, 65, 69, 76, 80, 85, 90]

avg_marks = some_marks[4:8]
print(avg_marks)

good_marks = some_marks[8:]
print(good_marks)

poor_marks = some_marks[:4]
print(poor_marks)

#index jump
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:9:3])

#negative index slice
squares = [1, 2, 5, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 4, 6, 7, 8]
print(squares[3:-4])

#list reverse
values = [3, 4, 5, 6, 7, 8]
print(values[::-1])

#some numeric operation on list
# Prints the minimum value among all the elements of the list below
print(min([1, 2, 3, 4, 0, 2, 1]))

# Prints the maximum value among all the elements of the following list
print(max([1, 4, 9, 2, 5, 6, 8]))

# Print sum of all the elements of the following list
print(sum([1, 2, 3, 4, 5]))
