'''Flatten a nested list structure.
    Transform a list, possibly holding lists as elements into a `flat' 
	list by replacing each list with its elements (recursively).'''

#initialized list with random elements
demo_list = [1,33,422,[[23,5,4],[[25,[[33,54]]]],[24,[[43],34]],[101]],2,[40,100]]

#printing list
print("list is: ",demo_list)


def returnFlattenList(item,flatten_list):
	if isinstance(item,list):    #checking if item is a list
			for sub_item in item:       #if item is list iterate through its items
				returnFlattenList(sub_item,flatten_list)  #calling function again for each sub_item in item list
	else:                #if item is not a list
		flatten_list.append(item)   #appending item to list directly
	return flatten_list                #returm flatten_list



flatten_list = returnFlattenList(demo_list,[])  


print(f'List before {demo_list}')
print(f'list after {flatten_list}')
