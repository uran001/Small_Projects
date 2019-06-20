import networkx as nx

# import some functions to show graphs from last week

def airline_graph(routemap):
    """
    This function is given and returns a graph built from a airline "routemap", that is, a list of tuples, where
    each tuple represent a flight connection between two cities (see example in the main)
    :param routemap:
    :return:
    """
    G = nx.Graph()
    G.add_edges_from(routemap)
    return G



def function_one(route_graph):
    """
    This function gives an answer to the following question:
     1) Given a graph "route_graph" created from a routemap, what is the maximum number of hops that would
     ever be taken by a passenger on a single trip between any two serviced cities?

     Assume that  an airline only emits tickets for the shortest path between two destinations. That is,
     if city X can be reached from A travelling through B, or C and D, or F, G and H, then only the route A,B,X
     should be considered
    """
    print("Longest Path")
    heaviest_path = max(path for path in nx.all_simple_paths(route_graph, "Portland", "Tulsa"))
    print("Number of hops from Portland to Tulsa: {0}".format(
        len(heaviest_path)))
    print("Itinerary: {0}".format(heaviest_path))

def function_two(route_graph):
    """
    This function should answer the following question:
    2) Given a graph "route_graph" created from a routemap, let us assume that route_graph refers to the route_map of
     the airline company "NoFrills".
     If you were a rich celebrity traveling everywhere across the USA and were constrained to fly NoFrills
    (probably because of lucrative endorsement deals), which city would be the most optimal place for you to live,
    to minimize the number of hops you would have to make on average as you jet from home to your latest appointment spot?
    """
    # in other words, to answer the question we should calculate the average values of the shortest paths from
    # a node in route_graph to all other nodes, and then choose the node with minimum average
    d = {}
    for x in nx.nodes(route_graph):
        cur = 0
        for y in nx.nodes(route_graph):
            if x is not y:
                cur += len(nx.shortest_path(route_graph, x, y))
        d[x] = cur / len(nx.nodes(route_graph)) - 1
    ans = (min(d.items(), key=lambda x: x[1]))
    print("The best city to choose is {0} with average distance {1}".format(ans[0], ans[1]))
if __name__ == '__main__':

    routemap = [('St. Louis', 'Miami'), ('St. Louis', 'San Diego'), ('St. Louis', 'Chicago'),
                    ('San Diego', 'Chicago'),
                    ('San Diego', 'San Francisco'), ('San Diego', 'Minneapolis'), ('San Diego', 'Boston'),
                    ('San Diego', 'Portland'), ('San Diego', 'Seattle'), ('Tulsa', 'New York'), ('Tulsa', 'Dallas'),
                    ('Phoenix', 'Cleveland'), ('Phoenix', 'Denver'), ('Phoenix', 'Dallas'), ('Chicago', 'New York'),
                    ('Chicago', 'Los Angeles'), ('Miami', 'New York'), ('Miami', 'Philadelphia'), ('Miami', 'Denver'),
                    ('Boston', 'Atlanta'), ('Dallas', 'Cleveland'), ('Dallas', 'Albuquerque'),
                    ('Philadelphia', 'Atlanta'),
                    ('Denver', 'Minneapolis'), ('Denver', 'Cleveland'), ('Albuquerque', 'Atlanta'),
                    ('Minneapolis', 'Portland'), ('Los Angeles', 'Seattle'), ('San Francisco', 'Portland'),
                    ('San Francisco', 'Seattle'), ('San Francisco', 'Cleveland'), ('Seattle', 'Portland')]

    routemap_graph = airline_graph(routemap)
    print(nx.info(routemap_graph))
    print("Number of hops from Portland to Tulsa: {0}".format(
        len(nx.shortest_path(routemap_graph, "Portland", "Tulsa")) - 1))
    print("Itinerary: {0}".format(nx.shortest_path(routemap_graph, "Portland", "Tulsa")))

    function_one(routemap_graph)
    function_two(routemap_graph)