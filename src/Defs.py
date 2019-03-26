# -*- coding: utf-8 -*-

def addplayer():
    playername = ""
    money = 0
    playerDict = {}
    while playername != "Done":
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

"""
resultDict = {0: ['0', 'Green'], 1: ['1', 'Red', 'Odd', 'Low', 'Dozen 1', 'Column 1'], 2: ['2', 'Black', 'Even', 'Low', 'Dozen 1', 'Column 2'], 3: ['3', 'Red', 'Odd', 'Low', 'Dozen 1', 'Column 3'], 4: ['4', 'Black', 'Even', 'Low', 'Dozen 1', 'Column 1'], 5: ['5', 'Red', 'Odd', 'Low', 'Dozen 1', 'Column 2'], 6: ['6', 'Black', 'Even', 'Low', 'Dozen 1', 'Column 3'], 7: ['7', 'Red', 'Odd', 'Low', 'Dozen 1', 'Column 1'], 8: ['8', 'Black', 'Even', 'Low', 'Dozen 1', 'Column 2'], 9: ['9', 'Red', 'Odd', 'Low', 'Dozen 1', 'Column 3'], 10: ['10', 'Black', 'Even', 'Low', 'Dozen 1', 'Column 1'], 11: ['11', 'Black', 'Odd', 'Low', 'Dozen 1', 'Column 2'], 12: ['12', 'Red', 'Even', 'Low', 'Dozen 1', 'Column 3'], 13: ['13', 'Black', 'Odd', 'Low', 'Dozen 2', 'Column 1'], 14: ['14', 'Red', 'Even', 'Low', 'Dozen 2', 'Column 2'], 15: ['15', 'Black', 'Odd', 'Low', 'Dozen 2', 'Column 3'], 16: ['16', 'Red', 'Even', 'Low', 'Dozen 2', 'Column 1'], 17: ['17', 'Black', 'Odd', 'Low', 'Dozen 2', 'Column 2'], 18: ['18', 'Red', 'Even', 'Low', 'Dozen 2', 'Column 3'], 19: ['19', 'Red', 'Odd', 'High', 'Dozen 2', 'Column 1'], 20: ['20', 'Black', 'Even', 'High', 'Dozen 2', 'Column 2'], 21: ['21', 'Red', 'Odd', 'High', 'Dozen 2', 'Column 3'], 22: ['22', 'Black', 'Even', 'High', 'Dozen 2', 'Column 1'], 23: ['23', 'Red', 'Odd', 'High', 'Dozen 2', 'Column 2'], 24: ['24', 'Black', 'Even', 'High', 'Dozen 2', 'Column 3'], 25: ['25', 'Red', 'Odd', 'High', 'Dozen 3', 'Column 1'], 26: ['26', 'Black', 'Even', 'High', 'Dozen 3', 'Column 2'], 27: ['27', 'Red', 'Odd', 'High', 'Dozen 3', 'Column 3'], 28: ['28', 'Black', 'Even', 'High', 'Dozen 3', 'Column 1'], 29: ['29', 'Black', 'Odd', 'High', 'Dozen 3', 'Column 2'], 30: ['30', 'Red', 'Even', 'High', 'Dozen 3', 'Column 3'], 31: ['31', 'Black', 'Odd', 'High', 'Dozen 3', 'Column 1'], 32: ['32', 'Red', 'Even', 'High', 'Dozen 3', 'Column 2'], 33: ['33', 'Black', 'Odd', 'High', 'Dozen 3', 'Column 3'], 34: ['34', 'Red', 'Even', 'High', 'Dozen 3', 'Column 1'], 35: ['35', 'Black', 'Odd', 'High', 'Dozen 3', 'Column 2'], 36: ['36', 'Red', 'Even', 'High', 'Dozen 3', 'Column 3'], 37: ["00", "Green"]}       

fieldList = []

boardfactorDict = {"Dozen1" : 3, "Colum1" : 3, "Dozen2" : 3, "Colum2" : 3, "Dozen3" : 3, "Colum3" : 3, "Low" : 2, "High" : 2, "even" : 2, "Odd" : 2, "Red" : 2, "Black" : 2}
"""

def bet(playerDict, boardfactorDict, resultDict):
    betDict = {}
    for playername,money in playerDict.items():
        
        betDict[playername] = {}
        
        print(playername, "please place your bets")
        
        field = ""
        
        while field != "Done":
            
            field = input(str(playername) + " : Which field would you like to bet?").title()
            
            if field == "00":
                field = "37"
            if field != "Done":
                while field not in str(resultDict.keys()):
                    if field not in boardfactorDict.keys():
                        print("I do not understand which board-field you would like to bet.\n\nBet on a number from 1 to 36 or on green (0 / 00) \n\nWrite them as follows, please :) ")
                        for key in boardfactorDict.keys():
                            print(key)
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