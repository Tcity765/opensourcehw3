
 
"""
===================
rock paper scissors
===================

#raw-form
This is a program that lets you play rock paper scissors!

1.how to play
2.how to win

===================
Chapter 1
===================

#raw-form
This program lets you play the game 10 times.
enter the hand you wish to play(capital sensitive)
the program will tell you whether you won or lost

====================
Chapter 2
====================

#raw-form
You will win if:
you play scissors and comp plays paper
you play rock and comp plays scissors
you play paper and comp plays rock

"""

import random
hand_symbols = ['rock', 'paper', 'scissor']

def determine_winner(com, human):
    """ Determine winner of the game.
    :param com:   Computer hand
    :param human: Human hand
    :returns void: Nothing is returned.
    """
    print("Computer has", hand_symbols[com], ", you have", hand_symbols[human])
    result = human - com
    if result == 0:
        print("Draw.")
        print("game over.")
        a = input(print("play again?(y or n)"))
        if a == "n":
            x  = x + 1
    elif result < 0 or result == 2:
        print("Computer wins.")
        print("game over.")
        a = input(print("play again?(y or n)"))
        if a == "n":
            x  = x + 1
        
    else:
        print("You win.")
        print("game over.")
        a = input(print("play again?(y or n)"))
        if a == "n":
            x  = x + 1

x = 0
while x == 0:
    if __name__ == "__main__":
        com_hand = random.randint(0, 2)
        print("Type your hand (rock: 0, paper: 1, scissor: 2)")
        human_hand = int(input())
        determine_winner(com_hand, human_hand)
