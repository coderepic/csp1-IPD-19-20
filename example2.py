####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'MegaRcheat'
strategy_name = 'Random'
strategy_description = 'Picks a random number between 1 and 2 in order to determine the action'
import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move by importing a random number.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    # This player colludes on even numbered rounds (first round is r.    
    choice = random.randint(1, 2)
    if choice == 1:
      return "c"
    else: 
      return "b"
    