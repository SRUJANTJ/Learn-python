# Time Module
# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications.


# time.time()
# The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time. Here's an example:
import time
print(time.time())  # Output: Current time in seconds since the epoch
# As you can see, the function returns the current time as a floating-point number, which can be used for various purposes, such as measuring the duration of an operation or the elapsed time since a certain point in time.
# The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads. Here's an example:
print("\n time.sleep() example:")

print("Start")
time.sleep(2)  # Pause for 2 seconds
print("End")
# As you can see, the function time.sleep() suspends the execution of the program for 2 seconds, allowing other parts of the program to run during that time



# time.strftime()
# The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report.

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)



# As you can see, the function time.strftime() formats the current time (obtained using time.localtime()) as a string, using a specified format. The format string contains codes that represent different parts of the time value, such as the year, the month, the day, the hour, the minute, and the second.




# time.localtime(seconds)
# Converts seconds since the Epoch to a struct_time object representing local time.
# If no argument is provided, it uses the current time.

local_time = time.localtime()
print("Local time:", local_time)