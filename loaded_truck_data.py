# Loaded Truck data.  The packages on each invidual truck have been manually inputted and also their individual departure times.
import datetime
from truck import Truck

# Create an instance of Truck representing Truck One
truck_one = Truck(16, 18, None, [15, 1, 13, 14, 16, 19, 20, 31, 34, 40, 26, 30, 37, 29], 0.0, "4001 South 700 East",
               datetime.timedelta(hours=8))

# Create an instance of Truck representing Truck Two
truck_two = Truck(16, 18, None, [3, 18, 36, 38, 2, 4, 5, 9, 7, 8, 10, 23, 24, 35], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Create an instance of Truck representing Truck Three
truck_three = Truck(16, 18, None, [6, 25, 27, 33, 28, 32, 11, 12, 17, 21, 22, 39], 0.0, "4001 South 700 East",
               datetime.timedelta(hours=9, minutes=5))


