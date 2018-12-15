from math import sqrt, sin

print ("John Doe")

x=5
print ("x=%d" %x)

x = x+10
print ("x=%d" %x)

y=x
print ("y=%d" %y)

print (type(y))

a1=1
b1=5
c1=6

d = b1*b1 - 4*a1*c1

x1 = (-b1 - sqrt(d)) / 2*a1
x2 = (-b1 + sqrt(d)) / 2*a1

print ("The roots are %0.2f %0.2f" %(x1, x2))

print (type(x1))
print (type(x2))

print ("sin(x1) = %f" %sin(x1))
print ("sin(x2) = %f" %sin(x2))

C = 37
F = (9/5)*C + 32.0
print ("Fahrenheit equivalent of 37degC is %0.1f" %(F))

