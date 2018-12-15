'''
# Lecture note: Session 9 and 10

    lambda function
    Map
    Reduce
    Filter
    read and write files (text, binary)
'''
# ------------------------------ Lambda function ------------------------------#

# A lambda operator creates anonymous function
# Such a definition is not bound to a function identifier

# lambda x,y: x+y
# lambda x,y=12: x+y (default value of y is specified)

# lambda x,y: y=12, x+y (WRONG! can't use assignment inside lambda functino)
# You can't have assignment inside of lambda function

# lambda returns a function
f = lambda x,y: x*y
print (type(f)) # <class 'function'>

# Let's try sort a list of tuples using sort()
tlist = [(1,0), (10, 20), ("A", 2), ("B", -10)]

# return the second element of the tuple
tlist.sort(key=lambda t: t[1])
print (tlist)

def second(t): return t[1]
tlist.sort(key=second)

print (tlist)

# ------------------------------ Map ------------------------------#
# Map is a Python function that applies a function to a list

# map(f,x) ; Function f is applied to each element of an iterable x
f = map(lambda x: x[1], [(2,3), (3,4), (5,9)])
print (list(f)) # [3,4,9]

y = iter([3,4,5])
f = map(lambda x: x*3, y) # Function is applied to each element of the list
print (type(f)) # <class 'map'>
print (list(f)) # [9, 12, 15]

x = [1,2,3]
z = map(lambda y: y**y, x)
print (list(z)) # [1,4,27]

# x is an iterator,
x = iter([1,2,3])
f = map(lambda y: y**y, x)
print (list(f)) # [1,4,27]
print (list(f)) # [] # elements are exhausted, so it's all gone

# x2 is a list
x2 = [1,2,3]
f = map(lambda y: y**y, x2)
print (list(f)) # [1,4,27]
print (list(f)) # [] # elements are exhausted, so it's all gone

# -> the second element is converted into an iterator!!!

# ------------------------------ Reduce ------------------------------#
# Reduce is a Python function that applies a function to a sequence and reduce it to a single item
# You should import "functool" library to do Reduce
import functools

z = iter([1,2,3,4])
out = functools.reduce(lambda x, y: x**2+y**2, z) # the second element is iterator, so it is exhausting
print (out) # 1172
'''
1. [1,2,3,4] -> [f(1,2),3,4] = [5,3,4]
2. [5,3,4] -> [f(5,3), 4] = [34, 4]
3. [34,4] -> [f(34, 4)] = 1172

'''
# ------------------------------ Filter ------------------------------#
# Filter out all elements of a list that return True when a given function is applied
# So function should return True or False

z=["A",12,"c",22] # Remove all strings

# first element: function that returns True or False (it can be lambda)
# second element: iterator

out = filter(lambda x: type(x)==int, z)
print (list(out)) # [12, 22]

'''
Play and Learn

    P1: Try:
            f=lambda x,y=10: x+y
            f(2,3)
            f(4)

'''
f = lambda x,y=10: x+y

out = f(2,3)
print (out) # 5

out = f(4)
print (out) # 14

'''
Play and Learn

    P2: Write a lambda function 
    that when called with a tuple as input 
    returns True of the second item in the tuple is the square of the first item, else returns False. 
    Test your function with input (3, 9) and (3, 12).

'''
f = lambda tup: True if tup[0]**2 == tup[1] else False

out = f( (3,9) )
print (out) # True

out = f( (3, 6) )
print (out) # False

# -----------------------  File open, read, write and close -----------------------#

filename = "iris.txt"
f=open(filename, "r") # open file for read only

nextLine = f.readline()
print (nextLine) # 5.1,3.5,1.4,0.2,iris-setosa\n

f.close()

filename = "stats.txt"
f=open(filename, "w") # open file for writing only
f.write("Mean length="+str(35.23))
f.close()
