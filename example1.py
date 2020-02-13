####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'MegaRcheat'
strategy_name = 'Betray twice if colluded'
strategy_description = 'If we were colluded, we will betray for the next two turns'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
          
    def check_collude(their_history):
      if their_history[their_history.len()] == 'c' or their_history[their_history.len() - 1] == 'c':
        return "b"
    
    check_collude(their_history)
