
from adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
import time
class FlightLandingControl():

    def __init__(self, event_file):
        """
        This function initialises the simulator.
        :param event_file: the file containing the "events" received by flight control
        """
        self._queue = AdaptableHeapPriorityQueue()
        self._locator = {}
        self._event_file = event_file



    def _add_flight(self, priority, flight_no):
        """
        This function adds a flight to the queue.
        :param priority: the priority level of the flight
        :param flight_no: the flight
        :return:
        """
        loc = self._queue.add(priority, flight_no)
        self._locator[flight_no] = [loc, priority]


    def _update(self, new_priority, flight_no):
        """
        This function updates the level of priority of a flight in the queue
        :param new_priority: the new level of priority
        :param flight_no: the flight
        """
        loc = self._locator[flight_no]
        self._queue.update(loc[0], new_priority, flight_no)

    def _land(self):
        """
        This function simulates the landing of a flight by printing a message e.g.:
        "Flight AZ1100 landed!"
        """
        print("Flight {0} landed!".format(self._queue.remove_min()))

    def _process_event(self,line):
        """
        This function should process one event contained in one "line" of the events file.
        :param line: a string representing the event, e.g. KK8989,sick passenger; flight,land; AZ1012,national etc.
        """
        values = list(line.split(','))
        flight_no = values[0]
        event = values[1]

        if event == "short" :
            self._add_flight(2, flight_no)
        elif event == "long":
            self._add_flight(4, flight_no)
        elif event == "national":
            self._add_flight(6, flight_no)
        elif event == "land":
            self._land()
        elif event == "sick passenger":
            self._update(1, flight_no)
        elif event == "fuel low":
            self._update(1, flight_no)
        elif len(values) == 3:
            if values[2] == 'start':
                for loc in self._locator:
                    if loc[0] == 'A' and loc[1] == 'Z':
                        dat = self._locator[loc]
                        self._queue.update(dat[0], dat[1] - 2, flight_no)
            if values[2] == 'stop':
                for loc in self._locator:
                    if loc[0] == 'A' and loc[1] == 'Z':
                        dat = self._locator[loc]
                        self._queue.update(dat[0], dat[1] + 2, flight_no)


    def process_event_file(self):
        # open event file for reading
        file = open(self._event_file, "r")
        # each line is a new event
        for line in file.readlines():
            print("******************** Processing new event: {0}".format(line))
            self._process_event(line)
            time.sleep(0.5)






if __name__ == '__main__':
    """# ========== Use this code to test some events in your simulator
    FLC = FlightLandingControl()
    FLC.add_flight(2, "AZ2525")
    FLC.add_flight(5, "AZ6666")
    FLC.add_flight(3, "AZ5555")
    FLC.check_next()
    FLC.land()
    FLC.add_flight(2, "AZ7777")
    FLC.check_next()
    FLC.update(1,"AZ5555")
    FLC.add_flight(7, "AZ0000")
    FLC.add_flight(1, "KK0000")
    FLC.land()
    FLC.land()
    FLC.land()
    FLC.land()
    FLC.land()
    """
    # simulate flight control by reading from a file """

    # " ============================================= "
    # Use this code to test your simulator
    FLC = FlightLandingControl("flight_control.txt")
    FLC.process_event_file()