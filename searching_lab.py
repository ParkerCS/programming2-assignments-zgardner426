import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


file = open('search_files/dictionary.txt')


dictionary_list = []
for lines in file:
    split_line(lines)
    dictionary_list.append(lines.strip())


print(dictionary_list)