#Reverse a list.




#returning length of list
def getLengthofList(list):
	length_of_list = 0
	for item in demo_list:    #iterating through all elements and incrementing size counter.
		length_of_list += 1

	return length_of_list

#returs reversed string
def getReverseList(temp_list):
	length_of_list = getLengthofList(temp_list)
	reversed_list = list()       #Initialising new list object

	current_index = length_of_list - 1   #list index start from 0 ,so here list length is decremented by 1 to get index of last element.

	while current_index >= 0:
		reversed_list.append(demo_list[current_index])  #appending items to list from last index
		current_index -= 1    #reverse iterating from lenth of list (decremented by 1) to index 0.

	return reversed_list


#initialized list with random elements
demo_list = [10,42,73,64,35,29]


#printing list
print("list is: ",demo_list)

#getReversedList function called
reversed_list = getReverseList(demo_list)

#printing reversed list
print(f"New reversed list is: {reversed_list}")
