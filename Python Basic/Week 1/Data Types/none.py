print(type(None))

# see returning none!
def my_func():
    print("Printing Hello")

what_i_got = my_func()
print(what_i_got)

# setting argument value
def my_func(x = None):
    if x:
        return x * x
    else:
        return 0

print(my_func())
print(my_func(5))
