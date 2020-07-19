#Find the K'th element of a list.

#function returning length of list
def getListLength(temp_list):
    length = 0
    for item in temp_list:
        length += 1             #length counter incrementes on every element in the list
    
    return length

#getting element with location
def getElementWithLocation(elements_list,location):
    length = getListLength(elements_list)               #finding length of list
    founded_element = None                              #created a variable

    for index in range(length):
        if index == (location - 1):
            founded_element = elements_list[index]              #finding element with location
            print("element at lcotion",location,"is",founded_element)   #printing founded element
            return
    print("List is not having location",location)         #printing if list doesnt have that location


#initialized list with random elements
demo_list = [10,42,73,64,35,29]


#printing list
print("list is: ",demo_list)

#taking input of location
location = int(input("Enter location: "))

#calling function to found element with location
getElementWithLocation(demo_list,location)


