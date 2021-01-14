# start with 10
# end with 0
# step size -2
for i in range(10, 0, -2):
     print(i)


#user defined function for float
# we need all of those three argumet, such as  start, stop, step
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
for i in frange(0.5, 1.0 ,0.1):
         print(i)

#iterating with string
for letter in 'Python': # Here "Python" acts like a list of characters
    print(letter)
