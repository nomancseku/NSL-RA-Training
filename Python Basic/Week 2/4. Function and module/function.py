# Defining the function named hello
def hello():
    print("Hello World!")

# Calling the function to use it
hello()    

# Again calling the function
hello()



def show_double(x):
    print(x*2)

show_double(2)
show_double(100)


def make_sum(x, y):
    z = x + y
    print(z)

make_sum(5, 10)
make_sum(500, 500)


#multiple parameter handling
def make_sum(*args):
    sum = 0
    for num in args: # Here, args is like a Tuple which is (10, 20, 30, 40)
        sum += num
    return sum

print(make_sum(10, 20, 30, 40))


def print_dict(**kwargs):
    print(kwargs)
print_dict(a=1, b=2, c=3)


def print_dict(**kwargs):
    for args in kwargs:
        print("{0} : {1}".format(args, kwargs[args]))
print_dict(a=1, b=2, c=3)


def print_all(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
print_all(10, 20, 30, 50, b=5, c=10)

#যখন একটি ফাংশনকে ডিফাইন করা হয় তখন এর ভ্যারিয়েবল গুলোকে প্যারামিটার বলা হয়। আর যখন একটি ফাংশনকে কল করা হয় তখন সেই ফাংশনের প্যারামিটার হিসেবে যে ভ্যালু পাঠানো হয় তাকে আর্গুমেন্ট বলা হয়।
