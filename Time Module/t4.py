# time.perf_counter()
# Returns the value of a performance counter (in fractional seconds) for precise timing, often used for benchmarking.

import time
start = time.perf_counter()
# Code to measure goes here
end = time.perf_counter()
print("Elapsed time:", end - start)


# time.process_time()
# Returns the sum of system and user CPU time of the current process, useful for measuring CPU time taken by a process.


start = time.process_time()
# Code to measure CPU time
end = time.process_time()
print("CPU time used:", end - start)