'''
# Lecture note: Session 3 and 4

    Loops (for and while)

'''
# ------------------------------ Loops ------------------------------#
# We will use the range() function in loops
# Example: Find the sum of a list of numbers

nums = input()
myList = nums.split()
sum=0   # Initialize

# Don't forget myList elements are string
# range(3) will generate 0,1,2
for i in range(len(myList)):    # Condition
    sum = sum+int(myList[i]) # Computation (Loop body) if condition is true

# if condition is false, it goes out of the loop and goes to the next computation
print (sum) # Next computation

'''
Play and learn

    p1. Input a sentence that ends with a period.
    Create a list of all words in the sentence. 
    Print each word in the list on a separate line.
    How can the period be removed from the last word in the output? 
    Try replace().
'''
p1 = "hello my name is seunghee."
p1_words = p1.split()
print (p1_words) # ['hello', 'my', 'name', 'is', 'seunghee.']
print (len(p1_words)) # 5

lastWord = p1_words[-1]
lastWord = lastWord.replace(".","")
p1_words[-1] = lastWord

for i in range(len(p1_words)):
    print (p1_words[i])

'''
    p2. Input a string. Print each letter of the string on a new line.
'''
# not solved during the class
p2 = "hello. my name is seunghee."
print (len(p2))
for i in range(len(p2)):
    print (p2[i])

# Using while
# any loop need initialization
for i in [22, 23, 24]:
    print (i)

# when using 'for', computer knows how many loop body will be executed.
# when using 'while", computer doesn't know when the condition will become false
n = input() # Get an integer
max = int(n)    # convert to int

nextTerm = 1    # first odd number
sum = 0 # be careful while coding this. * sum - reserved function

while sum <= max:   # Termination condition
    sum = sum+nextTerm
    nextTerm = nextTerm+2

print (nextTerm, sum)

# Nested for loops
for i in range(3):
    for j in range(4):
        print (i, j)