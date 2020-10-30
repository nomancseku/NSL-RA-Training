class Monster:
	#class attribute
    identity = "negative character"

    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a Hero, Mu...hahahaha!!!")


mournsnake = Monster("Yellow", 4)
tangleface = Monster("Red", 3)

print('I am a ' + str(mournsnake.heads) + ' headed ' + mournsnake.identity)
print('I am a ' + str(tangleface.heads) + ' headed ' + tangleface.identity)


print(Monster.identity)
# because it is a class attribute