import re


def linear_search(word, dictionary, line):
    key = word
    for words in dictionary:
        if words == key.upper():
            break
    else:
        print("Line:", line, "Possible Misspelled Word:", word)


def binary_search(word, dictionary, line):
    lower_bound = 0
    upper_bound = len(dictionary) - 1
    a_word = False

    while not a_word and lower_bound <= upper_bound:
        middle_pos = (upper_bound + lower_bound) // 2
        if dictionary[middle_pos].upper() < word.upper():
            lower_bound = middle_pos + 1
        elif dictionary[middle_pos].upper() > word.upper():
            upper_bound = middle_pos - 1
        else:
            a_word = True


    if not a_word:
        print("Line:", line, "Possible Misspelled Word:", word)



def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


file = open('search_files/dictionary.txt')


dictionary_list = []
for lines in file:
    split_line(lines)
    dictionary_list.append(lines.strip())


file.close()

print("--- Linear Search ---")

file = open('search_files/AliceInWonderLand200.txt')
line_num = 0

for line in file:
    words = split_line(line)
    line_num += 1
    for word in words:
        linear_search(word, dictionary_list, line_num)


file.close()


print("---Binary Search---")


file = open('search_files/AliceInWonderLand.txt')
line_num2 = 0

for line in file:
    words = split_line(line)
    line_num2 += 1
    for word in words:
        binary_search(word, dictionary_list, line_num2)


file.close()

