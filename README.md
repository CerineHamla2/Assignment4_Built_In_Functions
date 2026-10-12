# Assignment4_Built_In_Functions
**#Purpose of the first part :**
The first part of the assignment asks the user to enter a positive integer for the size of a list and then enter the elements of the list. The program calculates the mean, median, and range of the list.

Mean: Calculates the average of all the elements and rounds the result to two decimal places.

Median: first Sort the list in ascending order. If the list has an odd number of elements, the median is the middle element. If it has an even number of elements, the median is the average of the two middle elements.

Range: Calculates the difference between the maximum and minimum values in the list.

The program also prints the original list and the sorted list. It uses try and except to handle invalid inputs.
**#example1 :** when running the program:
Enter a positive integer for the size of your list: 5    #in case the user enters a value that's either negative or a string an exception is raised then the programm will repeat until a valid value is entered

Enter element 1: 4     #adding elements to list1
Enter element 2: 8
Enter element 3: 2
Enter element 4: 10
Enter element 5: 6
The average of the elements in the list is: 6.0     #using built in function sum(), len(), and round
the sorted list is: [2, 4, 6, 8, 10]    #sorted the list using built in function sort()
the median element of the list is: 6
the range of the list is: 8          #using max(list1) - min(list1)

**#purpose of 2nd part:**
The second part of the assignment asks the user to enter a list of numbers separated by spaces. The program converts each number into an octal value and then translates it into a character to decode the message.

Input: The user enters a list of numbers separated by spaces.

Octal conversion: If a number is between 0 and 255, the program converts it into octal using Python's built-in oct() function.

Character conversion: The program removes the 0o prefix from the octal representation and uses int() with base 8 and chr() to obtain the corresponding character.

Invalid values: If a number is outside the range of 0 to 255, the program adds the negative of that number to the message.

Output: The program displays the translated message.

The program uses split() to separate the input into individual numbers and try and except to handle invalid input when converting the numbers to integers.
Input:

Enter a list of numbers separated by spaces: 81 73 79 76

Output:

The message is: Q I O L 
**#Sources: **
class slides, presentation slides, Python Documentation for Built-in Functions.
