'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.  (read the file line by line to accomplish this task)


file = open('search_files/dictionary.txt')

longest_word = " "
word_lens = []
word_list = []


for lines in file:
    words = split_line(lines)
    for word in words:
        word_list.append(word)
file.close()


file = open('search_files/dictionary.txt')

for lines in file:
    words = split_line(lines)
    for word in words:
        word_lens.append(len(word))
file.close()


len_long_word = max(word_lens)
index = word_lens.index(len_long_word)
longest_word = word_list[index]
print(longest_word)


#2.  (7pts)  Write code which finds
#  The total word count AND average word length of "AliceInWonderLand.txt"

word_count = 0
average_list = []
average = 0

file = open('search_files/AliceInWonderLand.txt')
for lines in file:
    words = split_line(lines)
    for word in words:
        word_count += 1
        average_list.append(len(word))


for numbers in average_list:
    average += numbers


average = average/(len(average_list))
print("Word Count:", word_count, "Average word length:", average)

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
file = open('search_files/AliceInWonderLand.txt')
num_cat = 0


for lines in file:
    words = split_line(lines)
    for word in words:
        if word == "Cat":
            num_cat += 1

print(num_cat)
file.close()

# How many times does "Cheshire" immediately followed by "Cat" occur?
file = open('search_files/AliceInWonderLand.txt')


num_cheshire = 0
book = []


for lines in file:
    words = split_line(lines)
    for word in words:
        book.append(word)


for i in range(len(book)):
    if book[i] == "Cheshire":
        if book[i + 1].upper() == "CAT":
            num_cheshire += 1
    else:
        continue


print(num_cheshire)
file.close()

#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"




# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.




