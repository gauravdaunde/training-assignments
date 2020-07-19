'''
Eliminate consecutive duplicates of list elements.
    If a list contains repeated elements they should be replaced with a 
	single copy of the element. The order of the elements should not be 
	changed.

Example:
* (compress '(a a a a b c c a a d e e e e))
(A B C A D E)
'''


#taking input of list elements at a single time seperating by space and splitting each by split() method
demo_list = input('enter elements seperated by space: ').split(' ')
new_list = list()   #creating new list

def removeConsecutiveDuplicates(demo_list):
	no_consecutive_dupliates_list = list(demo_list[0])        #appending first element to new_list

	for item in demo_list:               #iterating through all elements of demo_list
		if no_consecutive_dupliates_list[-1] != item:         #Checking if lastly added element to new_list is identical to to iterating item 
			no_consecutive_dupliates_list.append(item)        #if not same then appending to new_list. Here we're just eliminating the consecutive duplicates 

	return no_consecutive_dupliates_list


no_repeatative_dupliates_list = removeConsecutiveDuplicates(demo_list)


#printing both lists	
print(f'list before: {demo_list}')
print(f'list after removing repeatative duplicates: {no_repeatative_dupliates_list}')
