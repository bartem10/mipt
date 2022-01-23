with open('Упражнение_1.txt' , 'w') as file:
    file.write('   jglygdgdbdbdlb')
    file.write(' ubfbbbbluibb \n')
file.close()

F = input()
try:
    # a = 1 / 0
    with open(F, 'r') as file:
        for line in file:
            print(line.strip())
    file.close()

except FileNotFoundError:
    print("Error! Введите другое имя!")
except Exception:
    print("ERROR !!!")