'''
Generate a random permutation of the elements of a list.
    Example:
    * (rnd-permu '(a b c d e f))
    (B A D C E F)

'''

#importingrandint function from random module
from random import randint


input_list = input("Enter list seperated by space(max 10): ").split(' ')

print(f"given list is: {input_list}")

#creating new lists
randomly_permuted_list = list()
visited_indexes_list = list()


while len(randomly_permuted_list) < len(input_list):	#checking all elements are appended from input_list to randomly_permuted_list
	#generating random index
	random_index = randint(0,len(input_list)-1)
	
	#checking randomly generated index is already visited or not
	if random_index in visited_indexes_list:
		continue			#if visited already then terminating current iteration
	
	visited_indexes_list.append(random_index)		#if not visited then, is need to mark as visited
	selected_element = input_list[random_index]		#getting element present at generated index 
	randomly_permuted_list.append(selected_element)	#and apeending to permuted list
	

print(f"Newly permuted list is: {randomly_permuted_list}")
