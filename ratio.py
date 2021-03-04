import math


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.num: int = numerator
        self.den: int = denominator

    def __str__(self):
        return f'{self.num}/{self.den}'

    def multiply(self, c):
        return Fraction(self.num * c, self.den * c)

    def simplify(self):
        i: int = min(self.num, self.den)
        while i > 1:
            if self.num % i == 0 and self.den % i == 0:
                return Fraction(self.num // i, self.den // i)
            i -= 1
        return self

    def opposite(self):
        return Fraction(self.num * -1, self.den)

    def reciprocal(self):
        return Fraction(self.den, self.num)

    def eval(self):
        return self.num / self.den


class RMath:
    @classmethod
    def add(self, a: Fraction, b: Fraction):
        lcm: int = math.lcm(a.den, b.den)
        c: Fraction = a.multiply(lcm // a.den)
        d: Fraction = b.multiply(lcm // b.den)
        return Fraction(c.num + d.num, lcm).simplify()

    @classmethod
    def subtract(self, a: Fraction, b: Fraction):
        return self.add(a, b.opposite())

    @classmethod
    def multiply(self, a: Fraction, b: Fraction):
        return Fraction(a.num * b.num, a.den * b.den).simplify()

    @classmethod
    def divide(self, a: Fraction, b: Fraction):
        return self.multiply(a, b.reciprocal())
