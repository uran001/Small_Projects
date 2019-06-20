Flight Landing Control
        
    
    A simple flight landing control simulator using the AdaptableHeapPriorityQueue class.
    
    NOTE: the AdaptableHeapPriorityQueue class implements a min-heap, that is, the HIGHEST priority is given to the
    elements with the LOWEST value of the priority attributes (e.g., priority = 2 has HIGHEST priority than priority = 3)
    
    The simulator reads events from a text file (see flight_control.txt for the example used in the main) and
    processes events based on the following logic:
    
    The tasks to perform depend on the type of event. There are 5 types of events:
    
    1) "flight_no,type" : a new flight has approached the airport airspace and it is ready to queue for landing
    flight_no : a string like XX1234, e.g. AZ1234, KY0987
    type : can be "short", "national", or "long"
    When approaching the airport airspace, by default short flights are assigned priority 2, national flight priority 4,
    and long flights priority 6
    
    2) "flight,land" : the next flight with highest priority 😊 lowest value of the priority attribute) in the queue must land
    (note: we will use min-heaps, so highest priority means minimum value of the priority attribute,
    that is, a flight A with priority 2 must land before a flight B with priority 3)
    
    3) "weather,rain start" : it starts raining!!!!
    Flights beginning with "AZ" use very old aircrafts that cannot handle rain very well, so their priority must
    be decreased of 2 when rain starts
    
    3) "weather,rain stopped" : it stopped raining!!!!
    Priority of flights beginning with "AZ" must be increased by 2 to restore "normal" priorities
    
    4) "flight_no,sick passenger" : there is a sick passenger on board flight flight_no!!!!!
    Priority of flight flight_no must be set to 1
    
    5) "flight_no,fuel low" : the fuel level on flight flight_no is low!!!!
    Priority of flight flight_no must be set to 1
    

        