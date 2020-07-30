'''
Duplicate the elements of a list.
    Example:
    * (dupli '(a b c c d))
    (A A B B C C C C D D)
'''

#taking input of list elements at a single time seperating by space and splitting each by split() method
demo_list = input("Enter elements seperated by space: ").split()
duplicates_list = list()

list_length = len(demo_list)
index = 0

while index < list_length:
	for _ in range(2):
		duplicates_list.append(demo_list[index])  #adding every item twice to new list 
	index += 1


print(f"old list {demo_list}")
print(f"duplicates list {duplicates_list}")
