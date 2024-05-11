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

03.Problem: Histogram
Given n integers in the interval [1…1000]. Of these, some percentage p1 are below 200, another percentage p2 are from 200 to 399, another percentage p3 are from 400 to 599,
another percentage p4 are from 600 to 799 and the remaining p5 percentage are from 800 and up. To write a program that calculates and prints the percentages p1, p2, p3, p4 and p5.
Example: we have n = 20 numbers: 53, 7, 56, 180, 450, 920, 12, 7, 150, 250, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65. We get the following distribution and visualization:

Range           Numbers in range                                           Number of numbers                     Percent
< 200	        53, 7, 56, 180, 12, 7, 150, 2, 199, 46, 128, 65	           12	                                 p1 = 12 / 20 * 100 = 60.00%
200 … 399	250, 200	                                           2	                                 p2 = 2 / 20 * 100 = 10.00%
400 … 599	450	                                                   1	                                 p3 = 1 / 20 * 100 = 5.00%
600 … 799	680, 600, 799	                                           3	                                 p4 = 3 / 20 * 100 = 15.00%
≥ 800	        920, 800	                                           2	                                 p5 = 2 / 20 * 100 = 10.00%

input
The first line of the input contains the integer n (1 ≤ n ≤ 1000) - number of numbers. On the next n lines there is one whole number in the interval [1...1000] 
- the numbers on which the histogram should be calculated.
output
Print the histogram to the console - 5 lines, each containing a number between 0% and 100%, to two decimal places, eg 25.00%, 66.67%, 57.14%.

Sample input and output

input	output		input	output		input	output			input	output			input	output	
3       66.67%          4       75.00%          7       14.29%                  9       33.33%                  14      57.14%
1       0.00%           53       0.00%          800     28.57%                  367     33.33%                  53      14.29%
2       0.00%           7        0.00%          801     14.29%                  99      11.11%                  7       7.14%
999     0.00%           56       0.00%          250     14.29%                  200     11.11%                  56      14.29%
	33.33%          999     25.00%          199     28.57%                  799     11.11%                  180     7.14%
                                                599                             999                             450
                                                799                             333                             920
                                                                                555                             12
                                                                                111                             7
                                                                                9                               150
                                                                                                                250
														680
	                                                                                                        2
													        600
		                                                                                                200
	

	


	

