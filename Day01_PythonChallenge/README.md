# 🐍 Hands-on Python – Code2Xplore 60 Days Challenge  
## Day-01: User Profile Validation System

---

## 📌 Course Details
- **Course Code:** CSE205  
- **Course Name:** Hands-on Python  
- **Department:** Computer Science and Engineering  
- **University:** SRM University–AP  
- **Concerned Faculty:** Dr. Yasir Afaq  

---

## 🧠 Challenge Understanding
The Day-01 challenge focuses on creating a simple User Profile Validation System using Python.  
The task is to collect user details such as Full Name, Email ID, Mobile Number, and Age and then verify whether these details follow the given validation rules before accepting them.  
The challenge emphasizes the use of basic Python concepts like data types, string manipulation, and conditional statements, without using loops, regular expressions, or advanced libraries.

---

## 📝 Problem Statement
Write a Python program that takes the following inputs from the user:
- Full Name  
- Email ID  
- Mobile Number  
- Age  

Based on the validation rules, the program should determine whether the user profile is **VALID** or **INVALID**.

---

## ✅ Validation Rules Implemented

### Full Name
- Must contain at least two words  
- Must not start or end with a space  

### Email ID
- Must contain `@` and `.`  
- `@` must not be the first character  

### Mobile Number
- Must be exactly 10 digits  
- Must contain only digits  
- Must not start with `0`  

### Age
- Must be between 18 and 60 (inclusive)

---

## 🔍 Approach / Logic Used
Each input field is validated separately using basic string operations and conditional statements.  
Boolean variables are used to store the result of each validation.  
If all validations pass, the user profile is marked **VALID**; otherwise, it is marked **INVALID**.  
All given constraints are strictly followed.

---

## 🧾 Algorithm / Steps
1. Start the program.  
2. Accept Full Name, Email ID, Mobile Number, and Age from the user.  
3. Validate the Full Name based on word count and spacing.  
4. Validate the Email ID for required characters and position of `@`.  
5. Validate the Mobile Number for length, numeric content, and starting digit.  
6. Validate the Age for the allowed range.  
7. If all validations succeed, print **"User Profile is VALID"**.  
8. Otherwise, print **"User Profile is INVALID"**.  
9. End the program.

---

## 🧪 Sample Test Cases

### ✅ Test Case 1
**Input:**
- Full Name: Yasir Afaq  
- Email: yasir@gmail.com  
- Mobile Number: 9622949937  
- Age: 29  

**Output:**
User Profile is VALID

### ❌ Test Case 2
**Input:**
- Full Name: Yasir  
- Email: yasirgmail.com  
- Mobile Number: 0876543210  
- Age: 17  

**Output:**
User Profile is INVALID

### ❌ Test Case 3
**Input:**
- Full Name: Yasir Afaq  
- Email: @gmail.com  
- Mobile Number: 98765abc10  
- Age: 45  

**Output:**
User Profile is INVALID
---

## ⚙️ Constraints Followed
- No loops  
- No regular expressions  
- No advanced libraries  
- Only basic string functions such as `len()`, `count()`, and `isdigit()`  

---

## 🎯 Learning Outcome
This challenge helped in understanding how to validate user input using basic Python concepts.  
It improved logical thinking, string manipulation skills, and the ability to solve real-world problems while following strict constraints.

---

## 👤 Author
**Raja Sekhar Reddy**  
B.Tech CSE  
SRM University–AP  

---