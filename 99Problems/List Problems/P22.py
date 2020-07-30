'''
Create a list containing all integers within a given range.
    If first argument is smaller than second, produce a list in decreasing 
    order.
    Example:
    * (range 4 9)
    (4 5 6 7 8 9)
'''

#new list creation
demo_list = list()

#taking starting and ending point as inputs
start_point,end_point = input("Enter starting and ending point seperating by colon(:)-> ").split(':')

#type casting
start_point,end_point = int(start_point),int(end_point)


for element in range(start_point,end_point+1):  #loop from starting to ending point
	demo_list.append(element)             #appending every element in starting to ending point.
	

print(f"Created list is: {demo_list}")
