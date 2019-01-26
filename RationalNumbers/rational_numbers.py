from __future__ import division
import math

def Intersection(list1, list2):
    return list(set(list1) & set(list2))

def FindFactors(num):
    result = []
    for i in range(1, int(num) + 1):
        if num % i == 0:
            result.append(i)
    return result

def GreatestCommonFactor(num1, num2):
    factors1 = FindFactors(abs(num1))
    factors2 = FindFactors(abs(num2))
    common = Intersection(factors1, factors2)
    if len(common) == 0:
        return 1
    return common[len(common) - 1]


class Rational(object):
    def __init__(self, numer, denom):
        if numer != 0 and abs(numer) != 1 and denom % numer == 0:
            denom = denom / numer
            numer = 1
        if numer == 0:
            denom = 1
        if numer < 0 and denom < 0:
            numer = abs(numer)
            denom = abs(denom)
        if numer > 0 and denom < 0:
            numer = -1 * numer
            denom = abs(denom)
        self.numer = numer
        self.denom = denom

        self.Reduce()

    def Reduce(self):
        gcf = GreatestCommonFactor(self.numer, self.denom)
        self.numer = self.numer / gcf
        self.denom = self.denom / gcf

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        num = self.numer * other.denom + self.denom * other.numer
        den = self.denom * other.denom
        return Rational(num, den)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        num = self.numer * other.numer
        den = self.denom * other.denom
        return Rational(num, den)

    def __truediv__(self, other):
        num = self.numer * other.denom
        den = self.denom * other.numer
        return Rational(num, den)
        

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power < 0:
            power = abs(power)
            return Rational(self.denom**power, self.numer **power)
        else:
            return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        if self.numer == 0:
            return 1
        return math.pow(math.pow(base, self.numer), 1 / self.denom)
