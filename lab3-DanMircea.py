#======prob1

import sys
def str_to_morse(text):

    for char in text:
        if char.upper() in morse_dict.keys():
            #ca sa nu printeze cu newline
            sys.stdout.write(morse_dict[char.upper()])
        elif char == " ":
            sys.stdout.write(" ")


def create_dictionary(m_dict):
    with open("morse.txt", 'r') as f:
        words = f.read().split("\n")

        for word in words:
            aux_split_word = word.split(": ")
            m_dict[aux_split_word[0]] = aux_split_word[1]


morse_dict = {}
create_dictionary(morse_dict)
str_to_morse(input("Give phrase\n"))

#=======

#=====prob2======


def create_square_dict():
    sq_dict = {}

    for i in range(1, 31):
        sq_dict[i] = i*i

    return sq_dict


square_dict = create_square_dict()
print(square_dict)

#=======