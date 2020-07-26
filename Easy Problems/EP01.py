'''

                  +-------------------------+
                  ¦ 34 ¦ 21 ¦ 32 ¦ 41 ¦ 25  ¦
                  +----+----+----+----+-----¦
                  ¦ 14 ¦ 42 ¦ 43 ¦ 14 ¦ 31  ¦
                  +----+----+----+----+-----¦
                  ¦ 54 ¦ 45 ¦ 52 ¦ 42 ¦ 23  ¦
                  +----+----+----+----+-----¦
                  ¦ 33 ¦ 15 ¦ 51 ¦ 31 ¦ 35  ¦
                  +----+----+----+----+-----¦
                  ¦ 21 ¦ 52 ¦ 33 ¦ 13 ¦ 23  ¦
                  +-------------------------+



1. Do you like treasure hunts? In this problem you are to write a program to explore the above array for a treasure. The values in the array are clues. Each cell contains an integer between 11 and 55; for each value the ten's digit represents the row number and the unit's digit represents the column number of the cell containing the next clue. Starting in the upper left corner (at 1,1), use the clues to guide your search of the array. (The first three clues are 11, 34, 42). The treasure is a cell whose value is the same as its coordinates. Your program must first read in the treasure map data into a 5 by 5 array. Your program should output the cells it visits during its search, and a message indicating where you found the treasure.
'''

clues_array = [[34, 21, 32, 41, 25],
               [14, 42, 43, 14, 31],
               [54, 45, 52, 42, 23],
               [33, 15, 51, 31, 35],
               [21, 52, 33, 13, 23]]


# visiting locations by checking data at location
def visit_locations(row, col):
    # indexing starts from 0 so, substracting 1 from col and row
    clue = str(clues_array[row-1][col-1])

    # checking if location contains locatin itself
    if row == int(clue[0]) and col == int(clue[1]):
        print(f"Treasure found at {row},{col}")  # then treasure s found
        return

    # else print current visited location and go for visiting location present given in its data
    print(f"{row},{col} visited.")
    visit_locations(int(clue[0]), int(clue[1]))


visit_locations(1, 1)
