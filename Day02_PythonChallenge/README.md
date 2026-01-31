Smart ID & Credential Validator - DAY-2 Challenge
Overview

This project is part of the Python: Code2Xplore - 60 Days Challenge under the Department of Computer Science and Engineering, SRM University–AP.
The goal of this challenge is to develop a Smart ID & Credential Validator that ensures students’ registration details meet strict university rules before account approval.

The program takes the following inputs from the user:

Student ID

Email ID

Password

Referral Code

Registration Number

It validates each input according to the defined rules and prints:

APPROVED → if all credentials are valid

REJECTED → if any credential is invalid

Validation Rules
1. Student ID

Must be exactly 7 characters

Must start with "CSE"

The 4th character must be "-"

The last 3 characters must be digits

Example: CSE-245

2. Email ID

Must contain exactly one @

Must contain at least one .

@ cannot be the first or last character

Must end with .edu

Example: student@univ.edu

3. Password

Minimum length of 8 characters

The first character must be uppercase

Must contain at least one digit

Example: Aman1234

4. Referral Code

Must be exactly 6 characters

Must start with "REF"

Next two characters must be digits

The last character must be "@"

Example: REF45@

Approach / Logic Used

The solution uses string operations and conditional statements only, strictly following the challenge constraints.

The last digit of the Registration Number determines the validation order:

Even digit → Student ID is validated first, then Password

Odd digit → Password is validated first, then Student ID

Each input is validated independently:

Student ID → validated using string slicing and digit checks

Email ID → validated using @, ., and .edu ending checks

Password → validated for length, uppercase first character, and digit presence using direct index checks

Referral Code → validated using string slicing and digit checks

Boolean variables store validation results. All validations are combined using logical AND to determine approval.

This ensures clarity, correctness, and full adherence to constraints.

Algorithm / Steps

Start the program

Accept Student ID, Email ID, Password, Referral Code, and Registration Number

Extract the last digit of the Registration Number

Validate Student ID and Password based on even/odd rule

Validate Email ID

Validate Referral Code

If all validations pass → print APPROVED

Else → print REJECTED

End the program

Instructor Test Cases
Student ID	Email ID	Password	Referral	Output
CSE-245	student@univ.edu
	Aman1234	REF45@	APPROVED
CSE245	student@univ.edu
	aman1234	REF4A@	REJECTED
CSE-12A	@univ.edu	Amanabcd	REF99@	REJECTED
Constraints

Only strings and conditional statements are used

No loops

No regular expressions

No lists or dictionaries

No advanced libraries

Individual work with zero plagiarism

Author

Raja Sekhar Reddy
SRM University–AP
Department of Computer Science & Engineering