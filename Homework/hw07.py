import functools

#Q1
print("Q1")

# First input: the number of strings
numOfStr = input()
numOfStr = int(numOfStr)

if numOfStr == 0:
    print ("No string available")

else:

    # Second input
    string1 = input().split(",")

    f = map(lambda str: list(str), string1)
    print(list(f))

#Q2
print("Q2")

def frequency(str):

    frequencydict = {}  # frequency listing in python dictionary

    str = str.lower()

    for letter in list(str):

        if letter == " ": continue

        if letter in frequencydict:
            frequencydict[letter] += 1
        else:
            frequencydict[letter] = 1

    return frequencydict

texts = []

# Get Keyboard input and append it to texts
while True:
    text = input()

    if text == "\end":
        break

    texts.append(text)

if len(texts) == 0: print ("Error")
else:

    for i in range(len(texts)):

        unordered_dict = frequency(texts[i])
        ordered_dict = {}

        # sort the dictionary by keys
        for key, value in sorted(unordered_dict.items()):

            ordered_dict[key] = value

        print(ordered_dict)

#Q3
print("Q3")

locs = []

while True:

    x_y = input()
    if x_y == "\end":
        break

    x_y = x_y.split(",")
    locs.append((float(x_y[0]),float(x_y[1])))

points = iter(locs)

def comp1(p1, p2):

    # First compare x point
    if p1[0] < p2[0]:
        return p1

    elif p1[0] > p2[0]:
        return p2

    else:
        # Compare y point
        if p1[1] < p2[1]:
            return p1
        elif p1[1] > p2[1]:
            return p2
        else:
            p2 # p1 and p2 is the same

out = functools.reduce(comp1, points)

print (out)