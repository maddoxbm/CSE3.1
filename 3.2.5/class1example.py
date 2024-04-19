"""The function move(my_history, their_history) must return "r", "p", or "s".
my_history and their_history are strings of the same length, perhaps length zero.
"""

import random

strategy_name = "Look Back 2 "


def move(my_history, their_history):
    if (len(their_history) == 0):
      return "p"

    #second move is always rock
    elif(len(their_history) ==1):
        return "r"

    else:
        if their_history[-2] == "p"=
            return "s"
        elif their_history[-2] == "r":
            return "p"
        else:
            return "r"

