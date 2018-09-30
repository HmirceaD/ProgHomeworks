#======prob1=====

cel_to_fah = lambda c: (9/5) * c + 32
fah_to_cel = lambda f: (5/9) * (f - 32)

celsius = [6, 11, 9.5, 15, 22, 27, 24, 30.3, 37.5, 44]
fahrenheit = [37, 29, 40, 58.6, 20, 68, 21.5, 0, 77, 34]

converted_cel = map(cel_to_fah, celsius)
converted_fah = map(fah_to_cel, fahrenheit)

print(list(converted_cel))
print(list(converted_fah))

#======

#====prob2====

text = "Now is the winter of our discontent " \
       "Made glorious summer by this sun of York; " \
       "And all the clouds that lour'd upon our house " \
       "In the deep bosom of the ocean buried. "

check_words = lambda word: len(word) > 3

result = filter(check_words, text.split(" "))

print(list(result))

#=====

#====prob3=====

from functools import reduce

l = [12, 32, 1, 73, 25, 68, 83, 29, 55, 61, 100, 97, 2]

get_max = lambda x, y: x if x > y else y

result_max = reduce(get_max, l)

print(result_max)

#======