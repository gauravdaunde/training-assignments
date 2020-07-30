'''
Rotate a list N places to the left.
    Examples:
    * (rotate '(a b c d e f g h) 3)
    (D E F G H A B C)

    * (rotate '(a b c d e f g h) -2)
    (G H A B C D E F)

    Hint: Use the predefined functions length and append, as well as 
    the result of problem P17.
'''


demo_list = list(map(str,input("Enter elements seperating by space: ").split(' ')))
starting_location = int(input("Enter starting location: "))

rotated_list = list()

if starting_location < 0:                   #if startiing_location is negative position
    starting_location += len(demo_list)+1   #then converting it to its positive equivant list index position
for i in range(starting_location-1,len(demo_list)):  #we know element3 in list is at index 2, so decrementing starting_location by 1, and running loop from it to length of list
	rotated_list.append(demo_list[i])           #appending elements to new lists 

for i in range(0,starting_location-1):  #also need to add remaining elements present in list before starting_location, so adding here
	rotated_list.append(demo_list[i])

print(f"old list: {demo_list}")
print(f"rotated list: {rotated_list}")


