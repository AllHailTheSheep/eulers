# find the longest collatz sequence with a starting digit below a million

def collatz(number):
    if number % 2 == 0:
        return number/2
    else:
        return (3 * number) + 1

highest_steps = 0
highest_steps_num = 2
for i in range(2, 1000000):
    steps = 1
    number = i
    while number != 1:
        number = collatz(number)
        steps += 1
    if steps > highest_steps:
        highest_steps = steps
        highest_steps_num = i

print(highest_steps, highest_steps_num)
