'''
Run-length encoding of a list (direct solution).
    Implement the so-called run-length encoding data compression method 
	directly. I.e. don't explicitly create the sublists containing the 
	duplicates, as in problem P09, but only count them. As in problem P11, 
	simplify the result list by replacing the singleton lists (1 X) by X.

	Example:
* (encode-direct '(a a a a b c c a a d e e e e))
((4 A) B (2 C) (2 A) D (4 E))
'''


#taking input of list elements at a single time seperating by space and splitting each by split() method
demo_list = input("Enter elememts sep by space: ").split(' ')

#creating new lists
encoded_list = list()

previous_item = demo_list[0]         #assigning first element of demo_list to previous_item
previous_item_count = 0

for current_item in demo_list:               #iterating through all elements of demo_list
	if current_item == previous_item:        #checking if previously added element is same as current element of list, for checking repetative elements 
		previous_item_count += 1
	else: 									 #if not repetative element
		if previous_item_count == 1:		 #if element not repeating, means have only one occurance thndirectly
			encoded_list.append(previous_item)
		else:
			encoded_list.append([previous_item_count,previous_item])		 #appending previously created sublist(temp_list) copy to new_list 
		
		previous_item_count = 1
		previous_item = current_item         #assigning current_item to previous_item
else:		#for last item
	if previous_item_count == 1:		 #if element not repeating, means have only one occurance thndirectly
		encoded_list.append(previous_item)
	else:
		encoded_list.append([previous_item_count,previous_item])		 #appending previously created sublist(temp_list) copy to new_list 
		

#pritning demo_list and its encoded list
print(f"old list: {demo_list}")
print(f"encoded list: {encoded_list}")	

