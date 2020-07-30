#Find out whether a list is a palindrome.


#returning length of list
def getLengthofList(list):
	length_of_list = 0
	for item in demo_list:    #iterating through all elements and incrementing size counter.
		length_of_list += 1

	return length_of_list

#returs reversed string
def getReversedList(temp_list):
	length_of_list = getLengthofList(temp_list)
	reversed_list = list()       #Initialising new list object

	current_index = length_of_list - 1   #list index start from 0 ,so here list length is decremented by 1 to get index of last element.

	while current_index >= 0:
		reversed_list.append(demo_list[current_index])  #appending items to list from last index
		current_index -= 1    #reverse iterating from lenth of list (decremented by 1) to index 0.

	return reversed_list



#initialized list with random elements
demo_list = [10,42,73,42,10]


#printing list
print("list is: ",demo_list)


#finding reversed list
reversed_list = getReversedList(demo_list)

#checking reversed list and original list is same or not
if demo_list == reversed_list:	  #if same then list is palindrome
	print('Entered list is palindrome')
else:
	print('entered list is not palindrome')
