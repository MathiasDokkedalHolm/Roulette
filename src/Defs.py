# -*- coding: utf-8 -*-

def addplayer():
    playername = ""
    money = 0
    playerDict = {}
    while playername != "done":
        playername = input('Write player-name or finish with "done"\n\n').title()
        if playername != "Done":
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
    return playerDict

def bet(playerDict, boardfactorDict, resultDict):
    betDict = {}
    for playername,money in playerDict.items():
        
        betDict[playername] = {}
        
        print(playername, "please place your bets")
        
        field = ""
        
        while field != "Done":
            field = input(str(playername) + " : Which field would you like to bet?").title()
            if field not in boardfactorDict:
                while field not in boardfactorDict or resultDict.keys():
                    field = input(str(playername) + " : Which field would you like to bet?").title()
                
            if field == "Done":
                break
            bet = int(input(str(playername) + " : How much would you like to bet?"))
            if bet > money:
                while bet > money:
                    print("You cant afford it - input an amount you can afford")
                    bet = int(input(playername, ": How much would you like to bet?"))
            else:
                playerDict[playername] -= bet
            betDict[playername][field] = bet
            print("Type 'done' when done betting for this round")
    return betDict

import random

def spin():
    WheelSpinResult = random.randint(0,38)
    return WheelSpinResult