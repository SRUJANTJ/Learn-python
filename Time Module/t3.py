# time.strftime(format, t)
# Formats a struct_time object or a tuple according to a specified format string.
# The format string uses special codes for time and date formatting, such as %Y for the year, %m for the month, etc.
import time
local_time=time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted time:", formatted_time)




# time.strptime(string, format)
# Parses a time string according to a specified format and returns a struct_time object.

import time
time_string = "2024-11-13 12:00:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print("Parsed time:", parsed_time)