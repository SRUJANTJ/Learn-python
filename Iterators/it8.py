# Lazy Evaluation
# Iterators support lazy evaluation, which means they compute values on-the-fly. This is useful for generating sequences without consuming memory for all items at once..


def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Use the countdown function
for number in countdown(5):
    print(number)  # Outputs 5, 4, 3, 2, 1