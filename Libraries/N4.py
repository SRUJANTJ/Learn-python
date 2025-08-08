#  Useful NumPy Functions in ML

import numpy as np


data = np.random.randn(5, 4)  # Random normal distribution
print(np.mean(data, axis=0))  # Mean of each column
# This calculates the mean of each column.


print(np.std(data))           # Standard deviation
# This returns the standard deviation of the entire dataset — treating all 20 numbers as a flat list.

print(np.sum(data, axis=1))   # Row sums
# This returns the sum of each row (because axis=1 means “along the columns”).
print(np.argmax(data))        # Index of max value
# It returns the index (position) of the maximum element in the flattened array (i.e., it ignores the shape and treats all numbers as one long list).






# | Function                | Purpose                            | ML Use                                     |
# | ----------------------- | ---------------------------------- | ------------------------------------------ |
# | `np.mean(data, axis=0)` | Column-wise average                | Feature centering                          |
# | `np.std(data)`          | Overall spread                     | Feature scaling                            |
# | `np.sum(data, axis=1)`  | Row totals                         | Feature aggregation                        |
# | `np.argmax(data)`       | Max value index in flattened array | Class prediction (argmax of probabilities) |
