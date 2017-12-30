import random
def CoinToss(num):
    headcount = 0
    tailcount = 0
    for i in range(1, num+1):
        print "Attempt #", i, ": Throwing a coin..."
        if random.randint(0,1) == 0:
            print("It's a head! ...")
            headcount += 1
        else:
            print("Its a tail! ... ")
            tailcount += 1
        print "Got " + str(headcount)+" head(s) so far and "+ str(tailcount)+" tail(s) so far."
CoinToss(5000)