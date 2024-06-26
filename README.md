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
												  
04.Problem: Clever Lily	
Lily is now N years old. For every birthday she gets a present.
• For odd birthdays (1, 3, 5...n) he gets toys.
• For even birthdays (2, 4, 6...n) he receives money.
For the second birthday, he receives BGN 10.00, and the amount increases by BGN 10.00 for each subsequent even birthday (2 -> 10, 4 -> 20, 6 -> 30...etc.). Over the years, Lily has secretly saved the money. Lily's brother, in the years that she receives money, takes BGN 1.00 from them. Lily sold the toys received over the years, each for P leva and added the amount to the money saved. She wanted to use the money to buy a washing machine for BGN X. Write a program to calculate how much money she has collected and whether she has enough to buy a washing machine.
input
The program reads 3 numbers entered by the user on separate lines:
• Lily's age - an integer in the range [1...77]
• The price of the washing machine - a number in the interval [1.00...10 000.00]
• Unit price of a toy - an integer in the interval [0...40]
output
To print one line to the console:
• If Lily's money is enough:
o "Yes! {N}" - where N is the remaining money after the purchase
• If the money is not enough:
o "No! {M}" - where M is the amount missing
The numbers N and M must be formatted to the second decimal place.

Sample input and output
input	output
10      Yes! 5.00
170.00
6

input	output
21      No! 997.98
1570.98
3	

05. Problem: Salary
A company boss notices that more and more employees are spending time on distracting websites.
To prevent this, it implements surprise checks on its employees' open browser tabs.
According to the open site in taba, the following fines are imposed:
• "Facebook" -> BGN 150
• "Instagram" -> BGN 100
• "Reddit" -> BGN 50
Two lines are read from the console:
• Number of open tabs in the browser n - an integer in the interval [1...10]
• Salary - number in the interval [500...1500]
Then n - number of times website name - text is read
output
• If during the check the salary becomes less than or equal to BGN 0, the console displays
"You have lost your salary." and the program ends.
• Otherwise, after checking the console, the balance of the salary is printed (to be printed as an integer).

Sample input and output
input	     output
10           You have lost 
750          your salary.
Facebook
Dev.bg
Instagram
Facebook
Reddit
Facebook
Facebook

input	           output
3                  500
500
Github.com
Stackoverflow.com
softuni.bg	

input	output
3       350
500
Facebook
Stackoverflow.com
softuni.bg	

06.Problem: Oscars
You are invited by the academy to write software to calculate the points for an actor/actress. The academy will give you initial points for the actor. Each rater will then give their rating. The points the actor receives are formed by: the length of the evaluator's name multiplied by the points he gives divided by two.
If the score at any point exceeds 1250.5 the program should abort and print that the given actor has received a nomination.
input
• Actor name - text
• Academy points - a real number in the interval [2.0... 450.5]
• Number of evaluators n - an integer in the interval [1… 20]
On the next n-th number of lines:
o Evaluator's name - text
o Points from the evaluator - a real number in the interval [1.0... 50.0]
output
To print one line to the console:
• If points are above 1250.5:
"Congratulations, {actor's name} got a nominee for leading role with {points}!"
• If the points are not enough:
"Sorry, {actor name} you need {points needed} more!"
The result should be formatted to the first digit after the decimal point!

Sample input and output
input	        output
Zahari Baharov  Sorry, Zahari Baharov 
205             you need 247.5 more!
4
Johnny Depp
45
Will Smith
29
Jet Lee
10
Matthew Mcconaughey
39	

input              output
Sandra Bullock     Congratulations, Sandra Bullock got a 
340                nominee for leading role with 1268.5!
5
Robert De Niro
50
Julia Roberts
40.5
Daniel Day-Lewis
39.4
Nicolas Cage
29.9
Stoyanka Mutafova
33	

07.Problem: Trekking Mania
Climbers from all over Bulgaria gather in groups and mark the next peaks to climb. Depending on the size of the group, climbers will climb different peaks.
• Group up to 5 people - climb Musala
• Group of 6 to 12 people - climb Mont Blanc
• A group of 13 to 25 people - climb Kilimanjaro
• Group of 26 to 40 people - climb K2
• Group of 41 or more people - climb Everest
To write a program that calculates the percentage of climbers who climb each peak.
input
A series of numbers are read from the console, each on a separate line:
• On the first line - the number of groups of climbers - an integer in the interval [1...1000]
• For each group on a separate line - the number of people in the group - an integer in the interval [1...1000]
output
Print to the console 5 lines, each containing a percentage between 0.00% and 100.00% to the second decimal place.
• First row - the percentage of Musala climbers
• Second row – the percentage of Mont Blanc climbers
• Third row – the percentage of Kilimanjaro climbers
• Fourth row – the percentage of K2 climbers
• Fifth row – the percentage of Everest climbers

Sample input and output
input	output
10      1.84%
10      6.75%
5       5.21%
1       31.60%
100     54.60%
12
26
17
37
40
78	

input	output
5       0.00%
25      1.70%
41      7.08%
31      8.78%
250     82.44%
6

08.Problem: Tennis ranklist
Grigor Dimitrov is a tennis player whose next goal is to climb the world rankings in men's tennis.
During the year, Grisho participated in a certain number of tournaments, and for each tournament he received points that depend on the position in which he finished in the tournament. There are three options for completing a tournament:
 W - if winner gets 2000 points
 F - if he is a finalist he gets 1200 points
 SF - if semi-finalist gets 720 points
Write a program that calculates how many points Grigor will have after playing all the tournaments, knowing how many points he started the season with. Also calculate how many points he averaged from all the tournaments played and what percentage of the tournaments he won.
input
Two lines are first read from the console:
• Number of tournaments in which he participated - an integer in the interval [1…20]
• Initial number of points in the ranking list - an integer in the interval [1...4000]
A separate line was read for each tournament:
• Tournament Stage Reached - Text - "W", "F" or "SF"
output
Three lines are printed in the following format:
• "Final points: {number of points after the tournaments played}"
• "Average points: {average points earned per tournament}"
• "{tournament won percentage}%"
Midpoints should be rounded down to the nearest whole number, and percentages should be formatted to the second digit after the decimal point.

Sample input and output
input	output
5       Final points: 8040
1400    Average points: 1328
F       40.00%
SF
W
W
SF	

input	output
4       Final points: 6190
750     Average points: 1360
SF      50.00%
W
SF
W

input	output
7       Final points: 11040
1200    Average points: 1405
SF      42.86%
F
W
F
W
SF
W	






















	

	


	

