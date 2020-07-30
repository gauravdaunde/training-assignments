'''
Modified run-length encoding.
    Modify the result of problem P10 in such a way that if an element 
	has no duplicates it is simply copied into the result list. Only 
	elements with duplicates are transferred as (N E) lists.
	Example:
* (encode-modified '(a a a a b c c a a d e e e e))
((4 A) B (2 C) (2 A) D (4 E))
'''

'''
Modified run-length encoding.
    Modify the result of problem P10 in such a way that if an element 
	has no duplicates it is simply copied into the result list. Only 
	elements with duplicates are transferred as (N E) lists.
	Example:
* (encode-modified '(a a a a b c c a a d e e e e))
((4 A) B (2 C) (2 A) D (4 E))
'''



#taking input of list elements at a single time seperating by space and splitting each by split() method
demo_list = input("Enter elememts sep by space: ").split(' ')

#creating new lists
runLength_converted_list = list()
encoded_list = list()

previous_item = demo_list[0]         #assigning first element of demo_list to previous_item
temp_list = list()				     #creating new list as temp_list

for current_item in demo_list:               #iterating through all elements of demo_list
	if current_item == previous_item:        #checking if previously added element is same as current element of list, for checking repetative elements 
		temp_list.append(current_item)		 #appending current element to temp_list. for creation of sublist 
	else: 									 #if not repetative element
		runLength_converted_list.append(temp_list[:])		 #appending previously created sublist(temp_list) copy to new_list 
		temp_list.clear()					 #clearing temp_list to create new sublist
		temp_list.append(current_item)		 #appending current_item to temp_list		
		previous_item = current_item         #assigning current_item to previous_item
else:
	runLength_converted_list.append(temp_list[:])            #appending temp_list copy to new_list
	
	
	
for item in runLength_converted_list:            		#iterating through all elements of demo_list
	count_sublist_items = len(item)  		#new_list contains sublist of repetative elements, so finding size of sublist and appending to temp_list.
	if count_sublist_items == 1:
		encoded_list.append(item[0])
	else:
		encoded_list.append([count_sublist_items,item[0]])	#appending temp_list to encoded_list


#pritning demo_list and its encoded list
print(f"old list: {demo_list}")
print(f"encoded list: {encoded_list}")	
