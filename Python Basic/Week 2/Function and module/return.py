def get_larger(x, y):
    if x > y:
        return x
    else:
        return y

larger_value = get_larger(23, 32)
print(larger_value)

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))


#Comment and doc string
# few variables below
x = 10
y = 5

# make sum of the above two variables
# and store the result in z
z = x + y

print(z) # print the result
# print (x // y)
# another comment

def greet(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

def greet(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

# What the fucntion does?
print(greet.__doc__)

# Make sense, now lets use it    
greet("Hello World")


def square_root(n):
    """Calculate the square root of a number.

    Args:
        n: the number to get the square root of.
    Returns:
        the square root of n.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.

    """
    pass
