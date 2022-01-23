import math
class Complex():
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b - other.a * self.b)

    def __truediv__(self, other):
        return Complex((self.a * other.a + self.b * other.b) / (other.a * other.a + other.b + other.b), (self.b * other.a - self.a * other.b) / (other.a * other.a + other.b + other.b))

    def __abs__(self):
        return math.sqrt(self.a * self.a + self.b * self.b)
    def __str__(self):
        # return '{} + {}i '.format(self.a, self.b)
        res = ''
        if self.a != 0:
            res += str(self.a)
        if self.b > 0:
            if res == '':
                res += ' {}i'.format(self.b)
            else:
                res += ' + {}i'.format(self.b)
        elif self.b < 0:
            if res == '':
                res += ' {}i'.format(self.b)
            else:
                res += ' - {}i'.format(-self.b)
        else:
            pass
        return(res)

if __name__ == '__main__':
    a = Complex(2, 3)
    b = Complex(2, 4)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a)
    print(b)