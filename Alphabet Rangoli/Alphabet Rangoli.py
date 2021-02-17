"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art 
based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

Input Format
Only one line of input containing N, the size of the rangoli.

Output Format
Print the alphabet rangoli in the format explained above.

Sample Input
5

Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
def print_rangoli(N):
    for i in range (-(N-1),N):
        for j in range (-2*(N-1),2*(N-1)+1):
            if j%2==0 and (abs(j//2)+abs(i))< N:
                print (chr(abs(j//2)+abs(i)+ord('a')),end='')
            else:
                print('-',end='')
        print()
