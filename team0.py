####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Mr G' # Only 10 chars displayed.
strategy_name = 'Im guessing'
strategy_description = 'History'
    
def move(my_history, their_history, my_score, their_score):
    if len(history) == 0:        
          return "c"    
    if len(history) > 0:
          check = []
          (you, them) = history[-1] #Access the most recent move made by both players. History is always a list of tuples consisting of your move and then your opponent's move.
          check.append(them)          
          if "c" in check:    
               import random
               number = random.randint(1,10)
               if number == 10:
                    return "c"
               else:
                    return "c"
          else:
               return "c"

   