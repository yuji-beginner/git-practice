from greeting import Greeting
from burgerGenerator import BurgerGenerator

print("this is main")

gr = Greeting("Hello, World!")
gr.greet()

burgers = ["hamburger", "cheese burger", "chicken burger"]
bg = BurgerGenerator(burgers)
bg.generate()