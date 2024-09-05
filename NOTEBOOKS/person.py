class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def show(self):
    print("Hello, i'm {} and i am {}".format(self.name, self.age))