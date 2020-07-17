#Reverse a list.


demo_list = [11,22,33,44,55,66,77,88,99]

new_list = list()       #Initialising new list object

length_of_list = 0      #counter to find lengh of list

for item in demo_list:    #iterating through all elements and incrementing length_of_list counter.
	length_of_list += 1

current_index = length_of_list - 1   #list index start from 0 ,so here counted length is decremented by 1.

while current_index >= 0:
	new_list.append(demo_list[current_index])  #appending items to list from last index
	current_index -= 1    #reverse iterating from lenth of list (decremented by 1) to index 0.
	
print(f"Old list is: {demo_list}")
print(f"New reversed list is: {new_list}")
