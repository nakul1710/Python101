# Iterator = An object that returns elements one at a time from a sequence
#            (or a data stream)
#            and remembers its position in the sequence
#            A python object is an iterator if it has
#            __iter__() -> returns the iterator object itself
#            __next__() -> returns the next element in the sequence

import random

class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        self.count = 0  # Reset count for new iterations
        return self

    def __next__(self):
        if self.count < self.rolls:
            self.count += 1
            return random.randint(1, 6)
        else:
            raise StopIteration

dice = Dice(3)

for die in dice:
    print(die)
# Alternatively, you can still use the manual iterator logic if needed:
# iterator = iter(dice)
# while True:
#     try:
#         roll = next(iterator)
#         print(roll)
#     except StopIteration:
#         break
