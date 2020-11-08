class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
# print(s.__egg) will give error
print(s._Spam__egg)