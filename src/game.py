# -*- coding: utf-8 -*-

from src.Defs import *

print('Welcome to Roulette!\n')

playerDict = addplayer()

betDict = bet(playerDict) 

print(betDict)

winningnumber = spin()

resultDict = {0: ["0", "green"], 1: ["1", "odd", "red"], 2: ["2", "even", "black"], 3: ["3", "odd", "red"], 4: ["4", "even", "black"], 5: ["5", "odd", "red"], 6: ["6", "even", "black"], 7: ["7", "odd", "red"], 8: ["8", "even"], 9: ["9", "odd", "red"], 10: ["10", "even", "black"], 11: ["11", "odd", "black"], 12: ["12", "even", "black"], 13: ["13", "odd", "red"], 14: ["14", "even", "black"], 15: ["15", "odd", "red"], 16: ["16", "even", "black"], 17: ["17", "odd", "red"], 18: ["18", "even", "black"], 19: ["19", "odd", "red"], 20: ["20", "even", "black"], 21: ["21", "odd", "red"], 22: ["22", "even", "black"], 23: ["23", "odd", "red"], 24: ["24", "even", "black"], 25: ["25", "odd", "red"], 26: ["26", "even", "black"], 27: ["27", "odd", "red"], 28: ["28", "even", "black"], 29: ["29", "odd", "red"], 30: ["30", "even", "black"], 31: ["31", "odd", "red"], 32: ["32", "even", "black"], 33: ["33", "odd", "red"], 34: ["34", "even", "black"], 35: ["35", "odd", "red"], 36: ["36", "even", "black"], 37: ["00", "green"]}

wincon = resultDict[winningnumber]

"""
for person in betDict.values:
    for con in wincon:
        if con in person.keys:
            if person.values == con:
"""
                
for con in wincon:
    for player in betDict.keys():
        for key in betDict[player].keys():
            if key == con:
                print("key == con")
        
            
    
boardfactorDict = {"number" : 36,    "Dozen1" : 3, "Colum1" : 3, "Dozen2" : 3, "Colum2" : 3, "Dozen3" : 3, "Colum3" : 3, "Low" : 2, "High" : 2, "even" : 2, "Odd" : 2, "Red" : 2, "Black" : 2}

red = (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36)
black = (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)
green = (0, 00)
even = (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
odd = (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)
  
# doz1 : 50


#wheel result = 4


# hvis Rand Int = 38 amount * 2 => player.money



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



