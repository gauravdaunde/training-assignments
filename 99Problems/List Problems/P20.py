'''
Remove the K'th element from a list.
    Example:
    * (remove-at '(a b c d) 2)
    (A C D)
'''


def deleteItemWithLocation(temp_list,location):
	for index in range(len(demo_list)):
		if index == (location - 1):
			del temp_list[index]       #deletes element present at given index in list
			return

demo_list = input("Enter elements seperating by space: ").split(' ')


location = int(input("Enter location of element to delete: "))

#function call to delete element with location
deleteItemWithLocation(demo_list,location)

print(f"Element Deleted! {demo_list}")


