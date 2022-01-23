def zipka(*iterables):
    tmp = []
    for i in iterables:
        tmp.append(iter(i))
    while True:
        res = []
        try:
            for i in tmp:
                res.append(next(i))
            yield tuple(res)
        except StopIteration:
            break
#for i in zipka([1, 2, 3], ['A', 'B', 'C'], ['one', 'two', 'tree']):
 #   print(i)


def MAP(function, iterable):

    it = iter(iterable)
    while True:
        try:
            print(function(next(it)))
        except StopIteration:
            break
def enumeratik(iterable):
    i = 0
    for j in iterable:
        yield (i,j)
        i += 1
#for i in enumeratik([2, 4, 6, 8, 10]):
 #   print(i)