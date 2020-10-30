class Monster:
    def __init__(self, color, heads):
        self.color = color
        self.heads = heads

    def attack(self):
        print("Just attacked a Hero, Mu...hahahaha!!!")

# Create an instance/object/monster-character
mournsnake = Monster("Yellow", 4)
# Check if its created or not
print('I am a ' + str(mournsnake.heads) + ' headed monster.')
# Make an attack by the new monster
mournsnake.attack()