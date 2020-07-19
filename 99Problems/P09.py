'''
Pack consecutive duplicates of list elements into sublists.
    If a list contains repeated elements they should be placed in separate
	 sublists.
	 Example:
* (pack '(a a a a b c c a a d e e e e))
((A A A A) (B) (C C) (A A) (D) (E E E E))
'''

#taking input of list elements at a single time seperating by space and splitting each by split() method
demo_list = input('enter elements seperated by space: ').split(' ')

new_list = list()     #creating new list as new_list

previous_item = demo_list[0]         #assigning first element of demo_list to previous_item
temp_list = list()				     #creating new list as temp_list

for current_item in demo_list:               #iterating through all elements of demo_list
	if current_item == previous_item:        #checking if previously added element is same as current element of list, for checking repetative elements 
		temp_list.append(current_item)		 #appending current element to temp_list. for creation of sublist 
	else: 									 #if not repetative element
		new_list.append(temp_list[:])		 #appending previously created sublist(temp_list) copy to new_list 
		temp_list.clear()					 #clearing temp_list to create new sublist
		temp_list.append(current_item)		 #appending current_item to temp_list		
		previous_item = current_item         #assigning current_item to previous_item
else:
	new_list.append(temp_list[:])            #appending temp_list copy to new_list
	
	
	
#printing new_list and demo_list
print(f"old list: {demo_list}")
print(f"newly created list: {new_list}")
