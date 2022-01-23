импорт sys
импорт argparse

def createParser ():
    parser = argparse. АргументПарсер()
    парсер. add_argument('-n')
    парсер. add_argument('--name', nargs='?')

    анализатор возврата

def фибоначи(n):
    если n == 0:
        возврат 0
    elif n == 1:
        возврат 1
    еще:
        возврат фибоначи(n-1) + фибоначи(n-2)
если __name__ == '__main__':
    parser = createParser()
    пространство имен = синтаксический анализатор. parse_args(sys. argv[1:])

    если пространство имен. n:
        print(fibonachi(int(пространство имен. н)))
    если пространство имен. имя:
        print(fibonachi(int(пространство имен. имя)))