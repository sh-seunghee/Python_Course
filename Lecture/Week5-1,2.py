import numpy as np

'''
# Lecture note: Session 7 and 8

    [ Week5-1 ]
    SWaTDataset.xlsx (Processing time-series data)

    [ Week5-2 ] 
    numpy (create and use arrays)
    List comprehension
    matplotlib
    scipy

    * A sample of ML tools
    scikit-learn: For classification, regression, and clustering
    PyTorch: Dynamic neutral networks: Deep-learning
    TensorFlow: Deep learning
'''

def compute_count(state, index):

    count = 1
    while index < len(data):

        next_state = data[index+1]
        index += 1

        if state == next_state:
            count += 1
        else:
            break

        if (index == len(data)-1):
            break

    return (count, index) # (count, index)

v_o=0
v_c=0
v_t=0

v_open=2
v_closed=1
v_trans=0

data=[1,1,1,0,0,0,0,2,2,1,1,1]

index=0
v=data[index] # First item in data

while index < len(data)-1:

    if v==v_open:
        valve_open, index = compute_count(v_open, index)
        v_o += valve_open
    elif v==v_closed:
        valve_closed, index = compute_count(v_closed, index)
        v_c += valve_closed
    else:
        valve_trans, index = compute_count(v_trans, index)
        v_t += valve_trans

    v=data[index]

print (v_o, v_c, v_t) # 2 5 4

# ------------------------------ numpy ------------------------------#
# An "array" used as an alternate to "Lists" in Python
# Arrays: useful in scientific computing

# Difference:

# Array: Homogenous data structure (should be the same type)
# List: Heterogeneous data structure

# Array: Created and manipulated using numpy
# Array: Used in scipy, matplotlib, and ML libraries such as scikit-learn

# 1D array
height1 = [6.2, 5.7, 4.9, 5.9, 6.3]

# 2D array
height1 = ([6.2, 5.7, 4.9, 5.9, 6.3])
height2 = ([4.8, 5.6, 5.9, 4.9, 6.1])
height3 = ([6.4, 5.9, 6.1, 5.8, 6.3])
height4 = ([5.7, 5.7, 4.9, 5.9, 5.8])

x=[1,2,3]

# You will get an array
a = np.array([1,2,3]) # array([1,2,3])

# Get dimension
print (a.ndim) # 1

# Get shape (Vector with three element)
print (a.shape) # (3,)

# Access to array
print (a[1])

x = [1,2,3]
y = [4,5,6]

a = np.array([x,y])
# array([ [1,2,3],
#         [4,5,6] ])
print (a.ndim) # 2
print (a.shape) # (2, 3)

a = np.array([
    [[1,2,3], [3,4,5], [6,7,8]],
    [[9, 10, 11], [12, 13, 14], [15, 16, 17]]
])

print (a.ndim) # 3
print (a.shape) # (2,3,3)

print (a[0])
print (a[0][0])

# ---------- Many other way to create array

# three elements that equally spaced
x = np.linspace(1,10,3) # [1. 5.5 10.]
print (x)

# five elements that equally spaced
x = np.linspace(-10, 10, 5) # [-10. -5. 0. 5. 10.]
print (x)

# create array of all zeros
x = np.zeros(5) # [0. 0. 0. 0. 0]
print (x)

x = np.ones(3)
print (x) # [1. 1. 1.]

x = np.ones(3, dtype=int)
print (x) # [1 1 1]

x = np.ones(3, dtype=complex)
print (x) # [1.+0.j 1.+0.j 1.+0.j]

a = np.zeros((2,3,4))
# a.ndim = 3
# a.shape = (2,3,4)
print (a)

a = np.ones((2,3), dtype=bool)
print (a)


'''
Play and learn
'''

# P1: Learn to use random.randint(a,b): Generate a random integer between a and b
import random
x = random.randint(3,5)
print (x)

# P2: Create a 1D array of 5 random integers each between 1 and 10.
a = [random.randint(1,10) for i in range(10)] # List comprehension
print (a)
b = np.array(a)
print (b)

# P3: Create a 2D array of random integers between 1 and 10 of shape (2,5).

a = [random.randint(1,10) for i in range(5)] # List comprehension
b = [random.randint(1,10) for i in range(5)] # List comprehension
c = np.array([a,b])
print (c)

# P4: Create a 3D array of random integers between 1 and 10 of shape (3,2,5).

a = [ [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)] for i in range(2)] # List comprehension
b = [ [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)] for i in range(2)] # List comprehension
c = [ [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)] for i in range(2)] # List comprehension

a1 = np.array(a)

d = np.array([a,b,c])

print (d)
print (d.ndim)
print (d.shape)

# what is the advantage of array over list
# = You can apply a function to every element of the array!

def f(x): return (x*x)

a = np.array([[1,2,3],[4,5,6]])
print (f(a))
# array( [[1,4,9], [16,25,36]]

#f([1,2,3]) # This doesn't work; applying list doesn't work

a = np.array([1,2,3])
b = np.array([4,5,6])

c = a+b
print (c) # array[(5,7,9)]

c = a*b
print (c) # array([4,10,18)]

c = np.dot(a,b)
print (c) # 32

# In ML, you better use array, not list because it's more effcient
d = a+2
# Low dimension (2) is upgraded to high dimension
print (d) # array([3,4,5])


