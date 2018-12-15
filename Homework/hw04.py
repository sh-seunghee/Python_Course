
print ("Q1")

pos = ["Good", "Awesome", "Excellent", "Great", "Efficient", "Bug-free", "User-friendly"]
neg = ["Bad", "Bugs", "Boring", "Tiresome", "Poor performance", "Inefficient"]

pos_lower = []
neg_lower = []

for i in range(len(pos)):
    pos_lower.append(pos[i].lower())
for i in range(len(neg)):
    neg_lower.append(neg[i].lower())

texts = []
text = ""


# Input text
while ("\end" not in text):
    text = input()
    texts.append(text)

total_pos = 0
total_neg = 0
total_ind = 0

for i in range(len(texts)):

    pos_count = 0
    neg_count = 0
    ind_count = 0

    words = texts[i].split()

    for j in range(len(words)):

        cur_word = words[j].replace(".", "")
        cur_word = cur_word.replace("!", "")
        cur_word = cur_word.replace(",", "")
        cur_word = cur_word.replace("\end", "")

        cur_word = cur_word.lower()

        if (cur_word in pos_lower):
            pos_count = pos_count+1

        elif (cur_word in neg_lower):

            if (cur_word == "poor"):
                if ( j+1 < len(words)):
                    if (words[j+1] == "performance"):
                        neg_count = neg_count + 1
            else:
                neg_count = neg_count + 1


    # add to total
    if (pos_count > neg_count):
        total_pos = total_pos + 1
    elif (pos_count < neg_count):
        total_neg = total_neg + 1
    else:
        total_ind = total_ind + 1


if (total_pos > total_neg):
    print ("Positive")
elif (total_pos < total_neg):
    print ("Negative")
else:
    print ("Indeterminate")


#############################
print ("Q2")

num1 = input()
num1 = int(num1)

prime_in_num1 = []

def isprime(n):
    n = abs(int(n))

    # 2 is always prime
    if (n<2):
        return False
    if (n==2):
        return True

    # All other even numbers are not primes
    if (not n & 1):
        return False

    for x in range(3, int(n**0.5) +1, 2):
        if (n % x == 0):
            return False
    return True


for i in range(1, num1+1):
    if (isprime(i)):
        prime_in_num1.append(i)

num2 = input()
num2 = int(num2)

# Initialization
diff_min = 999999999
closest_num = -1

for i in prime_in_num1:
    diff = abs(i-num2)

    if (diff < diff_min):
        closest_num = i
        diff_min = diff
    elif (diff == diff_min):
        if ( i < closest_num ):
            closest_num = i

print ("Closest prime number: %g" %(closest_num))


