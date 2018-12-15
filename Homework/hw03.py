print ("Q1")

def get_fx(guess, coe):

    f_guess = 0

    for i in range(len(coe)):
        f_guess = f_guess + (coe[i] * pow (guess, i))

    return f_guess

def get_f_dev_x(guess, coe):

    f_dev_guess = 0

    for i in range(len(coe)):

        if (i==0):   continue
        f_dev_guess = f_dev_guess + (coe[i] * i * pow(guess, i-1))

    return f_dev_guess

coe = input()
coe = coe.split(",")

for i in range(len(coe)):
    coe[i] = float(coe[i])

guess = input()
guess = float(guess)

#Initial guess x = ini
#next guess x1 = x0 - ( f(x0) / f'(x0) )

#find x where f(x) < 0.0001
f_guess = 10.0 # initalization

while (abs(f_guess) >= 0.0001):

    # calculate guess and update
    guess = guess - (get_fx(guess, coe) / get_f_dev_x(guess, coe))
    f_guess = get_fx(guess, coe) # calcualte with new guess

print ("The root is:%.5f" %(guess))

#############################################################

print ("Q2")
word = ""
words = []

while (word != "\end"):
    word = input()
    words.append(word)

words.remove("\end")

for i in range(len(words)):

    words[i] = words[i].replace(".", "")
    words[i] = words[i].replace(",", "")
    words[i] = words[i].replace("?", "")
    words[i] = words[i].replace("!", "")

text = ""
texts = []

while (text != "\end"):
    text = input()
    texts.append(text)

texts.remove("\end")

for i in range(len(texts)):

    texts[i] = texts[i].replace(".", " ")
    texts[i] = texts[i].replace(",", " ")
    texts[i] = texts[i].replace("?", " ")
    texts[i] = texts[i].replace("!", " ")

result = ""
cur_word = ""

for i in range(len(texts)):

    sub_texts = texts[i].split()
    for j in range(len(sub_texts)):

        cur_word = sub_texts[j]

        if (cur_word in words):
            cur_word = cur_word[::-1]

        if (result == ""): result = cur_word
        else:    result = result + " " + cur_word

print (result)