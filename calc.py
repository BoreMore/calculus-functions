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
    def at_point(self, x):
        # limit definition
        value = (self.f(x+self.dx) - self.f(x-self.dx)) / (2*self.dx)
        return round(value, 10)




class Integral:

    def __init__(self, inputFunc):
        self.func = inputFunc

    # use riemann sums to calculate integral 
    def definite_integral(self, a, b, n=10000000):
        dx = (b-a)/n

        step = a
        sum = 0

        for _ in range(n):
            sum += self.func(step)*dx
            step += dx

        return round(sum, 10)
