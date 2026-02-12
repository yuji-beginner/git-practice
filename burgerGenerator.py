import random

class BurgerGenerator:
    def __init__(self, burger_list):
        self.burger_list = burger_list

    def generate(self):
        random_burger = random.choice(self.burger_list)
        print(random_burger);

if __name__ == "__main__":
    burgers = ["hamburger", "cheese burger", "chicken burger"]
    bg = BurgerGenerator(burgers)
    bg.generate()