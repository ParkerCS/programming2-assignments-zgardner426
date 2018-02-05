#FUNCTIONS AND IMPORTS (20PTS TOTAL)
# Be sure to comment all your functions as shown in notes

#PROBLEM 1 (how many upper case - 4pts)
# Make a function takes a string as a parameter, then prints how many upper case letters are contained in the string.
# A loop that compares each letter to the .upper() or .lower() of itself will suffice.
def function_1(word):
    count = 0
    for letters in word:
        if letters == letters.upper():
            count += 1
            if letters == " ":
                count -= 1
    print(count)


function_1("Hi My name is Zoe")

# PROBLEM 2 (Biggest, smallest, average - 4pts)
# Make a function which takes 3 numbers as parameters.
# The function then prints the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.


def function_2(num1, num2, num3):
    greatest_number = max(num1, num2, num3)
    lowest_number = min(num1, num2, num3)
    average = (num1 + num2 + num3) / 3
    print("Greatest Number = ", greatest_number)
    print("Lowest Number = ", lowest_number)
    print("Average = {:.2f}".format(average))


function_2(189, 782, 23)


# PROBLEM 4 (add me, multiply me - 4pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def function_3(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    print("The sum of {} and {} is {}".format(num1, num2, sum))
    print("The product of {} and {} is {}".format(num1, num2, product))


function_3(13, 89)


# PROBLEM 5 (Login - 4pts)
# Make a file called import_me.py in this same project
# Inside this new module/file, make a login function which works according to the flow diagram PasswordFlowchart.png in this folder
# Substitute your name for Rohan's, and use whatever generic password you want.

# PROBLEM 6 (main - 4pts)
# import the file import_me from Problem 5
# Create a main program using the format if __name__ == "__main__": 
# Place every call from problems 1 through 5 into this program.


import import_me


if __name__ == "__main__":
    function_1("What's up Everybody")
    function_2(123, 38, 9)
    function_3(34, 7987)
    import_me.password_function()

