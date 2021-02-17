"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print 
the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format
The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second 
line contains their grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, 
order their names alphabetically and print each one on a new line.

Sample Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:
Berry
Harry
"""
N=int(input())
python_students=[]
scores_list=[]
final_list=[]
if(N>=2 and N<=5):
    for i in range(N):
        names=input()
        scores=float(input())
        python_students.append([names,scores])
        scores_list.append(scores)
    scores_list=sorted(set(scores_list))
    for i in range(N):
        if(python_students[i][1]==scores_list[1]):
            final_list.append(python_students[i][0])
    for i in sorted(final_list):
        print(i)