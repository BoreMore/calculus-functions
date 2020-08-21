from calc import Limits, Derivative, Integral
import math
from decimal import Decimal


def piecewise1(x):
    if (x >= 0 and x <= 1):
        return x
    elif (x > 1 and x < 2):
        return 3 - x

# should not exist
limittest = Limits(lambda x: piecewise1(x))
print(limittest.two_sided(1))


def piecewise2(x):
    if (x > 0 and x < 1):
        return 2 - x
    elif (x > 1 and x < 2):
        return (x-2)**2

# 1
limittest = Limits(lambda x: piecewise2(x))
print(limittest.two_sided(1))

# 10
func1 = Derivative(lambda x: x**2)
print(func1.at_point(5))

# -2
func2 = Derivative(lambda x: (16/x) - (4*Decimal.sqrt(x)))
print(func2.at_point(4))

# 20.25
integratetest = Integral(lambda x: x**3)
print(integratetest.definite_integral(0.0, 3.0))

# 3250
complexintegraltest = Integral(lambda x: 12*x**3 - 9*x**2 + 2)
print(complexintegraltest.definite_integral(1, 6))

# 34.5
complexintegraltest2 = Integral(lambda z: 5*z**2 - 7*z + 3)
print(complexintegraltest2.definite_integral(-2, 1))

# 7.496204817
integralwitheuler = Integral(lambda x: math.exp(x) + 1/(x**2+1))
print(integralwitheuler.definite_integral(0, 2))