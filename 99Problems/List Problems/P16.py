'''
Drop every N'th element from a list.
    Example:
    * (drop '(a b c d e f g h i k) 3)
    (A B D E G H K)
'''

def deleteItemWithLocation(temp_list,location):
	counter = 0
	result_list = list()

	length_of_list = len(temp_list)
	for index in range(length_of_list):
		counter += 1
		if counter != location:		#checking for every location number occurance
			result_list.append(temp_list[index])      #appending elements present at given index in result_list
		else:
			counter = 0  		#setting counter to zero and not appending current index element
	return result_list

demo_list = input("Enter elements seperating by space: ").split(' ')

location = int(input("Enter location of element to delete: "))

#function call to delete element with location
result_list = deleteItemWithLocation(demo_list,location)

print(f"Element Deleted! {result_list}")


