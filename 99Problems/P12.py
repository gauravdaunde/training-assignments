'''
Decode a run-length encoded list.
    Given a run-length code list generated as specified in problem P11. 
	Construct its uncompressed version.
'''

#assigning a random run-length encoded list to encoded_list
encoded_list = [[3, 'a'],'f', [2, 'b'], [3, 'c'], [2, 'd'], [3, 'c']]
decoded_list = list()   	#creating new list

for item in encoded_list:					#iterating through all list elements
	if isinstance(item,list):				#checking if element is list or not. If it is list means elements should be repeated.
		for i in range(item[0]):			#first element of sublist contains occurance, so running loop for that iterations.
			decoded_list.append(item[1])	#second element in sublist contains the actual value that is being repeated, so appending it to decoded list
	else:									#if element of encoded_list is not a list, then it is value itself
		decoded_list.append(item)			#diectly appending to decoded_list

#printing given encoded_list and list after decoding it
print(f"encoded list: {encoded_list}")
print(f"decoded new list: {decoded_list}")
