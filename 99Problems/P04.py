#Find the number of elements of a list.

demo_list = [11,22,33,44,55,66,77,88,99]
size_of_list = 0

for item in demo_list:    #iterating through all elements and incrementing size counter.
	size_of_list += 1
	
print("List is:",demo_list)
print("Size of the list is",size_of_list)
