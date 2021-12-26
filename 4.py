# find the largest palindromic number that is the product of two three digit numbers

# this can be done in like 5 lines, but this is more readable imo

# define the condition of palindrome
def is_palindrome(string):
  if string[len(string)::-1] == string:
    return True
  else:
    return False

# list of natural numbers from 100-999
nums = []
for i in range(100, 1000):
  nums.append(int(i))

# list of x * y palindromes; brute force style
palindromes = []
for x in nums:
  for y in nums:
    n = int(x * y)
    if is_palindrome(str(n)) is True:
      palindromes.append(str(n))

# so i was trying to do print(max(palindromes)) but for some reason that wasn't
# doing it so i made i own max function
highest = palindromes[0]
for num in palindromes:
  if int(num) > int(highest):
    highest = num

# print our answer
print(highest)