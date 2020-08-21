from calc import Limits, Derivative, Integral


def piecewise1(x):
    if (x >= 0 and x <= 1):
        return x
    elif (x > 1 and x < 2):
        return 3 - x

limittest = Limits(lambda x: piecewise1(x))
print(limittest.two_sided(1))


def piecewise2(x):
    if (x > 0 and x < 1):
        return 2 - x
    elif (x > 1 and x < 2):
        return (x-2)**2

limittest = Limits(lambda x: piecewise2(x))
print(limittest.two_sided(1))


func1 = Derivative(lambda x: x**2)
print(func1.calcDerivative(5))
