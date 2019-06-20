

import networkx as nx
import matplotlib.pyplot as plt
import datetime as dt
import random as rd
from graphs_basics import print_graph, display_and_save





def modulo_digraph(N,M):
    """
    This function returns a directed graph DiGraph) with the following properties (see also cheatsheet at: http://screencast.com/t/oF8Nr1TdYDbl):
    - The graph has N nodes, labelled using numbers from 1 to N-1
    - All nodes in the same M-modulo class are on the same path (the path from the node with lower value to highest value)
    - All nodes that are multiple of M-1 (or, in other words, for which node % (M-1) == 0) are on the same path (that gos from lower to higher values)

    Hint:
    - Initialise the DiGraph, for each node you can store two properties (value of % M, value of % (M-1))
    - Scan the created graph to create paths based on similar values of the two properties
    - Create edges in the graph using the values of the lists of nodes that you created at the previous step

    More about DiGraphs at: https://networkx.github.io/documentation/development/reference/classes.digraph.html
    """
    G = nx.Graph()

    for i in range(1, N+1):
        G.add_node(i)

    for i in range(1, N+1):
        if i+M <= N:
            G.add_edge(i, i+M)
        if i+M-1 <= N:
            G.add_edge(i, i+M-1)

    return G



def create_random_graph(min_node_num, max_node_num):
    """
    This function creates a directed graph with n nodes, where n is a
    random number between min_node_num and max_node_num.
    Nodes are the numbered from 1 to n
    For each pair of nodes (a,b) in the graph except the pair (1,n), a random number r
    between 0 and 1 is used to determine whether to draw an edge or not:
    -	If r < 0.25, then an edge is added from a to b
    -	If 0.25 <=  r <= 0.7, then an edge is added from b to a
    -	If 0.7 < r 1, then no edge is added between a and b
    The function should:
    - create the graph
    - display the graph and print it in a file
    - print a message to say whether the obtained graph is connected
    (note: use "strong connectivity")
    - print the shortest path (if it exists!) between
    the node 1 and node n in the graph
    """
    G = nx.Graph()
    N = rd.randint(min_node_num,max_node_num)
    print(N)

    for i in range(1, N+1):
        G.add_node(i)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i == 1 and j == N:
                continue
            ran = rd.random()
            if ran < 0.25:
                G.add_edge(i,j)
            elif ran <= 0.7:
                G.add_edge(j,i)

    #b = nx.is_strongly_connected(G)
    if nx.is_connected(G) == True:
        print("graph is connected")
    if nx.has_path(G,1,N) == True:
        a = list(nx.shortest_simple_paths(G,1,N,None))
        print("Shortest path is ")
        print(a[0])

    return G


def longest_shortest_path(G):
    """
    Given a graph G, this functions prints on screen the longest among the shortest paths between two nodes in G.
    note that you can check whether a path exists between two nodes using nx.has_path(G, node1, node2)
    If there are more than 1 longest shortest path, then it doesn't matter which one is chosen
    """
    big = 0
    ans = []


    for i in range(1,G.number_of_nodes()-1):
        for j in range(i+1,G.number_of_nodes()):
            if nx.has_path(G,i,j) == True:
                #print(list(nx.shortest_simple_paths(G,i,j,None)))
                if len(list(nx.shortest_path(G,i,j,None,method='dijkstra'))) > big :
                    big = len(list(nx.shortest_path(G,i,j,None,method='dijkstra')))
                    ans = list(nx.shortest_path(G,i,j,None,method='dijkstra'))





    print("Longest shortest path")
    print("len is {0}".format(len(ans)))
    print(ans)


if __name__ == '__main__':
    '''
    G = modulo_digraph(6,3)
    print_graph(G)
    display_and_save(G, "graphG")
    '''

    G = create_random_graph(4,9)
    print_graph(G)


    longest_shortest_path(G)

    G = modulo_digraph(7, 2)
    print_graph(G)
    G = modulo_digraph(10, 5)
    print_graph(G)
    longest_shortest_path(G)
