# LOOPS (16pts TOTAL)
import random

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.


fib_1 = 1
fib_0 = 1
fib_2 = 0
print(fib_0, fib_1)
for i in range(0, 1000):
    fib_2 = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib_2
    print(fib_2)
    if fib_2 > 1000:
        break


# PROBLEM 2 (Dice Sequence - 6pts)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

for i in range(1000):
    die_1 = random.randrange(1, 7)
    die_2 = random.randrange(1, 7)
    if die_2 >= die_1:
        die_3 = random.randrange(1, 7)
        die_4 = random.randrange(1, 7)
        if die_4 >= die_3 >= die_2:
            die_5 = random.randrange(1, 7)
            die_6 = random.randrange(1, 7)
            if die_6 >= die_5 >= die_4:
                print(die_1, die_2, die_3, die_4, die_5, die_6)
                break

# PROBLEM 3 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve. 

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                number_1 = 4 * (int(str(a) + str(b) + str(c) + str(d)))
                number_2 = int(str(d) + str(c) + str(b) + str(a))
                if number_1 == number_2:
                    print(number_1 / 4)