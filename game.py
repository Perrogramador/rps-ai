"""
This module serves to provide game control functionality for rock/paper/scissors
It:
- Precalculates a move to play (either randomly or based on a statistical model)
- Recieves user's move
- Returns the computer's move
- Determines a winner

The idea is to have both play their moves at the same time.
"""

r = "r"; p = "p"; s = "s"

class RPS():
    # rock, paper, scissors
    MOVES = ["r", "p", "s"]

    def __init__(self):
        pass

    def play(self, move):
        """
        Takes a user move and calculates AI move simultaneously
        Determines winner
        """
        self.user_move = move if move in self.MOVES else False
        self.ai_move = self.calculate_move()

        print("You played: " + self.user_move)
        print("AI played: " + self.ai_move)

        return self.who_wins()

    def calculate_move(self):
        """
        Calculates a move to play for the AI
        """
        import random
        return random.choice(self.MOVES)

    def who_wins(self):
        """
        Given both players have made a move,
        determine the winner
        """
        p1 = self.ai_move
        p2 = self.user_move

        if p1 in self.MOVES and p2 in self.MOVES:
            if p1 == p2:
                return self._winner(0)

            if (p1 == r and p2 == s) \
            or (p1 == p and p2 == r) \
            or (p1 == s and p2 == p):
                return self._winner(1)

            if (p2 == r and p1 == s) \
            or (p2 == p and p1 == r) \
            or (p2 == s and p1 == p):
                return self._winner(2)
            
            raise Exception

    def _winner(self, player):
        """
        Return winner and winning move
        :player: integer (1|2)
        :return: string
        """
        if player == 0:
            print ("It's a tie! " + self.user_move + "==" + self.ai_move)
        elif player == 1:
            print ("AI wins! "
                    + self.ai_move + " defeats " + self.user_move)
        elif player == 2:
            print ("You win! "
                    + self.user_move + " defeats " + self.ai_move)
        else:
            raise ValueError('_winner() takes 1 argument: player must be 1 or 2. %d provided.' % player)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
