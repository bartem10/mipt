import time
def decorator(way):

    def res_decorator(func):

        def new_func(*args, **kwargs):

            file = open(way, 'w')
            t1 = time.time()
            file.write(str(t1)+"\n")
            file.write(str(*args)+"\n")
            file.write(str(**kwargs)+"\n")
            a = func(*args, **kwargs)
            if a != None:
                print(a)
            else:
                print('-')
            t2 = time.time()
            file.write(str(t2)+"\n")
            file.write(str((t2 - t1))+"\n")
            file.close()

            return a

        return new_func

    return res_decorator

way = 'C:\\Users\\sondd\\OneDrive\\Desktop\\пример.txt'

@decorator(way)
def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)

fibonachi(5)