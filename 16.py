# sum the digits of 2^1000

from math import pow

num = int(pow(2, 1000))
sum = 0
for char in str(num):
    sum += int(char)

print(sum)