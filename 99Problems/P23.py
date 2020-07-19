'''
Extract a given number of randomly selected elements from a list.
    The selected items shall be returned in a list.
    Example:
    * (rnd-select '(a b c d e f g h) 3)
    (E D A)
'''


#importing randint function from random module
from random import randint


demo_list = [13,42,34,50,103,74,86,87,18,44,56,88]
randomly_selected_list = list()

print(demo_list)

count_to_select = int(input("Enter how many elements to be selected randomly: "))

length_of_list = len(demo_list)

for i in range(count_to_select):
    random_number = randint(0,length_of_list)    #generating random number between 0 to length of list(excludes last number)
    randomly_selected_list.append(demo_list[random_number])    #appeding element present at random number to list.

print(f"randomly selected elements list is: {randomly_selected_list}")
