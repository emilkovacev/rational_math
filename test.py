from ratio import Fraction, RMath
from itertools import combinations


# to account for rounding errors in precision
def is_equal(a: float, b: float):
    return a - b < 0.000000000001


class Tests:

    def __init__(self, r):
        self.r = r

    def addition(self):
        for i in combinations(range(1, self.r), 2):
            for j in combinations(range(1, self.r), 2):
                a = Fraction(i[0], i[1])
                b = Fraction(j[0], j[1])

                add = RMath.add(a, b)
                if not is_equal(add.eval(), a.eval() + b.eval()):
                    print(f'error: {add.eval()} != {a.eval()} + {b.eval()}')

    def subtraction(self):
        for i in combinations(range(1, self.r), 2):
            for j in combinations(range(1, self.r), 2):
                a = Fraction(i[0], i[1])
                b = Fraction(j[0], j[1])

                sub = RMath.subtract(a, b)
                if not is_equal(sub.eval(), a.eval() - b.eval()):
                    print(f'error: {sub.eval()} != {a.eval()} - {b.eval()}')

    def multiplication(self):
        for i in combinations(range(1, self.r), 2):
            for j in combinations(range(1, self.r), 2):
                a = Fraction(i[0], i[1])
                b = Fraction(j[0], j[1])

                mult = RMath.multiply(a, b)
                if not is_equal(mult.eval(), a.eval() * b.eval()):
                    print(f'error: {mult.eval()} != {a.eval()} * {b.eval()}')

    def division(self):
        for i in combinations(range(1, self.r), 2):
            for j in combinations(range(1, self.r), 2):
                a = Fraction(i[0], i[1])
                b = Fraction(j[0], j[1])

                div = RMath.divide(a, b)
                if not is_equal(div.eval(), a.eval() / b.eval()):
                    print(f'error: {div.eval()} != {a.eval()} * {b.eval()}')


t = Tests(20)
t.addition()
t.subtraction()
t.multiplication()
t.division()
print('done :)')
