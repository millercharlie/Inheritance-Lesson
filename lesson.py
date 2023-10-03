# As you may notice from the previous lesson practice, many of these vehicle classes have the same variables

# They all have a maker, year, etc

# How can we streamline this code even further?

# This is where inheritance comes in

# Inheritance allows you to create a 'parent' class

# Each other class is called a 'child' class

# Each child will inherit the variables of the parent class unless overriden

# To write a parent class for this scenario, you can do something like this

class Vehicle:
  def __init__(self, maker, year):
    self.maker = maker
    self.year = year

  def add_year(self):
    self.year += 1


# We now have a parent class with only the variables that every child class inherits!

# Now, the other classes would look like this:

class Car(Vehicle):
  def __init__(self, maker, year, type):
    super().__init__(maker, year)
    self.type = type

# The super() keyword refers to the 'super class', which is the 'parent' class Vehicle


class Motorcycle(Vehicle):
  def __init__(self, maker, year, color, miles_driven):
    super().__init__(maker, year)
    self.color = color
    self.miles_driven = miles_driven


class Airplane(Vehicle):
  def __init__(self, maker, year, airline, miles_flown, seat_capacity, is_luxury):
    super().__init__(maker, year)
    self.airline = airline
    self.miles_flown = miles_flown
    self.seat_capacity = seat_capacity
    self.is_luxury = is_luxury


# Besides just inheriting variables, the child classes can also inherit methods!

boeing = Airplane('Boeing', 2021, 'jetBlue', 2056, 203, 'yes')

print(boeing.year)
boeing.add_year()
print(boeing.year)














