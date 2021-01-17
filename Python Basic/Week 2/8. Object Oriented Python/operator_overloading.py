class MyNum():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return (self.value * 2) + (other.value * 2)


a = MyNum(2)
b = MyNum(3)

c = a + b

print(c)