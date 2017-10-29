import random
def Qck():
    amount = int(input("How many Serial Numbers would you like to generate? >> "))
    for i in range(0,amount):
        ran1 = random.randint(11111111111,99999999999)
        ran1 = str(ran1); sn = "63391" + ran1
        print (sn)
        txt = open("Output\Qck.txt", "a")
        txt.write("SteelSeries / " + sn + " / QckPrism, \n")
        txt.close()
