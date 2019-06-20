
from queue import ArrayQueue
import random


def hot_potato_spicy(name_list, num):
    """
    Simulates the Hot potato game "spiced up" with lives and randomness

    :param name_list: a list containing the name of the participants and their number of lives
    :param num: the counting constant (e.g., the length of each round of the game)
    :return: the winner
    """
    print("Game is started with players")

    r = 1
    n = 0
    while 1:

        if len(name_list) == 1:
            return name_list[0]
        print("Round {0}".format(r))
        print(name_list)
        for x in range(len(name_list)):
            n += 1
            if n % num == 0:
                r = random.random()
                if r < 0.5:
                    name_list[x][1] -= 1
                if name_list[x][1] == 0:
                    print(name_list[x][0])
                    name_list.remove(name_list[x])

        r += 1


if __name__ == '__main__':
    name_list = [["Marco", 5], ["John", 5], ["Hoang", 5], ["Minji", 5], ["Hyunsuk", 5], ["Jiwoo", 5]]

    winner = hot_potato_spicy(name_list, 21)
    # winner = hot_potato(name_list, 5)
    print("...and the winner is: {0}".format(winner))
