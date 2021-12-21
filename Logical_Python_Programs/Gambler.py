"""
   * Author - Nitin Babar
   * Date -  19-DEC-2021
   * Time -  6.30 PM
   * Title - Gambler program
"""

import random
def gambler(stake, goal, num_of_times):
    bet = 1
    win = loss = temp = 0
    for i in range(1,num_of_times+1):
        if ( random.random() >= 0.5):  
            win = win + 1
            stake = stake + bet
        if (stake == goal):
            break
        else:
            loss = loss + 1
            stake= stake - bet
        if (stake == 0):
            break
        print("The game was completed")
        temp = i

    if (temp <= num_of_times) and (stake == goal):
        print("The goal has reached")
    if (temp == num_of_times) and (stake != goal):
        print("Timeup.... Goal not reached")
    else:
        print("No more stake")

    print("No.of Wins:", win)
    print("Win percentage:", win * 100 / temp)  
    print("No.of Loss:", loss)
    print("Loss percentage", loss * 100 / temp) 

stake = int(input("Enter the amount: "))
goal = int(input("Enter the amount he want to gain: "))
num_of_times = int(input("How many times you want to repeat experiment:"))
gambler(stake, goal, num_of_times)
