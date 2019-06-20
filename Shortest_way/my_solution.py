import networkx as nx
import matplotlib.pyplot as plt

station_line = {}
station_latitude = {}
flag = 1000000.0


def get_lex(a, b):
    i = 0
    while 1:
        if i >= min(len(a), len(b)):
            return 1
        if a[i] != b[i]:
            return abs(ord(a[i]) - ord(b[i]))- 1
        i += 1

def get_lat(a, b):
    if a not in station_latitude or b not in station_latitude:
        return flag
    return abs(station_latitude[a] - station_latitude[b])





def get_nodes_from_file(f):
    line_of_station = ""

    my_nodes = []

    for line in f.readlines():
        if "Line:" not in line:
            node = line.strip()
            my_nodes.append(node)
            station_line[node] = line_of_station
        else:
            new_line = line.split(" ")
            line_of_station = new_line[1].strip()

    return my_nodes

def get_graph_from_nodes(nodes):
    prev_node = "Nope"
    G = nx.Graph()

    for node in nodes:
        if prev_node != "Nope":
            G.add_edge(prev_node, node, default=1, lex=get_lex(prev_node, node), lat=get_lat(prev_node, node))
        prev_node = node

    G.add_nodes_from(nodes)

    return G

def f(tube_lines, tube_loc):
    tube_file = open(tube_lines, "r")
    file_tubloc = open(tube_loc, "r")

    nodes = get_nodes_from_file(tube_file)

    for line in file_tubloc.readlines():
        line.strip()
        new_line = line.split("\t")
        node = new_line[0].strip()
        lat_str = new_line[1].split(" ")[0].strip()
        lat = float(lat_str)
        station_latitude[node] = lat

    G = get_graph_from_nodes(nodes)

    tube_file.close()
    file_tubloc.close()

    return G

def calc(G, A, B, type):
    return (nx.shortest_path(G, A, B, weight=type))


if __name__ == '__main__':

    make_graph = f("tube_lines.txt", "tube_locations.txt")

    A = "Brent Cross"
    B = "Rickmansworth"

    print("Number of stations between two given stations: {0} and {1} is ====> {2}\n".format(A, B, len(calc(make_graph, A, B, "default")) - 2))

    print("DEFAULT PATH")

    ite = 1

    for station in calc(make_graph, A, B, "default"):
        print("{0} ----------- {1} ----------- {2}".format(ite, station, station_line[station]))
        ite += 1

    ite = 1
    result = []
    acc = 0
    prev_station = "Nope"

    for station in calc(make_graph, A, B, "lex"):
        result.append("{0} ----------- {1} ----------- {2}".format(ite, station, station_line[station]))
        if prev_station != "-1":
            acc += get_lex(prev_station, station)
        prev_station = station
        ite += 1

    print("\n\nLexigraphical distance ---------- {0}\n".format(acc))

    print("LEXIGRAPHICAL PATH")

    for station in result:
        print(station)

    ite = 1
    result = []
    acc = 0.0
    prev_station = "Nope"

    for station in calc(make_graph, A, B, "lat"):
        result.append("{0}==> {1} in {2}".format(ite, station, station_line[station]))
        if prev_station != "Nope":
            acc += get_lat(prev_station, station)
        prev_station = station
        ite += 1

    print("\nLatitude distance ------------- {0}\n".format(acc))

    print("LATITUDE PATH")

    for station in result:
        print(station)
