

import networkx as nx
import datetime
import googlemaps

import matplotlib.pyplot as plt
from gmaps_basics1 import get_trip_info, get_gmaps_time

def graph_with_gmaps_travel_info(routemap):
    """
    This function takes as input a "routemap", i.e., a a list of tuples (origin, destination) (see exercises of
    last week) and returns a graph in which:
    - nodes are the destinations in the routemap
    - an edge is drawn if two destinations are connected, i.e., if a tuple exists in routemap connecting them
    - each edge is labelled with information about the duration of travelling between two connected nodes using a car
    ("driving") and a bicycle ("bicycling"). This information must be captured in real time using the Google Maps API.

    Assume the routemap can only contain cities in the USA as destinations

    TWIST: How much longer does is take on average to cycle as compared to driving among the destinations in routemap?
    """
    G = nx.Graph()
    G.add_edges_from(routemap, length=10)

    gmaps = googlemaps.Client(key='AIzaSyBb_wxnFj_QJjA9UJII6rU9x00pxSGMDQY')
    now = datetime.datetime.now()
    dep_time = get_gmaps_time(now.year, now.month, now.day, now.hour, now.minute)
    d = {}
    for x in routemap:
        a = get_trip_info(x[0], x[1], 'driving', dep_time, 0, gmaps)
        b = get_trip_info(x[0], x[1], 'bicycling', dep_time, 0, gmaps)
        d[x] = [a, b]
    pos = nx.spring_layout(G, k=1, iterations=50)
    plt.figure(figsize=(16,16))
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=100, node_color='pink', alpha=0.9,
            labels={node: node for node in G.nodes()})

    nx.draw_networkx_edge_labels(G, pos, edge_labels=d, font_color='red')
    plt.axis('off')
    plt.savefig("graph.png")
    plt.show()


if __name__ == '__main__':
    # use this simple routemap to test!
    rm_simple = [('Austin',"San Antonio"), ("San Antonio", "Houston"), ("Houston", "Austin"), ("Houston", "Dallas")]

    #graph_with_gmaps_travel_info(rm_simple)
    #print_graph(G)

    routemap = [('St. Louis', 'Miami'), ('St. Louis', 'San Diego'), ('St. Louis', 'Chicago'), ('San Diego', 'Chicago'),
                ('San Diego', 'San Francisco'), ('San Diego', 'Minneapolis'), ('San Diego', 'Boston'),
                ('San Diego', 'Portland'), ('San Diego', 'Seattle'), ('Tulsa', 'New York'), ('Tulsa', 'Dallas'),
                ('Phoenix', 'Cleveland'), ('Phoenix', 'Denver'), ('Phoenix', 'Dallas'), ('Chicago', 'New York'),
                ('Chicago', 'Los Angeles'), ('Miami', 'New York'), ('Miami', 'Philadelphia'), ('Miami', 'Denver'),
                ('Boston', 'Atlanta'), ('Dallas', 'Cleveland'), ('Dallas', 'Albuquerque'), ('Philadelphia', 'Atlanta'),
                ('Denver', 'Minneapolis'), ('Denver', 'Cleveland'), ('Albuquerque', 'Atlanta'),
                ('Minneapolis', 'Portland'), ('Los Angeles', 'Seattle'), ('San Francisco', 'Portland'),
                ('San Francisco', 'Seattle'), ('San Francisco', 'Cleveland'), ('Seattle', 'Portland')]
    graph_with_gmaps_travel_info(routemap)
