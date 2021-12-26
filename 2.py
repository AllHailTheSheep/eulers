# find the sum of all even valued terms of the fibonacci sequence that do not exceed four million

# sequence generator
a = 0
b = 1
fibs = []
while b < 4000000:
  a = a + b
  b = b + a
  fibs.append(a)
  fibs.append(b)
# just get the even ones
to_sum = []
for i in fibs:
  if i % 2 == 0:
    to_sum.append(i)
# print the answer
print(sum(to_sum))