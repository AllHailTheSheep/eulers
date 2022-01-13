# find the sum of all primes below 2 million

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

array = []
for i in range(0, 2000000):
    if is_prime(i) == True:
        print(i)
        array.append(i)
print(sum(array))