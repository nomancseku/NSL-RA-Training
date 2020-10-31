class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print('I am attacking...')


class Fogthing(Monster):
    def make_sound(self):
        print('Grrrrrrrrrr\n')


class Mournsnake(Monster):
    def make_sound(self):
        print('Hiiissssshhhh\n')


fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()

mournsnake = Mournsnake("Mournsnake", "Red")
mournsnake.attack()
mournsnake.make_sound()
