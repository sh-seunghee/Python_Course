'''
# Lecture note: Session 1 and 2

    Comment
    Assignment
    Complex number
    Math library
    Square, division
    printing
'''
# ------------------------------ Comment ------------------------------#
# This is a comment.

'''
    This is comment for multiple lines.
'''
# ------------------------------ Assignment ------------------------------#

# This statement is called assignment
temp = 43.9
fc = "F"    # variable name: fc

temp = temp + 1
print (temp)

# you can use underscore as a part of name of a variable
# there are some convention whether you decided to use underscore or not
_age_ = 45
print (_age_)

# Convention: All class names begin with an uppercase letter, all other names begin with a lower case name
ageOfChild = 3
age_of_child = 3

# names are case sensitive
A = 1
a = 2
print (A)

a =True
name = "CS50100"    # String constant
print (name)
sem = 'fall'

print (sem+name)

# Every variable has a name; its type is the type of its value
a = 2
# the name is a and its type is int
print (type(a))

# ------------------------------ Complex number ------------------------------#

a = 3.2+4j  # Type of a changed to complex
print (type(a))

# ------------------------------ Math library ------------------------------#

import math

a = math.sin(3.14159)
print (a)

print (math.pi)
print (math.sin(math.pi))

# you can separate them by ; when assignment
x=1; y=2; z=3.0

x = 3+4*2.5
print (x)

# multiple assignment works
a = b = c = 1
print (a)
print (b)


d = math.sqrt(2)
print (d) #1.41421356

'''
Excercise 1

Problem: Given the value of x in radians, estimate the value of sin(x)

Method:

    1. Use Google to find the first three terms in the Taylor series expansion of sin(x)
    2. Wrtie Python code to estimate sin(x) for x=pi using only the first three terms.
    3. Use the Python math library to calculate sin(x) for x=pi
    4. Print the estimate and the absolute value of the difference
        between the estimate and the value computing by using the sin() function from the math library.
'''
x = math.pi

estimate = x - (pow(x, 3) / math.factorial(3)) + (pow(x, 5) / math.factorial(5))
mathlib = math.sin(x)

print ("The estimate: %0.3f" %(estimate))

diff = estimate - mathlib
print ("The difference : %0.3f" %(diff))

# ------------------------------ square, divisions ------------------------------#

a = 5
x = a**2    # x is a complex number obtained by squaring d
print (x)

d = math.pow(2,8)
print (d) # 256.0

# it gives you divisions (In python2, it gives you 1)
print (9/5) # 1.8

# it gives you integer division
print (9//5) # 1

# ------------------------------ printing ------------------------------#

# beautiful printing
a = 1
b = 2.987
c = 6.022140857e23
d = "Hello"

print (a,b,c,d)

# formatted string
print ("a=%g, b=%0.3f d=%.2E, d=%s"%(a,b,c,d))

# %g: Best fit
# %0.3f: Floating point to 3-digits
# %.2E: Exponential with 2-digits
# %s: String

# New line
print ("a=%g, \nb=%0.3f \nd=%.2E, \nd=%s"%(a,b,c,d))
