# Now, we are going to practice with inheritance!

# To do this, we are going to create a family tree with grandparents, brothers, sisters, and parents, and yourself!

# To begin, create the 'Person' class

# Some starter code is provided below

class Person:
  def __init__(self, name, age, hometown):
    self.name = name
    self.age = age
    ...

  # Give the class a birthday function to add one year to your age

  def birthday(self):
    ...


# Now, create the Parent (person) class, which inherits the name and age from the person class

# In addition, add a variable called is_mother that is a boolean

class Parent(Person):
  def __init__(self, name, age, hometown, is_mother):
    ...
    super().__init__()
    

  # override the birthday function that adds amount to the birthday
  def birthday(self, amount):
    ...

mom = Parent('mom', 35, 'Arcadia', True)


# class Child(Person) with a name, hometown, mood

  