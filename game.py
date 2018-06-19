#!/user/bin/env python3

"""
This module serves to provide game control functionality for rock/paper/scissors
It:
- Precalculates a move to play (either randomly or based on a statistical model)
- Recieves user's move
- Returns the computer's move
- Determines a winner

The idea is to have both play their moves at the same time.
"""

import random

class RPS():
    # rock, paper, scissors
    MOVES = ["r", "p", "s"]

    def __init__(self):
        self.ai_move = False
        self.user_move = False
        pass

    def ai_move(self):
        """
        The computer decides on a move to play
        """
        self.ai_move = random.choice(self.MOVES)
        return self.ai_move

    def user_move(self, move):
        """
        The user makes a move
        """
        self.user_move = move if move in self.MOVES else False
        return self.user_move

    def winner(self):
        """
        Determines a winner
        """

    
    def play(self, p1, p2):
        """
        Quick function to compare moves
        """
        if p1 in self.MOVES and p2 in self.MOVES:
            # determine winner using algorithm

        

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
