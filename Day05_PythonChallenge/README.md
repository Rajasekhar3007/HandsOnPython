Emergency Resource Dispatch Analyzer
Course Details

Course: CSE205 – Hands on Python
University: SRM University–AP
Challenge: Code2Xplore – 60 Days Challenge (Day-5)
Faculty: Dr. Yasir Afaq

Student Details

Name: Raja Sekhar Reddy Thippireddy
Register Number: AP24110011528

Problem Description

During a disaster drill, different zones report the number of emergency resources required. However, these reports may contain invalid values, zero demand, low demand, moderate demand, or high demand.

The objective of this program is to analyze the list of resource requests, classify them into categories, apply a personalized filtering rule, and generate a final dispatch report.

Classification Rules

Each request is categorized as follows:

Less than 0 → Invalid Request

0 → No Demand

1 to 20 → Low Demand

21 to 50 → Moderate Demand

Greater than 50 → High Demand

The program stores each category in separate lists and counts the total valid requests.

Personalization Applied

Personalization is based on the last digit of the birth year.

Let:
Last Digit = last digit of birth year
Choice = Last Digit % 3

Rules Applied:

If Choice = 0 → Remove all Low Demand requests

If Choice = 1 → Remove all High Demand requests

If Choice = 2 → Keep only Moderate Demand requests

This ensures that the output differs for each student depending on their birth year.

Example

If Birth Year = 2004

Last Digit = 4
Choice = 4 % 3 = 1

Applied Rule → Remove High Demand requests

Program Features

Uses list data structure

Uses for loops for processing

Uses conditional statements for classification

Counts total valid requests

Counts removed requests after personalization

Generates a structured final dispatch report

Learning Outcome

Through this challenge, I improved my understanding of loops, conditional statements, and list manipulation in Python. I learned how to classify data logically and apply personalization using mathematical operations. This exercise helped me strengthen my problem-solving and logical thinking skills.