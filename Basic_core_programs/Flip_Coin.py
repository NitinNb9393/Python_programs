"""
    * Author - Nitin Chandrakant Babar
    * Date -  14-12-2021
    * Time -  11.30pm
    * Title - flip coin 
"""

import random

coin_heads, coin_tails, times_flipped = 0, 0, 0

timesflipped = 0  
while timesflipped < 100:
	coin_flips = random.randrange( 2 )
	if coin_flips == 0:
		coin_heads += 1
	else:
		coin_tails += 1
	timesflipped += 1
	

print ("Out of 100 flips, " + str(coin_heads) + " were heads and " + str(coin_tails) + " were tails.")
