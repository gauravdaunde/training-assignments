'''
Replicate the elements of a list a given number of times.
    Example:
    * (repli '(a b c) 3)
    (A A A B B B C C C)
'''

#taking input of list elements at a single time seperating by space and splitting each by split() method
demo_list = input("Enter elements seperating by space: ").split(' ')

replication_constant = int(input("Enter no to replicate: "))
replicated_list = list()

for item in demo_list:
	for _ in range(replication_constant):
		replicated_list.append(item)            #adding items to new list at replication_constant times

print(f"old list: {demo_list}")
print(f"new list: {replicated_list}")
