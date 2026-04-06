Program Overview
The program defines a class MARKSHEET that collects and displays a student’s academic details — including name, roll number, and marks in four subjects.

Class Details
Constructor (__init__)
Initializes:
name → Student’s name
roll_no → Student’s roll number
__marks → A private dictionary to store subject–marks pairs
add_mark() Method
Prompts the user 4 times to enter:
Subject name
Marks obtained (integer)
Stores these key–value pairs in the private dictionary __marks.
show() Method
Displays:
Student’s name and roll number
Each subject with its marks
Calculates and prints:
Total marks
Average marks
Main Program Flow
Prompts user for:
Name
Roll number
Creates an object of MARKSHEET.
Calls add_mark() to input marks.
Calls show() to display the complete marksheet.
Example Output


Enter name: Alice
Enter roll: 101
Enter subject: Math
Enter marks: 85
Enter subject: English
Enter marks: 90
Enter subject: Science
Enter marks: 80
Enter subject: History
Enter marks: 75
Name: Alice
Roll No: 101
Marks:
Math : 85
English : 90
Science : 80
History : 75
Total: 330
Average: 82.5
In short:
The program creates a basic marksheet system using object-oriented programming (OOP) — demonstrating encapsulation, user input handling, and simple data processing (total and average calculation).




