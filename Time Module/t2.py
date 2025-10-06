# time.gmtime(seconds)
# Converts seconds since the Epoch to a struct_time object representing UTC (Coordinated Universal Time).
# If no argument is provided, it defaults to the current time.

import time
utc_time = time.gmtime()
print("UTC time:", utc_time)




# time.mktime(t)
# Converts a struct_time object or a tuple representing local time into seconds since the Epoch.

import time
time_tuple = (2024, 11, 13, 12, 0, 0, 0, 0, 0)  # year, month, day, hour, min, sec, weekday, yearday, DST
seconds = time.mktime(time_tuple)
print("Seconds since Epoch:", seconds)