# find the difference between the sum of the first 100 sqaures and the sqaure
# of the sums of the first 100 numbers

list_of_numbers = list(range(1, 101))
sum_of_first_hundred_squared = sum(list_of_numbers) ** 2

sum = 0
for number in list_of_numbers:
    sum += number ** 2

difference = sum_of_first_hundred_squared - sum
print(difference)


