# find the first triangle number to have over 500 divisors
import math

def find_nth_trangle_number(n):
    return n * (n + 1) / 2

def find_divisors(n):
    divisors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            divisors += 2
        if i*i==n:
            divisors -= 1
    return divisors

i = 1
while True:
    num = find_nth_trangle_number(i)
    divisors = find_divisors(num)
    print("{0}: {1}".format(int(num), divisors))
    if divisors > 500:
        exit(0)
    i += 1