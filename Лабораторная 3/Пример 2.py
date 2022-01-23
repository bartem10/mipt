def write_array(array, file):
    file.writelines(array)
    pass

file = open("Упражнение_2", "w")
array = [ 'I', 'am', 'Ivan', '!']
array = map(lambda x:x + '\n', array)
write_array(array, file)
file.close()

file = open("Упражнение_2", "r")
for line in file:
    print( line.strip())
file.close()