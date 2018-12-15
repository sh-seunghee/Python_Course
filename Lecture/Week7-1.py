'''
# Lecture note: Session 9 and 10

    learn OO programming (classes and objects)

'''
# -----------------------  OO programming ----------------------- #
# Class: A blueprint (template) for creating objects
# Object: An instance of a class created using the class blueprint

# Creating and using objects

class Animal:

    # __init__() is a constructor to initialize attributes (__init__() is a reserved method name)
    # __init__() is called automatically when you create an object
    def __init__(self, name="", owner="", vaccinated=False):
        self.name = name
        self.owner = owner
        self.vaccinated = vaccinated

    def set_owner(self, o):
        self.owner = o

    def set_name(self, n):
        self.name = n

# "self" refers to THIS object, to an instance of this class
# Thus, self.x is the "x" that is in THIS object

dog = Animal("Raja", "Aditya", True)
print(dog.name)
print(dog.owner)

dog.set_owner("John")
print (dog.owner)

horse = Animal()
horse.set_name("goodluck")
print (horse.name)

class Country:

    border = True

    def __init__(self, name, pop, area):
        self.name = name # copy the parameters into the object
        self.pop = pop
        self.area = area

    def set_pop(self, pop):
        self.pop = pop

    def get_static(self):
        return self.border

usa = Country("USA", 3.5, 10)
mexico = Country("Mexico", 1.2, 8)
france = Country("France", 1.2, 2.1)

countries = [france, usa, mexico]

d = []
for c in countries:
    print (c.pop)

print (usa.pop)
usa.set_pop(3.9)
print (usa.pop)

if usa.pop < mexico.pop:
    print ("mexico is larger")
else:
    print ("usa is larger")
'''
c = input()
c1, c2, c3 = c.split()
c2 = float(c2)
c3 = float(c3)

germany = Country(c1, c2, c3)

print (germany.name)
'''
# -----------------------  Instance and static variables ----------------------- #
# variables declared in a class declaration are considered "static", or "class" variables
# Static variables can be used where the class can be used.
# Variables assigned values inside a method in a class are instance variables.
# Instance variables are associated with an object

print (france.border)
print (usa.border)


print (france.get_static())

'''
Play and Learn

    (a) Create a class named Animal with attributes: 
        name	# String e.g., “Dog”
        group  	# string [use groups Invertebrates, Fish, Amphibions, Reptiles, Birds, and Mammels]
        char 	# list of characteristics of the animal
        found	# list of strings  denoting where is this animal found
    (b) Include __init()__ to initialize the attributes.
    (c) Create a method addChar () that inputs a  characteristic and adds it to the existing list of characteristics of an animal. 
    (d) Similarly, create a method add_whereFound() that inputs the name of a region where this animal is found and adds it to the where_found list. 
    (e) Use the Animal class to create at least three animals. Place these animals in a list.
    (f) Write a method named search() for an animal based on its group. The method inputs the list of animals and a group, and returns the name of each animal in that group; returns an empty list otherwise. (g) Test your program.

'''
class Animal2:

    def __init__(self, name, group, char, found):
        self.name = name
        self.group = group
        self.char = char
        self.found = found

    def addChar(self):

        newChar = input()
        self.char.append(newChar)

    def add_whereFound(self):

        region = input()
        self.found.append(region)

cat = Animal2("cat", "Mammels", "cute", "seoul")
dog = Animal2("dog", "Mammels", "cute", "usa")
bird = Animal2("bird", "Birds", "fly", "mexico")

animals = [cat, dog, bird]

def search(animals, group):

    commonType = []

    for animal2 in animals:

        if animal2.group == group:

            commonType.append(animal2)

    return commonType

output = search(animals, "Mammels")