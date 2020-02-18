####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'MegaRcheat'
strategy_name = 'Betray twice if betrayed'
strategy_description ='if we were betrayed, we will betray the opponent for the next two turns.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
'''

    def check_betray(their_history):
      if len(their_history) >= 2:
        if their_history[len(their_history) - 1] == 'b' or their_history[len(their_history) - 2] == 'b':
          return "b"
      elif len(their_history) == 1:
        if their_history[len(their_history) - 1] == 'b':
          return "b"
      else: 
        return "c"

    check_betray(their_history)
  
    