class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zebra(Animal):
    def __str__(self):
        return 'age: {}, name: {}, я зебра'.format(self.age, self.name)

class Dolphin(Animal):
    def __str__(self):
        return 'age: {}, name: {}, я дельфин'.format(self.age, self.name)

if __name__ == "__main__":
    z = Zebra(5, "Гера")
    d = Dolphin(14 ,"Дони")

    print(z)
    print(d)