'''
# Lecture note: Session 5 and 6

    Mutability: lists, strings
    Tuples
    Conditions
    if-else statement
    define function
'''
# ------------------------------ Mutability ------------------------------#
# List is mutable whereas string is not mutable

s = "Hello"
s.replace("H", "Y") # s doesn't change. String is not mutable!
print (s)

newS = s.replace("H", "Y")
print (newS)    # newS has the new string replaced with Y

myList = [3,14,-2]
myList.remove(-2) # This change the given input and not giving you a new list
# It's changing the same list

# newList doesn't have anything and its type is none-type
newList = myList.remove(3)
print (newList) # print 'None'

# ------------------------------ Tuples ------------------------------ #
# Tuple is collection of Python objects
# It can have different type of objects like list!

# Tuple is not mutable
# but if it has a mutable object inside of the tuple, then that can be changed

t = (3,4,5)
print (type(t)) # <class 'tuple'>
print (t[1]) # 4

# Difference between tuple and list
# *** Tuple is not mutable
# so t[1]=7 will give you an error

t = ("H", 5, "y")
t = (5, [10,15,17], 99) # It has 3 elements in tuple
print (len(t)) # 3

# The type of second element is list so is the second element mutable?
# Try!
t[1][1] = 77
print (t) # Yes! it changes
# Tuples are immutable
# but if it has a mutable object inside of the tuple, then that can be changed

# ------------------------------ Conditions ------------------------------ #
# A condition is an expression that evaluates to True or False
# Boolean constants: True and False
# Relational operators: <. <=, >, >=, !=, ==
# Logical operators: and, or, not ------ for Compound conditions

print ("hello"=="Hello") # False bec. python is case-sensitive

text = "\end"
if text=="\End" or text=="\end":
    print ("done")
elif text=="CS501":
    print ("Python")
elif text=="CS180":
    print ("JAVA")
else:
    print ("Error")

'''
In-class exercise-1

    Write a program that creates a list of items input from the keyboard. 
    Each item is input on one line.  
    Ignore (do not add to the list)  any input that  is 0. 
    The  end of input is indicated when an “\end” is entered. 
    Print the list crated.
'''
output = []
end="\end"
newtext=""

while newtext != end:
    newtext = input()
    if newtext != "0" and newtext != "\end":
        output = output + [newtext]

#output.remove(end)
print(output)

'''
In-class exercise-2

    Write a program that
    (a) inputs a string s,
    (b) Inputs another sequence of strings, one at a time,
         until the string ‘\end’ is entered, and 
    (c) prints the number of times s occurs in the strings 
        that are input subsequently.
'''
end="\end"
newtext = ""

search=input("Enter string to be searched.")
count = 0

while newtext != "\end":
    newtext = input()
    if (newtext == search):
        count += 1

print (count)

# -------------------------- Use defined functions -------------------------- #

# parameters is LOCAL to a function
# EXCEPT FOR LIST AND DICTOINARY!!!!! List element can be changed

x = 1 # Global variable
def f(x): # This x is local to this function
    x=5

f(7)
print (x) # 1

# Except for list

def g(x):
    x[0]=99

y = [1,2,3]
g(y)
print (y) # 99, 2, 3

# Let's try with tuple
z = (1,2,3)
#g(z) # This gives an error cause tuple cannot be changed!

s = "Hello"
#g(s) # This gives an error! String is not mutable

def f(x,y): return x+y # This x,y are formal parameters
x=[1,2]
y=[3,4]
print (f(x,y)) # [1,2,3,4]

'''
Play and learn 1

    Write a function that takes a list of numbers as input 
    and returns the sum of all numbers. 
    [Do not use the sum() function; use a loop to add.]

'''
def num_sum(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

print (num_sum([1,2,3,4]))

'''
Play and learn 2

    Write a function that takes a string and a list of letters as input.
    It removes all letters from the string that are in the list.

'''
def pl2(s, l):

    for i in range(len(l)):
        s = s.replace(l[i], "")

    return s

print (pl2("Hello", ["H", "o"]))
