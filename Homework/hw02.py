
#Q1
print("Q1")
#TODO

p1 = []
element = 1

while (element < 11):
    _input = element * element
    p1.append(_input)
    element = element+1

print (p1)
print (len(p1))

#Q2
print("Q2")
# TODO

element = [1,2,3,4]
L2 = []
for i in range(4):
    L2.append(element)

print (L2)

#Q3
print("Q3")
# TODO

L3 = []
for i in range(len(L2)):
    cur = L2[i]
    for j in range(len(cur)):
        L3.append(cur[j])

print (L3)

#Q4
print("Q4")
# TODO
start = -10
L4 = []
for i in range(-10, 12, 3):
    L4.append(i)
print (L4)

max_L4 = max(L4)
print (max_L4)

min_L4 = min(L4)
print (min_L4)
L4.insert(3, 100)

L4 = sorted(L4)
print (L4)

#Q5
print("Q5")
# TODO

L1=input()
L2=input()

L1 = L1.split(",")
L2 = L2.split(",")

m = len(L1)
n = len(L2)

Q5_sum = 0
for i in range(0, m):
    for j in range(0, n):
        ele = float(L1[i]) * float(L2[j])
        Q5_sum = Q5_sum + ele

print ("Sum of products:%.2f" % (Q5_sum))
