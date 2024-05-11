01. Problem: Numbers ending in 7
Write a program that prints the numbers in the range 1 to 1000 that end in 7.
input     	    output
(there is no)	  7
17
27
…
997

02.Problem: Half sum element
Write a program that reads n-th number of integers entered by the user and checks if there is a number among them that is equal to the sum of all the others.
• If there is such an element, print "Yes" and on a new line "Sum = " + its value
• If there is no such element, print "No" and on a new line "Diff = " + the difference between the largest element and the sum of the others (by absolute value)

Sample input and output
input	       output	     commentary
7            Yes         3 + 4 + 1 + 2 + 1 + 1 = 12
3            Sum = 12
4
1
1
2
12
1	

input	       output	     commentary
4            Yes         1 + 2 + 3 = 12
6            Sum = 6
1
2
3	

input	       output	     commentary
3            No          |10 - (1 + 1)| = 8
1            Diff = 8
1
10	

input	       output	     commentary
3            No          |5 - (5 + 1)| = 1 
5            Diff = 1
5
1

input	       output	     commentary
3            No
1            Diff = 1
1
1	


	

	


	

