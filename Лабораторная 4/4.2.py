из случайного импорта randint

def декоратор(функция):

    def new_chet(*args):
        if args[2] < 0:
            print('Нет')
        elif args[2] > 10:
            print('Очень много')
        еще:
            печать('Есть')
    возврат new_chet


N = рандинт(1, 15)
a = [рандинт(1, 50) для i в диапазоне(N)]
печать(a)
К = 0

def chet(a, N, K):
    для i в диапазоне(N):
        если a[i] % 2 == 0:
            К += 1
    возврат K
печать(чет(a, N, K))

chet = декоратор(chet)

чет(a, N, K)