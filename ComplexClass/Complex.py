# Complex class

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def info(self):
        return self.re, self.im
    def ret_re(self):
        return self.re
    def ret_im(self):
        return self.im
    def __add__(self, other):
        return Complex(self.re + other.re , self.im + other.im)
    def __sub__(self, other):
        return Complex(self.re - other.re , self.im - other.im)
    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im , self.im * other.re  + self.re * other.im)
    def __truediv__(self, other):
        return Complex( ( self.re * other.re + self.im * other.im ) / (other.re ** 2 + other.im ** 2) , ( - self.re * other.im + self.im * other.re ) / (other.re ** 2 + other.im ** 2) )
    def __eq__(self, other):
        return ( self.re == other.re ) & ( self.im == other.im )
    def __ne__(self, other):
        return ( self.re != other.re ) | ( self.im != other.im )
    def abs(self):
        return ( (self.re ** 2 ) + ( self.im ** 2 ) ) ** 0.5
