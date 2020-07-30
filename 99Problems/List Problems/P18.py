'''
Extract a slice from a list.
    Given two indices, I and K, the slice is the list containing the 
    elements between the I'th and K'th element of the original list 
    (both limits included). Start counting the elements with 1.

    Example:
    * (slice '(a b c d e f g h i k) 3 7)
    (C D E F G)
'''

def getSliceFromList(demo_list,starting_location,ending_location):
    sliced_list = list()  #output list creation

    for index in range((starting_location-1),ending_location):  #iterating between given starting and ending point
        sliced_list.append(demo_list[index])                #adding every element to sliced_list

    return sliced_list

demo_list = input("Enter elements seperating by space: ").split(' ')
starting_location,ending_location = input("Enter range seperated by space: ").split(' ')  #taking location of slicing part

#typecasting from str to int
starting_location = int(starting_location)
ending_location = int(ending_location)

#calling function
sliced_list = getSliceFromList(demo_list,starting_location,ending_location)


print(f"old list: {demo_list}")
print(f"sliced list from original is: {sliced_list}")


