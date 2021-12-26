# find the sum of all multiples of 3 and 5 below 1000

lst = []
# declare range 
for i in range(1, 1000):
  lst.append(i)
# new list for multiples of 3 or 5
to_sum = []
for x in lst:
  if x % 3 == 0 or x % 5 == 0:
    to_sum.append(x)
# print the sum of all elements of the list
print(sum(to_sum))