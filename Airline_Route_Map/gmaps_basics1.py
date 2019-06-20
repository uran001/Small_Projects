import googlemaps
from datetime import datetime, date, time

import re


### ===================  Some usueful given functions ===========================================
### =======================================================================================
def get_gmaps_time(year, month, day, hour, mins):
    d = date(year, month, day)
    t = time(hour, mins)
    dt = datetime.combine(d, t)
    return int(dt.timestamp())

def get_date_time(gmap_time):
    return datetime.fromtimestamp(gmap_time)

def get_formatted_address(lat, lon, gmaps):
    """
    Returns a formattedd address given the latitude and longitude of a location
    :param lat: lattude (must be float!)
    :param lon: longitude (must be float!)
    :return:
    """


    location = gmaps.reverse_geocode((lat,lon))
    #location = gmaps.reverse(lat, lon)
    return location[0]['formatted_address']



def strip_html_tags(str):
    """
    remove html tags from a string
    :param str:
    :return:
    """
    return re.sub('<[^<]+?>', '', str)

### =======================================================================================
### =======================================================================================
### =======================================================================================
""" BELOW THE FUNCTIONS THAT YOU HAVE TO IMPLEMENT """



def check_time_to_dest(origin, destination, mode, dep_time, time_limit, gmaps):
    """
    checks whether travelling to destination in a given mode takes less than time_limit
    Note that when the travellig time to destination is less than 1 hour (up to 59 min), then the value is returned in seconds
    If travelling takes more than one hour, then it is returned in minutes
    :param origin:
    :param destination:
    :param mode:
    :param time_limit:
    :return: True or False
    """
    directions_result = gmaps.directions(origin, destination, mode=mode, departure_time=dep_time, units='metric')

    duration_info = directions_result[0]["legs"][0]["duration"]
    if "hour" in duration_info['text']:
        print("Route from {0} to {1} takes more than {2} minutes".format(origin, destination, time_limit))
        return False

    return True

def get_trip_info(origin, destination, mode, dep_time, verbose, gmaps):
    """
    This function should print in a "incely formatted way" some info about a trip:
    Example:
    Trip: <origin> TO <destination>
    Mode of transport: TRANSIT
    Total time: 56 min
    Steps:
        1) Walk to somewhere : WALKING from <start_address> to <end_address>, distance: 1kim, time: 3 min
        2) Take train to somewhere: TRANSIT from ...
        3) ...
        i) <instructions> : <mode of transport> from from <start_address> to <end_address>, distance: <...>, time: <...>
        etc.

    (note that dep_time must be a "gmaps_time"



    This function should return distance (text and value) and duration (text and value)
    """
    directions_result = gmaps.directions(origin, destination, mode=mode, departure_time=dep_time, units='metric')
    print("Total time: {0} min".format(directions_result[0]['legs'][0]['duration']))

    return directions_result[0]['legs'][0]['duration']['value']

    print("Trip: {0} TO {1}".format(origin, destination))
    print("Mode of transport: {0}".format(mode))
    print("Total time: {0} min".format(directions_result[0]['legs'][0]['duration']['text']))

    print("Steps:")
    for steps in directions_result[0]['legs'][0]['steps']:
        print("        {0} : {1} from {2} to {3}, distance:{4}, time:{5}".format(   steps['travel_mode'],
                                                                                    get_formatted_address(steps['start_location']['lat'],
                                                                                    steps['start_location']['lng'], gmaps),
                                                                                    get_formatted_address(steps['end_location']['lat'], steps['end_location']['lng'], gmaps),
                                                                                    steps['distance']['text'],
                                                                                    steps['duration']['text']))

    return directions_result[0]['legs'][0]['duration']['value']



if __name__ == '__main__':


    verbose = True

    time = get_gmaps_time(2018, 11, 20, 11, 34)
    print(time)
    print(get_date_time(time))

    str = "<b>This<b> string has <i>html<i> <c>tags<c>"
    print(str)
    print(strip_html_tags(str))

    # print(get_formatted_address(40.714224, -73.961452))
    gmaps = googlemaps.Client(key='AIzaSyBb_wxnFj_QJjA9UJII6rU9x00pxSGMDQY')

    get_trip_info("Trafalgar square, London, UK", "Berlin, Germany", "transit", time, verbose, gmaps)

    print(check_time_to_dest("Trafalgar square, London, UK", "Berlin, Germany", "transit", time, 40, gmaps))

    get_trip_info("Trafalgar square, London, UK", "John O'Groats, Scotland", "transit", time, verbose, gmaps)
    print(check_time_to_dest("Trafalgar square, London, UK", "John O'Groats, Scotland", "transit", time, 40, gmaps))

    get_trip_info("San Antonio, Texas", "Austin, Texas", "driving", time, verbose, gmaps)
