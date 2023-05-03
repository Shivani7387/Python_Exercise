# Lab Assignments:
# Q.1. Write a program that asks the user how many days are in a particular month, and what day of
# the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for
# that month. For example, here is the output for a 30-day month that begins on day 4 (Thursday):
# S M T W T F S
#  1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30

# Solution ---------------

# input_number_of_days = int(input("Days: "))
# start_day_of_week = int(input('0: Monday 1 : Tuesday ... '))
# print(f'S  M  T  W  T  F  S')
# cnt = 1
# for i in range((start_day_of_week-1)*-1, input_number_of_days+1,1):
#     print(f'{i:2}' if i > 0 else ' ' , end= ' ')
#     if cnt%7 == 0 :
#         print('')
#     cnt = cnt+1

#---------------------------------------------------------------------------------------------------------------------------------

# Q. 2. Define a procedure histogram() that takes a list of integers and prints a histogram to the
# screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

# Solution -----------------------------

# list1 = [4,9,7]
# j=0
# i=0
# for i in range(0,len(list1)):
#     print("\n")
#     for j in range(int(list1[i])):
#         print("*",end="")

#---------------------------------------------------------------------------------------------------------------------------------

# Q. 3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go
# hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan,
# Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired
# nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation,
# capitalization, and spacing are usually ignored.

# Solution ----------------------------------

import string as str
def isPal(s):
    return s == s[::-1]
str1 = "Go hang a salami I'm a lasagna hog"
str2 = "Was it a rat I saw?"
str3 = "Step on no pets"
str4 = "Sit on a potato pan, Otis"
str5 = "Lisa Bonet ate no basil"
str6 = "Satan, oscillate my metallic sonatas"
str7 = "I roamed under it as a tired nude Maori"
str8 = "Rise to vote sir"
str9 = "Dammit, I'm mad!"
list1 = [str1,str2,str3,str4,str5,str6,str7,str8,str9]
for s in list1:
    for char in str.punctuation:
        s = s.replace(" ", "")
        s = (s.replace(char, "")).lower()
        #str1 = str1.lower()
    print(s)
    print(s[::-1])
    res = isPal(s)
    print("YES" if res else "NO")

#----------------------------------------------------------------------------------------------------------------------------

# Q. 4. A pangram is a sentence that contains all the letters of the English alphabet at least once, for
# example: The quick brown fox jumps over the lazy dog

# Solution --------------------

# import re
# def ispangram(s):
#     str = re.search(r'[a-z]', s)
#     return str
#
# str1 = "The quick brown fox jumps over the lazy dog"
# res = ispangram(str1)
# print(res)
# print("YES" if res else "NO")

