#Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

#First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price
#Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "Repaired!"
  
#Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
      super.init(max_speed, condition, price):

  def boost(self):
    self.max_speed = max_speed * 2



#Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
      super.init(max_speed, condition, price):

  def flame_jet(self, other):
      other.condition = "TRASHED!"
    

  
#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

#Encapsulation
#All the data is bundled together in a way that lets only the classes that need to know something access the information it requires.

#Abstraction
#With the code being bundled together as it is, it's extremely reusable.

#Inheritance
#AnakinsPod inherits all the properties of Podracer as they're the same basic object.

#Polymorphism
#Inheritance is rather easy in this way. The code is rather flexible and new things can be added to each class to enhance functionality easily.

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#It would not. It's easiest to do this sort of problem this way because it's easiest to think of Podracers and models like them as classes.

  
#How in particular did Object Oriented Programming assist in the solving of this problem?
#Allowed the issue to be broken up into parts.