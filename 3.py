# find the largest prime factor of 600851475143

num = 600851475143
i = 2
# since the number is odd, this script will work. its buggy with sqaures tho
while i * i < num:
    while num % i == 0:
        num = num / i
    i = i + 1
print(num)