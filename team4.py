####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'idk' # Only 10 chars displayed.
strategy_name = 'Winning'
strategy_description = 'If they have betrayed, betray. If they havent betrayed, betray 1% of the time and collude the rest of the time'

def move(my_history, their_history, my_score, their_score):


    if 'b' in their_history: # If the other player has betrayed 
        return 'b'
    else:
        if random.random()<0.01: # 1% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 99% of the time collude

    
            
            