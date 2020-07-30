'''
Find the last but one box of a list.
Example:
* (my-but-last '(a b c d))
(C D)
'''

#function returning length of list
def getListLength(temp_list):
    length = 0
    for item in temp_list:
        length += 1             #length counter incrementes on every element in the list
    
    return length


#initialized list with random elements
demo_list = [10,42,73,64,35,29]

#printing list
print("list is: ",demo_list)

#creating empty list
last_two_elements_list = list()

#finding last two elements
for element in demo_list:
    list_length = getListLength(last_two_elements_list)
    if list_length == 2:                                #if list length is equal to 2
        del last_two_elements_list[0]                   #removal of element at index 0, cause last two elements to be find.
    
    last_two_elements_list.append(element)              #appending every element to this list

print(last_two_elements_list) # printing last two elements as a list
