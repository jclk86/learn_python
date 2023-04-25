#  making objects with class. Don't use dictionaries when you need methods

# Self is the instance, so if student = Student(), self is student. Can call whatever, but self is convention -- self must always be first - -whatevery put first is self
class Student:
    def __init__(self, name, grades):
      self.name = name
      self.grades = grades
      
    def average(self):
      return sum(self.grades) / len(self.grades)
      
      
      
student = Student("Bob", (70,54,90))

# A class is really just a dictionary where some of the keys are functions that automatically take the whole dictionary as the first argument (self). If you know what the keys of your dict will always be at code writing time, and you're going to have several functions that take the whole dictionary as an argument, you really want a class.

# with a class, you also get the syntactic sugar of accessing values with the mything.attribute syntax, rather than mything['attribute'], but it's the same thing.

# basically use class if you have related data and you need to manipulate it 

# print(student.average())

# MAGIC METHODS
#  __init__ gets called without dot notation reference when you make class 
# __methods__ get called automatically. 
# __str__ represents what you want to print by default when printing instance in string. Without it, you get machine and some object reference

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # calls when yo want to turn object into string
  # use this when you want to print a string to user
  # def __str__(self):
  #   return 'hey'
  
  # GOAL be unambiguous with this method - if possible, should return a string that allows to us recreate original object easily
  # __str__ will override cause python assumes you are dealing with user and __repr__ is for debugging, so comment out __str__ to see __repr__
  def __repr__(self):
    return f"<Person({self.name}, {self.age})>"
  
jim = Person('Jim', 36)

print(jim)