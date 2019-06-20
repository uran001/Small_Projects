
# Note the import of the Queue class
from queue import ArrayQueue

def hot_potato(name_list, num):
    """
    Hot potato simulator. While simulating, the name of the players eliminated should also be printed
    (Note: you can print more information to see the game unfolding, for instance the list of
    players to whom the hot potato is passed at each step...)

    :param name_list: a list containing the name of the players, e.g. ["John", "James", "Alice"]
    :param num: the counting constant (i.e., the length of each round of the game)
    :return: the winner (that is, the last player standing after everybody else is eliminated)
    """
    print("Game is started with players")

    r = 1
    n = 0
    while 1:

        if len(name_list) == 1:
            return name_list[0]
        print ("Round {0}".format(r))
        print(name_list)
        for x in range(len(name_list)):
            n += 1
            if n % num == 0:
                print(name_list[x])
                name_list.remove(name_list[x])

        r += 1




if __name__ == '__main__':
    name_list = ["Marco", "John", "Hoang", "Minji", "Hyunsuk", "Jiwoo"]
    winner = hot_potato(name_list, 5)
    print("...and the winner is: {0}".format(winner))
