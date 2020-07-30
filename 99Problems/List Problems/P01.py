'''find the last box of a list.
Example:
* (my-last '(a b c d))
(D)
'''

#initialized list with random elements
demo_list = [10,42,73,64,35,29]

#printing list
print("list is: ",demo_list)


#initialized a variable
last_element = None

#finding last element of a list
for element in demo_list:
    last_element = element

#printing last element of list
print("Last box in the list is: ",last_element) 
