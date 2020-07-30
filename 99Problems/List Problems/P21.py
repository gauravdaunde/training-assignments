'''
Insert an element at a given position into a list.
    Example:
    * (insert-at 'alfa '(a b c d) 2)
    (A ALFA B C D)
'''


def insertElementAtLocation(temp_list,location,element):
	length_of_list = len(temp_list)		#length of list
	result_list = list()

	for index in range(length_of_list):
		if index == (location - 1):   #checking for location
			result_list.append(element)   	# we want element to be added on location , so appending element to result_list
		result_list.append(temp_list[index])
	
	return result_list
		
	



#taking input
demo_list = input("Enter elements seperating by space: ").split(' ')
print(demo_list)

location = int(input("Enter location of element insertion: "))
element = input("Enter element to ve added: ")

result_list = insertElementAtLocation(demo_list,location,element)

print(f"Previous List: {demo_list}")
print(f"List after insertion: {result_list}")


