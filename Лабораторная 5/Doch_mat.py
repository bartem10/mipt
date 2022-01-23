class mother():

    def __str__(self):
        return "I am mother"

class daughter(mother):
    def __str__(self):
        return "I am daughter"



if __name__ == "__main__":
    m = mother()
    d = daughter()
    print(m)
    print(d)