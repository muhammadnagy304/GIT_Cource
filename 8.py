print("\n\n\n ")

class Food:

  def __init__(self, name, price):
    self.name = name
    self.price = price
    print(f"{self.name} is created from base class")

  def Eat(self):
    print("eat method from base class")

class Apple(Food):

  def __init__(self, name, price):
    super().__init__(name, price)
    print(f"{self.name} is created from derived class, {self.name}")


#food1 = Food("Pizza")
food2 = Apple("Pizza", 150)
#food2.Eat()

