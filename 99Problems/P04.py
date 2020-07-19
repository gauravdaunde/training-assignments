#Find the number of elements of a list.


#returning length of list
def getLengthofList(list):
	length_of_list = 0
	for item in demo_list:    #iterating through all elements and incrementing size counter.
		length_of_list += 1

	return length_of_list

#initialized list with random elements
demo_list = [10,42,73,64,35,29]


#printing list
print("list is: ",demo_list)

#function called
size_of_list = getLengthofList(demo_list)


#printing founded size of list
print("Size of the list is",size_of_list)
