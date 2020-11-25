def make_twice(func, arg):
	return func(func(arg))
def add_five(x):
	return x + 5

print(make_twice(add_five, 10))


def my_pure_function(a,b):
	c = (2 * a) + (2 * b)
	return c
	
print(my_pure_function(5,10))


my_list = []
def my_impure_function(arg):
	my_list.append(arg)
	
my_impure_function(10)
print(my_list)
