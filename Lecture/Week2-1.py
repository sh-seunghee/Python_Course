'''
# Lecture note: Session 3 and 4

    keyboard input
    Read multiple values from keyboard
    List
    Range
    Loops (for and while)
'''

# ------------------------------ Keyboard input ------------------------------#
x=input()
print (type(x)) # <class 'str'>

y=input("Enter your city")
print (type(y)) # <class 'str'>

z=input("Enter today's temperature")
print (type(z)) # <class 'str'>

# What is the type of x?
# whatever your enter, it is always 'String'!

# if you wanna convert it to int
x = int(x)
print (type(x)) # <class 'int'>

x = float(x)
print (x)

# you might get error msg 'Could not convert string to float'
x = 'Wset Lafayette'
#y = float(x)
#print (x)

# ------------------------------ Read multiple values ------------------------------#

m = input("Enter names of first three months in an year:")
# Jan Feb Mar
months = m.split()

print (type(months))    # <class 'list'>
print (months)  # ['Jan', 'Feb', "Mar']

months = m.split("&")   # you can separate it using some other separator other than space which is default
print (months)

# Play and learn

'''
p1. Input a sequence of numbers separated by a comma.
    Separate the numbers and print them on separate lines. 
    What happens when by mistake you put two commas in a sequence? 
    Play with integers and floats. 
    Try formatting the output.

p2. 
    Input a sequence of numbers separated by exactly one space. 
    Separate the numbers and print them on separate lines. 
    Can you print them on one line?

p3. 
    Input a sequence of numbers separated by one or more spaces. 
    Separate the numbers and print them on separate lines.
'''
p1 = input()
p1s = p1.split(",")

print (p1s)
# It has empty string element in the list when putting two commas in a sequence
# so if you try to convert elements in the list into int, the empty string will be a probelm
p2 = input()
p2s = p2.split(" ", 1)

p3 = input()
# input: 3   4   2   1
p3s = p3.split(" ")

# There will be a many strings which is empty string
print (p3s) # ['3', '', '', '4', '', '', '2', '', '','1']

# ------------------------------ List ------------------------------#
# Lists - Sequence of objects

# Types can be mixed
month = ["Jan", 31, "Feb", 28, "March", 30]
print (len(month)) # 6

# Elements can be extracted and a list can be sliced
first = month[0] # This is "Jan"

# new list is created out of the list above
firstTwo = month[0:2]   # This is ["Jan", 31]
lastTwo = month[len(month)-2: len(month)]   # This is ["March", 31]

print (month[-1])   # 30
print (month[-2])   # March

# Nested lists
#weather=['Detroit', [64,75], 'West Lafayette', [62, 81], month=["Jan","Feb","March"]]

weather = ["Detroit", [64, 75], "West Lafayette", [62, 81]]
# index 0: "Detroit"

print (weather[-1]) # [62, 81]
print (weather[-1][1])  # 81

# Operations on lists
L1 = [1,2]
L2 = [3,4]

L3 = L1+L2
print (L3) # [1,2,3,4]

#L3 = L1*L2 # Not allowed
#print (L3)
#L3 = L1-L2 # Not allowed
#print (L3)

# Replicate the list by

L3 = L1*2
print (L3)  # [1,2,1,2]

L3 = L1*3
print (L3)  # [1,2,1,2,1,2]

L3 = L1*0
print (L3)  # [] empty list

L3 = L1*-1
print (L3)  # [] empty list

'''
Play and Learn

P1. Create and print the following list:
    [1,2,1,2,1,2,1,2]. 
    What if the pair (1, 2) is repeated 1000 times? 
'''
p1 = [1,2]*1000
print (p1)  # no problem

'''
P2. Input a sentence that ends with a period. 
    Create a list of all words in the sentence. 
    Print the list and  the number of words. 
    What if the sentence is empty?
'''
p2 = "Hello my name is seunghee."
p2l = p2.split()
print (p2l)
print (len(p2l))    # 5

# if sentence is empty
p2 = ""
p2l = p2.split()
print (p2l) # This is []
print (len(p2l))    # This is 0

'''
P3. 
    In P 2 remove the first and last words from the list
    and print the remaining words. 
    What if there is only one word in the list?
'''
p3 = "Hello my name is seunghee."
p3l = p3.split()
p3_ = p3l[1:len(p3l)-1]
print (p3_) # ['my', 'name', 'is']

# you can change elements
# list is mutable / map is not mutable
p3_[0] = "hi"
print (p3_) # ['hi', 'name', 'is']

'''
P4. Create the list [“hello”, “dear”, “frind”]
    Do a spelling correction on the list you created and create the list [“hello”, “dear”, “friend”]
    Create a list of correct spellings 
    for the three words “hello”, “dear”, and “friend”;  
    and another list with a few spelling errors in these words. 
    Use the list with correct spellings to correct any spelling errors 
    and print the corrected list. 
'''

p4 = ["hello", "dear", "frind"]
p4[2] = "friend"
print (p4)

p4_incorrect = ["hello", "dear", "frind"]
p4_correct = ["hello", "dear", "friend"]

p4_incorrect[2] = p4_correct[2]
print (p4_incorrect)

# ------------------------------ Range ------------------------------#
r = range(5)    # Generates[0,1,2,3,4]

# (starting value, upper limit, steps)
r = range(1,5,2) # Generates[1,3]

r = range(5,0,-1) # Generates [5,4,3,2,1]

print (r)   # range(5,0,-1)
print (type(r)) # <class 'range'>

# Be careful;
# Range is a function which will generate integers.
# but what is generated is not list! it is generator

# We will use the range() function in loops
# Example: Find the sum of a list of numbers
