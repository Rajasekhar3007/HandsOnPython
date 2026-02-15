Cyber Activity Risk Analyzer

Python: Code2Xplore – 60 Days Challenge
Course Code: CSE205
Student Name: T. Raja Sekhar Reddy
Register Number: AP24110011528
Department: Computer Science and Engineering
University: SRM University–AP

Project Description

This project implements a Cyber Activity Risk Analyzer that processes login activity intensity scores and categorizes them into different risk levels. The system cleans invalid data, classifies valid scores into risk categories, applies a personalized security filter, and generates a final security report.

The behavior of the system depends on the last digit of the register number, which ensures that each student’s implementation works differently.

Objective

The objective of this project is to simulate how a university IT department might monitor login activity and identify suspicious behavior. The program:

Accepts activity scores

Ignores invalid data

Categorizes risk levels

Applies personalized filtering

Displays a summarized report

Risk Categorization Rules

For each activity score:

Score less than 0 → Ignored (Invalid Data)

0 to 30 → Low Risk

31 to 60 → Medium Risk

61 to 100 → High Risk

Greater than 100 → Critical Risk

Four separate lists are created:

low_risk

medium_risk

high_risk

critical_risk

The program also counts total valid entries and ignored entries.

Personalization Logic

Last digit of my Register Number = 8

Since 8 is an even number, I applied the following rule:

If D is EVEN → Remove all Low Risk scores after categorization.

I followed this rule strictly as mentioned in the problem statement. Because my register number ends with 8, the system removes all Low Risk entries after categorization.

This represents a stricter monitoring system that focuses only on Medium, High, and Critical risk activities. Low-level activities are ignored so that attention is given to more serious threats.

This personalization ensures my program behaves differently from students whose register numbers end with an odd digit.

Program Workflow

Accept register number

Extract the last digit (D)

Accept number of activity scores

Store scores in a list

Categorize scores using a for loop

Count valid and ignored entries

Apply personalized filtering

Display the final security report

Example Test Case

Input:
10, 45, 78, 120, -5, 30, 99, 150

Output (D = 8 EVEN):

Low Risk: []
Medium Risk: [45]
High Risk: [78, 99]
Critical Risk: [120, 150]
Total Valid Entries: 7
Ignored Entries: 1
Removed Due to Personalization: 2

Concepts Used

Lists

For loops

Conditional statements

Input handling

Basic logical categorization

No list comprehensions, dictionaries, filter(), or built-in functions like sum(), max(), or min() were used as per the instructions.

Learning Outcome

Through this challenge, I learned how data can be categorized and filtered in a structured way. I understood the importance of cleaning invalid data before processing it. This project improved my understanding of loops, conditional logic, and personalization rules in Python.

It also helped me understand how security monitoring systems prioritize higher-risk activities over low-risk ones.

Conclusion

The Cyber Activity Risk Analyzer successfully categorizes activity scores and applies personalized filtering based on the register number. The project demonstrates how basic Python concepts can be used to simulate a simple cybersecurity monitoring system.