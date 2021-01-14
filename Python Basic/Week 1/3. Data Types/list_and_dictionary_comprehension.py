num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num_list = []
for num in num_list:
    if num % 2 == 0:
        even_num_list.append(num)
print (even_num_list)

#using list comprehension
even_num_list = [even_num for even_num in num_list if even_num % 2 == 0]
print (even_num_list)


# can be written as
even_num_list = [
  num
  for num in num_list
  if num % 2 == 0
]
print(even_num_list)


#list comprehension using nested loop
matrix_1d = []
matrix_2d = [[1, 2, 3],
            [4, 5, 6]]

for row in matrix_2d:
    for num in row:
        matrix_1d.append(num)
print(matrix_1d)
# now using list comprehension
matrix_2d = [[1, 2, 3],
            [4, 5, 6]]
matrix_1d = [num for row in matrix_2d for num in row]
# if we want to take square of num
matrix_1d1 = [num**2 for row in matrix_2d for num in row]
print(matrix_1d1)
