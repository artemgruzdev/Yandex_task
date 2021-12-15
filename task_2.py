class AbstractCat:

    # def __init__(self, weight, leftover_food):
    #     self.weight = weight
    #     self.leftover_food = leftover_food
    #
    # def eat(self, food):
    #     self.food = food
    #
    #     # weight = 0
    #     # leftover_food = 0
    #     if self.weight <= 100:
    #         self.weight += food // 10
    #         self.leftover_food += food % 10
    #         if self.leftover_food >= 10:
    #             self.weight += self.leftover_food // 10
    #             self.leftover_food = self.leftover_food % 10
    #     print(self.weight, self.leftover_food)

    def __init__(self):
        self.weight = 0
        self.leftover_food = 0

    def eat(self, food):
        self.food = food
        weight = 0
        leftover_food = 0
        if weight <= 100:
            weight += food // 10
            leftover_food += food % 10
            if leftover_food >= 10:
                weight += leftover_food // 10
                leftover_food = leftover_food % 10



class Kitten(AbstractCat):

    def __init__(self, weight):
        self.weight = weight

    def meow(self):
        return 'meow...'

    def sleep(self):
        return 'Snore' * (self.weight // 5)


class Cat(Kitten):

    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def meow(self):
        return 'MEOW...'

    def get_name(self):
        return self.name

    def catch_mice(self):
        return 'Got it'


abscat = AbstractCat()
abscat.eat(125)
abscat.eat(17)
print(abscat)
kit = Kitten(21)
print(kit.sleep())
cat = Cat(83, 'Molly')
print(cat.meow())
print(cat.get_name())
