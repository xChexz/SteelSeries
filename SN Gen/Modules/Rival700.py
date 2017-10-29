import random
def Rival700():
    amount = int(input("How many Serial Numbers would you like to generate? >> "))
    for i in range(0,amount):
        ran1 = random.randint(11111111111,99999999999)
        ran1 = str(ran1); sn = "62331" + ran1
        print (sn)
        txt = open("Output\R700.txt", "a")
        txt.write("SteelSeries / " + sn + " / Rival700, \n")
        txt.close()
