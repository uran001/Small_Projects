# implement here your solution

from For_use.linked_binary_tree import LinkedBinaryTree
import time

class MRP(LinkedBinaryTree):


    def create_bom(self, file_name):

        read_file = open(file_name, "r")
        now = None
        prev = 0

        for line in read_file.readlines():  # read lines in file one by one
            values = list(line.split(','))  # split the line using separator ','

            num = int(values[0])
            dir = values[1]
            part_name = values[2]

            if num == 0:
                now = self._add_root(part_name)
                prev = num
            else:
                rept = 0
                if prev >= num:
                    rept = prev - num + 1

                while rept > 0:
                    now = self.parent(now)
                    rept -= 1


                if dir == 'left':
                    now = self._add_left(now, part_name)
                    prev = num
                elif dir == 'right':
                    now = self._add_right(now, part_name)
                    prev = num

        read_file.close()





    def preorder_indent(self, p, d):
        """
        This is the function to "pretty" print a tree (already seen in previous sessions)
        """
        print(2 * d * '-' + str(p.element()))
        for c in self.children(p):
            self.preorder_indent(c, d + 1)
            time.sleep(0.5)





if __name__ == '__main__':
    # code for your demo here

    print("\n___START___\n")
    #Create tr  ee for Coolbike

    coolbike = MRP()

    #Required parts of coolbike
    coolbike_bom = {}
    coolbike_bom['frame_b'] = 1
    coolbike_bom['chain_a'] = 1
    coolbike_bom['tire_a'] = 2
    coolbike_bom['wheel_a'] = 2
    coolbike_bom['handlebar_c'] = 1
    coolbike_bom['rubberhandle_a'] = 2

    #creating Tree of coolbike parts
    coolbike.create_bom("coolbike.dat")

    coolbike.preorder_indent(coolbike.root(), 0)
    print('\n')

    time.sleep(1)

    #Create tree for Boringbike

    #Required parts of Boringbike
    boringbike = MRP()
    boringbike_bom = {}
    boringbike_bom['frame_a'] = 1
    boringbike_bom['chain_b'] = 1
    boringbike_bom['completewheel_a'] = 2
    boringbike_bom['handlebar_c'] = 1
    boringbike_bom['rubberhandle_a'] = 2

    boringbike.create_bom("boringbike.dat")
    boringbike.preorder_indent(boringbike.root(), 0)
    print('\n')

    time.sleep(1)
    #Parts in stock
    part = {}
    read_file = open("parts.dat", "r")

    for line in read_file.readlines():
        val = list(line.split(','))
        part[val[0]] = [int(val[2]), int(val[3])]

    read_file.close()



    #receiving order

    read_file = open("order.dat", "r")

    balance = 0
    cur = 0 #loan from bank in case not enough money
    req = []
    for line in read_file.readlines():
        values = line.split(',')
        values[1] = int(values[1])
        print("Received Order for {0}, {1}".format(values[0], values[1]))
        time.sleep(1)
        if values[0] == 'boringbike':

            for x in boringbike_bom:
                if part[x][0] - (boringbike_bom[x] * values[1]) > 0:
                    part[x][0] -= boringbike_bom[x] * values[1]
                else:
                    part[x][0] = 0
                    balance -= (part[x][1] * (abs(part[x][0] - boringbike_bom[x] * values[1]) + 1))

        elif values[0] == 'coolbike':

            for x in coolbike_bom:
                if part[x][0] - (coolbike_bom[x] * values[1]) > 0:
                    part[x][0] -= coolbike_bom[x] * values[1]
                else:
                    part[x][0] = 0
                    balance -= (part[x][1] * (abs(part[x][0] - coolbike_bom[x] * values[1]) + 1))

        print("Order for {0}, {1} done".format(values[0], values[1]))
        time.sleep(0.3)

        if balance < 0:
            print("To finish this order our company took loan {0} $ from bank....\n".format(abs(balance)))
            get_money = input("Would you like sell your unused stocks in order to get money?(Y/N) :  ")
            get_money = get_money.lower()
            get_money.split(' ')
            prev = balance
            if get_money[0] == 'y':
                print("\nProcessing....\n")
                time.sleep(1)
                av = 0
                for a in part:
                    if a in coolbike_bom:
                        av += part[a][0] // coolbike_bom[a]
                    elif a in boringbike_bom:
                        av += part[a][0] // boringbike_bom[a]
                av = av // len(part)
                for a in part:
                    if part[a][0] > av:
                        balance += part[a][1] * (abs(av - part[a][0]))
                        part[a][0] -= abs(av - part[a][0])
                if balance >= 0:
                    print("You earned {0} $ money with selling unused stocks\n".format(abs(balance - prev)))
                    time.sleep(0.3)

        bonus_part = values[1] // 3

        for c in part:
            part[c][0] += bonus_part

        print("The number of stocks has increased by {0}\n".format(bonus_part))

        prt = input("Do you want to see information about parts in your company?(Y/N) :  ")
        prt.split(' ')
        if prt[0] == 'y' or prt[0] == 'Y':
            print("\nProcessing.....\n")
            time.sleep(1)
            table = [
                ["Part Name", "Quantity", "Price"]
            ]
            for _ in part:
                table.append([_, part[_][0], part[_][1]])

            longest_cols = [
                (max([len(str(row[i])) for row in table]) + 2)
                for i in range(len(table[0]))
            ]
            row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])
            for row in table:
                print(row_format.format(*row))
                time.sleep(0.3)
            print("\n Balance: {0}".format(balance))
            print('\n')


    print("\n___EXIT___\n")


