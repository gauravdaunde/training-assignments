'''
2. Write a program to search for the "saddle points" in a 5 by 5 array of 
integers. A saddle point is a cell whose value is greater than or equal to 
in its row, and less than or equal to any in its column. There may be more 
than one saddle point in the array. Print out the coordinates of any saddle 
points your program finds. Print out "No saddle points" if there are none.
'''


array = [[0, 1, 4, 4, 4],
         [2, 2, 3, 4, 3],
         [5, 4, 2, 4, 3],
         [3, 1, 5, 3, 5],
         [2, 2, 3, 1, 4]]


for i in range(5):
    for j in range(5):
        ''' checking for saddle point if data is greater than or equal to 
        its row(with first row as 1) and less than equal to its column'''
        if array[i][j] >= (i+1) and array[i][j] <= (j+1):
            print(f"value at {i+1},{j+1} is saddle point->{array[i][j]}")
