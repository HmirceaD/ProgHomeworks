#======prob1=====

import re

text = "Now is the winter of our discontent " \
       "Made glorious summer by this sun of York; " \
       "And all the clouds that lour'd upon our house " \
       "In the deep bosom of the ocean buried." \

split_text = re.findall("[, ;.\n]+", text)
print(len(split_text))

num_vowels = 0

for word in split_text:
    for char in word:
        if char.lower() in "aeiou":
            num_vowels += 1

print("Number of vowels is {}".format(num_vowels))

#========

#======prob2=======

monty_list = ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']

monty_list = monty_list[::-1]

print(monty_list)

#======

#=====prob3=======

pali = input("Give a number to check if palindrome")

if pali == pali[::-1]:
    print("Object is a palindrome")
else:
    print("Object is not a palindrome")

#=========

#====prob4=====

def common_elems(list1, list2):
    return list(set(list1) - (set(list1) - set(list2)))


l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [2, 4, 9, 11, 33]

print(common_elems(l1, l2))

#========

#====prob5=====

def check_divis(num):
    if num >= 1000 and num <= 2000 and num % 7 == 0 and num % 5 == 1:
        return True
    else:
        return False

true_numbers = []

for i in range(1000, 2001):
    if check_divis(i):
        true_numbers.append(i)

print(true_numbers)

#======


#======prob6 ======

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

print(factorial(6))
print(factorial(0))

#=====

#======prob7 ======


def remove_dups(ls):
    return list(set(ls))


def remove_min_max(ls):
    ls.remove(max(ls))
    ls.remove(min(ls))


def compute_avg(ls):
    return sum(ls) / float(len(ls))


lista_cu_treburi = [10, 20, 20, 30, 30, 56, 67, 75, 22, 10, 33]

lista_cu_treburi = remove_dups(lista_cu_treburi)
remove_min_max(lista_cu_treburi)
print(compute_avg(lista_cu_treburi))
print(lista_cu_treburi)

#=====