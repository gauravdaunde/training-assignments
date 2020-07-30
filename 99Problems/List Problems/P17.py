'''
Split a list into two parts; the length of the first part is given.
    Do not use any predefined predicates.

    Example:
    * (split '(a b c d e f g h i k) 3)
    ( (A B C) (D E F G H I K))
'''

#returning list splitted in two parts
def getSplittedList(input_list,first_part_length):
    #creating lists
    splitted_list = list()
    temp_list = list()

    length_of_list = len(input_list)

    for index in range(length_of_list):
        temp_list.append(input_list[index])   #appending every item to temp_list
        if index == (first_part_length - 1):  #checking for first part limit is reached or not
            splitted_list.append(temp_list[:])  #first parrt is been appended to splitted list
            temp_list.clear()                   # clearing temp_list to store next part
    splitted_list.append(temp_list[:])          #appending remaining next part to splited_list

    return splitted_list        #returning splitted list

demo_list = input("Enter elements seperating by space: ").split(' ')
length_of_first_part = int(input("Enter the no of elements to be in first part: "))



splitted_list = getSplittedList(demo_list,length_of_first_part)
print(f"old list: {demo_list}")
print(f"new list: {splitted_list}")


