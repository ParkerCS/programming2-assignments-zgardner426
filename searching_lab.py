import re


def linear_search(word, dictionary, line):
    key = word
    for words in dictionary:
        if words == key.upper():
            break
    else:
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
        linear_search(word, dictionary_list, line_num


file.close()

print("---Binary Search---")


file = open('search_files/.txt'
