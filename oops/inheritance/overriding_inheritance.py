class Human:
    # num_eyes = 0

    def __init__(anything):
        anything.num_eyes = 2
        anything.num_nose = 1

    def work(self):
        print('yes i work')

    def eat(self):
        print("Human eat")


class Male(Human):

    # def __init__(self):
    #     super().__init__(self)

    def work(self):
        print("Male also work")

    def details(self):
        print(f"{self.num_eyes} - {self.num_nose}")


male_1 = Male()
male_1.work()
male_1.eat()
male_1.details()
print(male_1.num_eyes)
