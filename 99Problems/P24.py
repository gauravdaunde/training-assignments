'''
Lotto: Draw N different random numbers from the set 1..M.
    The selected numbers shall be returned in a list.
    Example:
    * (lotto-select 6 49)
    (23 1 17 33 21 37)

'''
#importingrandint function from random module
from random import randint

numbers_to_draw = int(input("Enter how many random numbers you want to draw from set: "))

highest_number_to_select = int(input("Enter highest number of set(last element) :"))

drawn_elements_list = list()

#running loop numbers_to_draw times
for _ in range(numbers_to_draw):
    #generating random number between 1 to highest num
    randomly_generated_number = randint(1,highest_number_to_select+1) #randint excludes ending_point that is its second argument, here we want to it to be included, so incrementing 2nd argument
    drawn_elements_list.append(randomly_generated_number)   #appending element to list


#pritning dreawn numbers list result
print(f"{numbers_to_draw} numbers are drawn, those are: {drawn_elements_list}")
