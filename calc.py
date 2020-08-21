import math
import sympy as sym
from decimal import Decimal


class Limits:

    def __init__(self, inputFunc):
        self.func = inputFunc
        self.dx = Decimal(1e-20)

    # subtract dx from x
    def left_side(self, x):
        value = self.func(x-self.dx)
        return round(value, 10)

    # add dx to x
    def right_side(self, x):
        value = self.func(x+self.dx)
        return round(value, 10)

    # check if two sided limit exists
    def two_sided(self, x):
        left_limit = self.left_side(x)
        right_limit = self.right_side(x)
        if left_limit == right_limit:
            return left_limit
        else:
            return "Two-sided limit does not exist for this function at x = {}".format(x)

    

class Derivative:

    def __init__(self, inputFunc):
        self.f = inputFunc
        self.dx = Decimal(1e-20)

    # calculate derivative using the limit definition of a derivative 
    def calcDerivative(self, x):
        # limit definition
        value = (self.f(x+self.dx) - self.f(x-self.dx)) / (2*self.dx)
        return round(value, 10)




# TO DO
class Integral:

    def __init__(self, inputFunc):
        self.func = inputFunc
        self.dx = 1e-10

    def definiteIntegral(self, a, b):
        # Riemann sums
        pass
