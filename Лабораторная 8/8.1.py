def print_map(function, iterable):
    for i in iterable:
        print(function(i))


def print_map(function, iterable):
        it = iter(iterable)
        while True:
            try:
                print(function(next(it)))
            except StopIteration:
                break
import math
print_map(math.sqrt, [1, 4, 9])