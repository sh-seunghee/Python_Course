import random

#Q1
print("Q1")

class Time:

    def __init__(self, hours=0, minutes=0):

        self.hours = hours
        self.minutes = minutes

    def addTime(self):

        time1_hours = input()
        time1_minutes = input()
        time1 = Time(int(time1_hours), int(time1_minutes))

        time2_hours = input()
        time2_minutes = input()
        time2 = Time(int(time2_hours), int(time2_minutes))

        self.hours = time1.hours + time2.hours
        self.minutes = time1.minutes + time2.minutes

    def displayTime(self):
        # print the time calculated

        if self.minutes >= 60:

            if self.minutes == 120:
                self.hours += 2
                self.minutes = 0
            else:
                self.hours += 1
                self.minutes -= 60

        print("%d hours %d minutes" % (self.hours, self.minutes))

    def displayMinute(self):
        # print the total minutes in the time calculated

        hours_to_minutes = self.hours * 60

        total_minutes = self.minutes + hours_to_minutes

        print ("%d minutes" % total_minutes)


time = Time()
time.addTime()
time.displayTime()
time.displayMinute()

#Q2
print("Q2")

class ClassA:

    name = "A"

    def __lt__(self, other):
        if other.name == "B":
            return False
        elif other.name == "C":
            return True

    def __gt__(self, other):
        if other.name == "B":
            return True
        elif other.name == "C":
            return False

    def __eq__(self, other):
        return False

class ClassB:

    name = "B"

    def __lt__(self, other):
        if other.name == "A":
            return True
        elif other.name == "C":
            return False

    def __gt__(self, other):
        if other.name == "A":
            return False
        elif other.name == "C":
            return True

    def __eq__(self, other):
        return False

class ClassC:

    name = "C"

    def __lt__(self, other):
        if other.name == "A":
            return False
        elif other.name == "B":
            return True

    def __gt__(self, other):
        if other.name == "A":
            return True
        elif other.name == "B":
            return False

    def __eq__(self, other):
        return False

class Player:

    def __init__(self):

        self.score = 0

    def get_score(self):
        return self.score

    def play(self):

        # returns an object of type either ClassA, ClassB, or ClassC
        ca = ClassA()
        cb = ClassB()
        cc = ClassC()

        vars = [ca, cb, cc]

        return random.choice(vars)

class PlayerX(Player):

    def __init__(self):

        super().__init__()

    def play(self):

        # read in the user's choice of a value from the keyboard instead of randomly selecting a move
        try:

            var = input("Input value of player([a], [b], [c], [end]): ")

            if var == "a":

                ca = ClassA()
                return ca

            elif var == "b":

                cb = ClassB()
                return cb

            elif var == "c":

                cc = ClassC()
                return cc

            elif var == "end": return "end"

        except KeyboardInterrupt:

            return "end"



if __name__ == "__main__":

    playerX = PlayerX()
    playerY = PlayerX()

    while True:

        value_for_X = playerX.play()

        if value_for_X == "end": break

        value_for_Y = playerY.play()

        if value_for_Y == "end": break

        print ("Player X chose "+value_for_X.name+", Player Y chose "+value_for_Y.name+".")

        if value_for_X < value_for_Y:
            print ("Player Y wins.")
            playerY.score += 1

        elif value_for_X > value_for_Y:
            print ("Player X wins.")
            playerX.score += 1

        else:
            print ("Draw.")

        # Print the scores
        print ("Player X score: %d, Player Y score: %d" %(playerX.get_score(), playerY.get_score()))

    print ("Game over")

