import types


class Animal:
    ZOO_NAME = 'Mysore'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name is {self.name} and colour is {self.colour}")


def update_colour(self, colour):
    self.colour = colour


dog = Animal("Ramu")

dog.update_colour = types.MethodType(update_colour, dog)

dog.update_colour('brown')
dog.show()
