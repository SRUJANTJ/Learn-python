# Streaming Data
# In applications like video streaming, audio streaming, or real-time data feeds, iterators help manage the flow of data efficiently. They allow you to process data as it comes in rather than waiting for the entire data set.
class Stream:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Simulating streaming data
data_stream = Stream(['packet1', 'packet2', 'packet3'])
for packet in data_stream:
    print(f"Processing {packet}")