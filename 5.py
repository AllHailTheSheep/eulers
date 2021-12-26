# find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

from functools import reduce
# def lcm function for finding lcm
def lcm(a, b):
    a = int(a)
    b = int(b)
    if a > b:
        greater = a
    else:
        greater = b

    # good old brute forcing
    while True:
        if greater % a == 0 and greater % b == 0:
            current_lcm = greater
            break
        greater += 1
    # this is the lcm now, as it divides evenly with respect to both a and b
    return current_lcm


# apply aforementioned brute forcing to list of numbers to find their lcm
def get_lcm_for(list):
    return reduce(lambda x, y: lcm(x, y), list)

# get the list
lst = []
for i in range(1, int(20)+1):
  lst.append(i)
# it's brute forcing time
print("The LCM of " + str(lst) + " is " + str(get_lcm_for(lst)))
