my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : "What?"}
my_nums[4] = 16

print(my_nums)

#adding new
my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
my_nums[5] = 25

print(my_nums)


#finding the key
nums = {1: "one", 2: "two", 3: "three"}

print(1 in nums)
print("three" in nums)
print(4 not in nums)


# get() function
my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums.get(5))

# default value with get()
my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums.get(5, "5 not in my numbers!"))
