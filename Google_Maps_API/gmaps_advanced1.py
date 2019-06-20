import googlemaps

from gmaps_basics1 import get_trip_info, get_gmaps_time

def quickest_mode_of_transport(origin, destination, dep_time, gmaps):
    """
    This function calculates and prints on the screen the quickest way of transport
    between origin and destination among ["driving", "walking", "bicycling", "transit"]

    Note that duration the trip duration returned by gmaps follows this rule:
    - of the trip takes 1 hour or more, then the duration value is returned in minutes
    - if the trip takes less than 1 hour, then the duration is returned in seconds

    Assume that trips between origin and destination take less than 24 hours in any travel mode


    :param origin:
    :param destination:
    :return:
    """

    a = get_trip_info(origin, destination, 'driving', dep_time, 0, gmaps)
    b = get_trip_info(origin, destination, 'walking', dep_time, 0, gmaps)
    c = get_trip_info(origin, destination, 'bicycling', dep_time, 0, gmaps)
    d = get_trip_info(origin, destination, 'transit', dep_time, 0, gmaps)
    e = min(a, b, c, d)
    if a == e:
        print("Quickest way is Driving time takes {0} sec".format(get_trip_info(origin, destination, 'driving', dep_time, 0, gmaps)))
    elif b == e:
        print("Quickest way is Driving time takes {0} sec".format(get_trip_info(origin, destination, 'walking', dep_time, 0, gmaps)))
    elif c == e:
        print("Quickest way is Driving time takes {0} sec".format(get_trip_info(origin, destination, 'bicycling', dep_time, 0, gmaps)))
    elif d == e:
        print("Quickest way is Driving time takes {0} sec".format(get_trip_info(origin, destination, 'transit', dep_time, 0, gmaps)))



def calculate_fuel_cost(itinerary, dep_time, price_per_liter, km_per_liter, gmaps):
    """
    This function calculates the fuel cost for a given trip specified in itinerary

    :param itinerary: a list of places to visit (see example of use in the main)
    :param dep_time: the departure time
    :param price_per_liter: the price per liter of fuel (e.g. 1322 won/l)
    "param km_per_litre: the efficiency of the vehicle used for travelling (expressed in km travelled with 1 liter of fuel, e.g. 15.6 km/l)
    """
    mode = 'driving'

    print("\n\n")
    total = 0

    for i in range(len(itinerary)-1):

        origin      = itinerary[i]
        destination = itinerary[i+1]

        directions_result = gmaps.directions(origin, destination, mode=mode, departure_time=dep_time, units='metric')
        print("Trip: {0} TO {1}".format(origin, destination))
        print("Mode of transport: {0}".format(mode))
        print("Total distance: {0}".format(directions_result[0]['legs'][0]['distance']))
        print("\n\n")
        total += int( directions_result[0]['legs'][0]['distance']['value'])


    print(" Total cost = {0}".format((total / km_per_liter) * price_per_liter))


if __name__ == '__main__':


    # print(get_formatted_address(40.714224, -73.961452))
    gmaps = googlemaps.Client(key='AIzaSyBb_wxnFj_QJjA9UJII6rU9x00pxSGMDQY')


    dep_time = get_gmaps_time(2018, 11, 20, 11, 34)

    quickest_mode_of_transport("Cupertino, California", "Mountain View, California", dep_time, gmaps)
    quickest_mode_of_transport("Piccadilly Circus, London, UK", "Waterloo station, London, UK", dep_time, gmaps)

    calculate_fuel_cost(["Austin, Texas", "Los Angeles, California", "Las Vegas, Nevada", "San Francisco, California"], dep_time, 1168, 15.6, gmaps)
    calculate_fuel_cost(["London, UK", "Birmingham, UK", "Newcastle, UK", "Edinburgh, Scotland"], dep_time, 1168, 15.6, gmaps)