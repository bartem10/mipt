from random import randint

def decorator(function):

    def new_chet(*args):
        if args[2] < 0:
            print('Нет')
        elif args[2] > 10:
            print('Очень много')
        else:
            print('Есть')
    return new_chet


N = randint(1, 15)
a = [randint(1, 50) for i in range(N)]
print(a)
K = 0

def chet(a, N, K):
    for i in range(N):
        if a[i] % 2 == 0:
            K += 1
    return K
print(chet(a, N, K))

chet = decorator(chet)

chet(a, N, K)