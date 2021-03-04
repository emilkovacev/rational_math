from ratio import Fraction, RMath

# implement strict tests


a = 562
b = 38
c = 37
d = 11
if RMath.add(Fraction(a, b), Fraction(c, d)).eval() != a / b + c / d:
    print(False)
print(True)
