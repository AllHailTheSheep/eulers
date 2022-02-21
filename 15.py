# find the number of routes that can be traveled to traverse a 20x20
# grid starting at the top left using only the directions down and right
# im not actually going to write a program because this can be solved with math

from math import factorial
n = 20
print(factorial(2 * n) / (factorial(n) * factorial(n)))