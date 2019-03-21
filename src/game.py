# -*- coding: utf-8 -*-

print('Welcome to Roulette!\n')

playerDict = {}

playername = ""
money = ""

boardfactorDict = {"number" : 36,    "Dozen1" : 3, "Colum1" : 3, "Dozen2" : 3, "Colum2" : 3, "Dozen3" : 3, "Colum3" : 3, "low" : 2, "High" : 2, "Even" : 2, "Odd" : 2, "Red" : 2, "Black" : 2}

red = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
green = (0, 00)
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)

while playername != "n":
    playername = input('Write player-name or finish with "n"\n\n')
    if playername != "n":
        while True:
            try:
                money = int(input('How much money does he/she bring to the table?\n\n'))
                if money > 0:
                    playerDict[playername] = money
                    break
                else:
                    print("Insufficient amount. Retry")
            except ValueError:
                print("Valueerror - please try again")
                


import random

def bet(playerDict):
    betDict = {}
    for playername,money in playerDict.items():
        print(playerDict.playername, "please place your bets")
        field = ""
        while field != "done":
            field = input(playername, ": Which field would you like to bet?")
            bet = input(playername, ": How much would you like to bet?")
            if bet > money:
                while bet > money:
                    print("You cant afford it - input an amount you can afford")
                    bet = input(playername, ": How much would you like to bet?")
            else:
                money -= bet
            betDict[playername][field] = bet
            print("Type 'done' when done betting for this round")
    return betDict

def spin():
    WheelSpinResult = random.randint(0,38)
    return WheelSpinResult

    
# doz1 : 50

# hvis Rand Int = 38 amount * 2 => player.money
    
        
    


"""

Bet                      Payout  Win probability* Win probability**
Red / Black (18 numbers)   1:1        48.65%          47.37%
Even / Odd (18 numbers)    1:1        48.65%          47.37%
Low / High (18 numbers)    1:1        48.65%          47.37%
Dozen (12 numbers)         2:1        32.43%          31.58%
Column (12 numbers)        2:1        32.43%          31.58%
Double Street (6 numbers)  5:1        16.22%          15.79%
First Five (5 numbers)     6:1          -             13.16%
Corner (4 numbers)         8:1        10.81%          10.53%
Street (3 numbers)         11:1       8.11%           7.89%
Split (2 numbers)          17:1       5.41%           5.26%
Straight (single number)   35:1       2.70%           2.63%

"""



