#2. 1)
x = float(input("ievadi x skaitli: "))
y = float(input("ievadi y skaitli: "))

from fractions import Fraction
frac = Fraction(2+x, x*y)

#2. 2)
x = float(input("ievadi x skaitli: "))
result = 5 * x**3 - x**2 + 7 * x - 6

#2. 3)
x = float(input("ievadi x skaitli: "))
y = float(input("ievadi y skaitli: ")) 
result = (x * y)  ** 0.5
print(result) 

#2. 4)
from fractions import Fraction
x = float(input("ievadi x skaitli: "))
y = float(input("ievadi y skaitli: "))

numerator = 2 ** (x* y)
denominator = 5 *y

fraction = Fraction(numerator, denominator)
print(fraction)