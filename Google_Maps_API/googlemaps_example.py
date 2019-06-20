import googlemaps

from datetime import datetime, date, time


def get_gmaps_time(year, month, day, hour, mins):
    d = date(year, month, day)
    t = time(hour, mins)
    dt = datetime.combine(d, t)
    return int(dt.timestamp())


if __name__ == '__main__':

    your_key = 'AIzaSyBb_wxnFj_QJjA9UJII6rU9x00pxSGMDQY'

    gmaps = googlemaps.Client(key=your_key)                                   # initialise the gmaps api object

    print("============== Example of value returned when geocoding an address:")
    geocode_result = gmaps.geocode('Wimbledon station, London')                          # call the geocoder
    print(geocode_result)                                                                # To-Do: look at the data structure returned by the geocoder

    print(" ")

    print("============== Example of value returned when reverse geocoding coordinates (latitude, longitude):")
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))             # Note: coordinates must be in a tuple (<lon>, <lat>)
    print(reverse_geocode_result)

    print(" ")

    dep_time = get_gmaps_time(2017, 10, 20, 11, 34)                                     # create example departure time, to be used in the example (always pick a time in the future!)

    # ================================================================================================================================================
    # ================================================================================================================================================


    origin = "Trafalgar square, London, UK"
    destination = "Wimbledon, London, UK"

    print(" ")
    print("============== Example of directions returned by python-gmaps:")

    # get directions from Gmaps:
    # mode: driving, walking etc. see: https://developers.google.com/maps/documentation/directions/intro#TravelModes
    # departure time: must be an integer timestamp, the function get_gmaps_time() can be used to obtain such a timestamp
    # units: metric or imperial (use always metric!) https://developers.google.com/maps/documentation/directions/intro#UnitSystems
    # other possible parameters at https://developers.google.com/maps/documentation/directions/intro#RequestParameters
    directions_result = gmaps.directions(origin, destination, mode="transit", departure_time=dep_time, units='metric')

    print(" ")
    print(directions_result)

    # ================================================================================================================================================
    # ================================================================================================================================================

    print(" ")
    print("============== Inspecting the content of the variable returned by directions (a list with one complex dictionary inside...)")
    print(len(directions_result))
    print(directions_result[0].keys())                                                          # most useful information is at the key "legs"
    print(directions_result[0]['legs'][0].keys())                                               # directions_result[0]['legs'][0] is itself a dictionary
    print("\n")
    for key in directions_result[0]['legs'][0].keys():
        print("{0} : {1}".format(key,directions_result[0]['legs'][0][key]))

    print("\n")
    for step in directions_result[0]['legs'][0]['steps']:                                       # within "legs", "steps" contains information about indivdual steps of the trip
        print(step)



