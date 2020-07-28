'''
5.   The results from the mayor's race have been reported by each precinct as follows:

          Candidate  Candidate  Candidate  Candidate
Precinct      A          B          C          D
   1         192        48         206        37
   2         147        90         312        21
   3         186        12         121        38
   4         114        21         408        39
   5         267        13         382        29

Write a program to do the following:

a. Read the raw vote totals from a data file that contains one row for each precinct.

b. Display the table with appropriate headings for the rows and columns.

c. Compute and display the total number of votes received by each candidate and
the percent of the total votes cast.

d. If any one candidate received over 50% of the votes, the program should print
 a message declaring that candidate the winner.

e. If no candidate received 50% of the votes, the program should print a message
declaring a run-off between the two candidates receiving the highest number of
votes; the two candidates should be identified by their letter names.

f. For testing, run the program with the above data, and also with another
   data file where Candidate C receives only 108 votes in precinct 4.
'''

candidate_a_votes = [192, 147, 186, 114, 267]
candidate_b_votes = [48, 90, 12, 21, 13]
candidate_c_votes = [26, 312, 121, 108, 382]
candidate_d_votes = [37, 21, 38, 39, 29]
first = []
total = []
for i in range(len(candidate_a_votes)):
    total.append(candidate_a_votes[i] + candidate_b_votes[i] +
                 candidate_c_votes[i] + candidate_d_votes[i])

print("Precint\tA\t\tB\t\tC\t\tD\t\tWin")
for i in range(len(candidate_a_votes)):
    str = ""
    percentage_list = []

    percentage_list.append(
        float(format((candidate_a_votes[i]/total[i])*100, '.2f')))
    str += f"{candidate_a_votes[i]}->{percentage_list[-1]}%\t"
    percentage_list.append(
        float(format((candidate_b_votes[i]/total[i])*100, '.2f')))
    str += f"{candidate_b_votes[i]}->{percentage_list[-1]}%\t"
    percentage_list.append(
        float(format((candidate_c_votes[i]/total[i])*100, '.2f')))
    str += f"{candidate_c_votes[i]}->{percentage_list[-1]}%\t"
    percentage_list.append(
        float(format((candidate_d_votes[i]/total[i])*100, '.2f')))
    str += f"{candidate_d_votes[i]}->{percentage_list[-1]}%\t"

    maximum_votes_gainer = "None"
    highest_percentage = max(percentage_list)
    if highest_percentage > 50.00:
        maximum_votes_gainer = percentage_list.index(highest_percentage)
        maximum_votes_gainer = chr(65 + maximum_votes_gainer)
    print(f"{i+1}\t{str}{maximum_votes_gainer}")
