#while loop review
fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# Lets make juice with these fruits

start_index = 0
max_index = len(fruits) - 1

while start_index <= max_index: # Work until this condition is True
    fruit = fruits[start_index]
    print(fruit + " Juice!")

    start_index = start_index + 1

#same work using for loop
    
fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# Lets make juice with these fruits
for fruit in fruits:
    print(fruit + " Juice!")


# using range in for loop
for i in range(10):
    print(i)

# using limited range in for loop
# start with 5 and ends with 9
for i in range(5, 10):
      print(i)

#with step size
# start with 5 and ends with 15 and step size 3
for i in range(5, 15, 3):
      print(i)
