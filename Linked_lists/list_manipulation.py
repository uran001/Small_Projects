
from linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList


def find(L, e):

    cur = L.find(e)
    if cur == None:
        print("Element not found in the list")
    else:
        print("ELement {0} found in the list at position {1}".format(e, cur))

def cat(L1,L2):

    temp = L2._head
    t = L2.__len__()
    print(t)
    while t > 0:
        L1.add_last(temp._data)
        temp = temp._next
        t -= 1

def copy(L):

    temp = L

    return temp

def copy_and_cat(L1,L2):

    temp = copy(L1)
    cat(temp, L2)
    return temp

def swap_first_with_last(DL):

    data = DL._head._data
    data1 = DL._tail._data

    DL.remove_first()
    DL.remove_last()
    DL.insert_front(data1)
    DL.insert_last(data)

def insert_at_position(DL, n, data):

    DL.insert(data, n - 1)


def special_copy(DL1,DL2):



    l = []
    current_node = DL2._head
    while current_node is not None:
        if current_node._next == None:
            l.append(current_node._data)
        else:
            l.append(current_node._data)
        current_node = current_node._next
    l.reverse()
    for x in l:
        DL1.add(x)
    return DL1


if __name__ == '__main__':



     L1 = LinkedList()
     L2 = LinkedList()
     L1.add_first("Jin")
     L1.add_first("Jun")
     L1.add_first("Jan")
     L1.print()
     L2.add_first(118)
     L2.add_first(115)
     L2.add_first(89)
     L2.add_first(87)
     L2.print()
     find(L1,"Jin")
     find(L1, 908)
     cat(L1,L2)
     L1.print()
     print("""Test deep copy and copy_cat""")
     L3 = copy(L1)
     L3.print()
     L3.add_first("new")
     L3.print()
     L1.print()
     print("cat")
     cat(L1, L3)
     L1.print()
     L4 = copy_and_cat(L1,L3)
     L4.print()

     print("DL")
     """ create two doubly linked lists and add some data"""
     DL1 = DoublyLinkedList()
     DL2 = DoublyLinkedList()
     DL1.add("A")
     DL1.add("B")
     DL1.add("Y")
     DL1.add("Z")
     DL1.print()
     DL2.add(67)
     DL2.add(69)
     DL2.add(25)
     DL2.add(29)
     DL2.add(76)
     DL2.print()
    #
    # """ test swap """
     print("========== Test swap() ===================================")
     DL2.print()
     print(str(DL2.__len__()))
     swap_first_with_last(DL2)
     DL2.print()

     """ test insert at position"""
     print("========== Test insert_at_position() ===================================")
     insert_at_position(DL2, 2, "marco")  # insert walking from head
     DL2.print()
     insert_at_position(DL2, 6, "james")  # insert walking from tail
     print(str(DL2.__len__()))
     DL2.print()
     insert_at_position(DL2, 1, "2345")  # insert at head
     DL2.print()
     insert_at_position(DL2, DL2.__len__(), "Bob")  # insert at tail
     DL2.print()
     insert_at_position(DL2, 4, "4")
     insert_at_position(DL2, 7, "7777")
     DL2.print()

    #""" test cat """
     print("========== Test special_copy() ===================================")
     DL1.print()
     DL2.print()
     DL3 = special_copy(DL1, DL2)
     DL3.print()

