# # #=====prob 1=====
# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
#
# if a1 > a2 and a1 > a3:
#     print("{} is max".format(a1))
#
# elif a2 > a1 and a2 > a3:
#     print("{} is max".format(a2))
#
# elif a3 > a1 and a3 > a2:
#     print("{} is max".format(a3))
#
# else:
#     print("all equal")
# # #======
# #
# # #====prob2====
# num = int(input())
#
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("Number is odd")
# # #=======
# #
# # #=====prob3=====
# #
# temp_cel = int(input("give temp in celsius"))
# temp_fah = (9/5) * temp_cel + 32
# print(temp_fah)
# #
# # #=====
# #
# # #=====prob4====
# temp_fah = int(input("give temp in fah"))
# temp_cel = (5/9) * (temp_fah - 32)
# print(temp_cel)
# #
# # #======
# #
# #
# # #=====prob5
# #
# year = int(input("Give year"))
#
# if year % 4 == 0 and (year % 100 == 1 or year % 400 == 0):
#     print("is a leap year")
# else:
#     print("not a leap year")
# #
# # #=======
# #
# #
# # #====prob6=====
# #
# swap1 = int(input("num to swap 1"))
# swap2 = int(input("num to swap 2"))
#
# swap1, swap2 = swap2, swap1
#
# print("{} and {}".format(swap1, swap2))
# #
# # #=====
# #
# # #=====prob7===
# #
# test_num = int(input("give num to test "))
#
# if test_num < 0:
#     print("negative")
# elif test_num == 0:
#     print("zer0")
# else:
#     print("positive")
# #
# # #========
# #
# # #=====prob8====
# #
# tel = input("gib tel num")
#
# print("({0}){1}".format(tel[:4], tel[4:]))
# print("{0}-{1}".format(tel[:4], tel[4:]))
# print("{0}-{1}-{2}".format(tel[:3], tel[3:6], tel[6:]))

# #=====
#
# #====prob9====
#
word = input("give a word with a *")

l_word = list(word)

for i, val in enumerate(l_word):

    if val == "*":

        del l_word[i]

        if i + 1 is not len(l_word) - 1:
            del l_word[i]

        if i is not 0:
            del l_word[i-1]

print(''.join(l_word))


#======

#=====prob10

word = input("give word for 10")

print(word[0] + word[1:].replace(word[0], "$"))

#=====