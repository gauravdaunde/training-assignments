'''
Run-length encoding of a list.
    Use the result of problem P09 to implement the so-called run-length 
	encoding data compression method. Consecutive duplicates of elements 
	are encoded as lists (N E) where N is the number of duplicates of the 
	element E.
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
	temp_list.clear()			 		#removing all elements from temp_list
	temp_list.append(len(item))  		#new_list contains sublist of repetative elements, so finding size of sublist and appending to temp_list.
	temp_list.append(item[0])    		#also appending element with its count present in sublist.
	encoded_list.append(temp_list[:])	#appending temp_list to encoded_list


#printing demo_list and encoded_list
print(f"old list: {demo_list}")
print(f"result list: {encoded_list}")	
