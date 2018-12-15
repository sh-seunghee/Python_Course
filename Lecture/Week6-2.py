'''
# Lecture note: Session 9 and 10

    read and write files (text, binary)
    Dictionaries
'''

# -----------------------  Dictionaries -----------------------#
# A set of key-value pairs

# Key and value can be anything. They can be a tuple, list, ..anything

wimbledon_mens={1968: "Rod Laver", 1969: "Rod Laver", 1970: "John Newcombe"}
wimbledon_womens={1968: "Billie Jean King", 1969: "Ann Hayden Jones", 1970: "Margaret Court"}

# Access a value using key 1970
print (wimbledon_womens[1970]) # Margaret Court

# Add a key-value pair
wimbledon_mens[1971] = "John Newcombe"
print (wimbledon_mens[1970]) # John Newcombe

# iterating over a dictionary
for key in wimbledon_mens:
    print(key, " ", wimbledon_mens[key])

# Deleting from a dictionary and testing for a key
del wimbledon_mens[1971]

if 1971 in wimbledon_womens:
    print ("Key 1971 exists")
else:
    print ("key 1971 does not exist")


'''
Play and Learn

    P1: Create a dictionary that contains key-value pairs 
    where the keys are M1, M2, and so on denoting team members, 
    and the values are names of the members.

    P2: Print the dictionary you have created

    P3: Read a key, e.g., M3,  from the input
    and print the corresponding member’s name. 
    Print “Key does not exist” if it does not!
 
'''

teams = {"M1": "name1", "M2": "name2"}
print (teams)

key = input()
if key in teams:
    print (teams[key])
else:
    print ("Key does not exist")



for k in teams:
    print (k, teams[k])

'''
In-class Exercise

    Download grades_file.csv and read the scores from the grades file into a dictionary named grades. 
    [Comma separated file; read using file I/O.] 
    
    Read the scores from the grades file into a dictionary named grades. 
    [Comma separated file; read using file I/O.] 
    
    There is one key for each group. Thus, the keys are A, B, C, and D.
    
    For each key create a list that contains the five grades obtained by each team.
    
    Sum the grades obtained by each team and add the sum as the last element to the list of grades for that team.  
    Print the updated dictionary.
    
    Sample output:
    grades={“A”: [2,3,5,5,12, 27.0], “B”: [1.5,3,5,4,15, 28.5],  “C”: [2,2,5,4,11,24.0 ],  ”D”: [0,5,5,5,10, 25.0]}
    
    Write the modified dictionary to a new file. 
    Make sure that the new file is comma separated with data 
    for each group, along with group ID, on a separate line. 

'''

filename = "grades_file.csv"

f = open(filename, "r") # open file for read only

grades = {}

# Read the first line cause the first line is heading
curLine = f.readline()

while True:

    data=f.readline()
    data = data.replace("\n","")

    if data == "":
        break

    g_values = data.split(",")
    key = ""
    values=[]
    sum = 0

    converted = [ float(x) for x in g_values[1:] ]

    grades[g_values[0]] = converted

    '''
    
    for i in range(len(g_values)):

    if i==0:
        key = g_values[0]

    else:
        values.append(float(g_values[i]))
        sum += float(g_values[i])

    #print (sum)
    grades[key] = values

    '''

f.close()

print (grades)
