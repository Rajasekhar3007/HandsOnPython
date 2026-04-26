# 📊 Academic Data Drift & Copy Behavior Analyzer

## 🏫 Project Details
- **Course:** CSE205 – Hands-on Python  
- **University:** SRM University–AP  
- **Challenge:** Code2Xplore – Day 10  
- **Instructor:** Dr. Yasir Afaq  

---

## 📌 Overview
This project analyzes how student academic data behaves when duplicated and modified using **shallow copy** and **deep copy** techniques in Python.  

It demonstrates how improper copying can lead to **data drift** and **unexpected mutations**, which are critical concepts in data processing and analysis.

---

## 🎯 Objectives
- Generate structured student data using Python  
- Understand **shallow vs deep copy behavior**  
- Apply transformations using mathematical functions  
- Perform statistical analysis using **NumPy** and **Pandas**  
- Detect **data drift** between datasets  
- Identify **copy failure due to shared references**  

---

## 📂 Data Structure

Each student record is stored as a dictionary:

```python
{
    "id": int,
    "marks": int,
    "attendance": int,
    "scores": [internal, assignment]
}

Features
✅ Random data generation (10–15 students)
✅ Use of list, dictionary, set, tuple
✅ Implementation of shallow copy & deep copy
✅ Mathematical transformation using sqrt()
✅ Statistical analysis:
Mean
Standard Deviation
✅ Manual mean calculation (without NumPy)
✅ Data drift detection
✅ Copy failure detection
✅ Data visualization using Pandas DataFrame
🔄 Processing Steps
Generate student data using random
Store data in nested dictionary format
Create:
Shallow copy
Deep copy
Apply mutations on copied data:
Modify marks using marks + sqrt(marks)
Update attendance
Change nested scores
Convert data into Pandas DataFrames
Perform statistical analysis using NumPy
Calculate data drift
Detect copy failure
Classify system behavior
🧠 Personalization Logic
Register Number: AP24110011528
Last Digit = 8
8 % 3 = 2

➡️ Mutation applied on indices:

i % 2 == 0
📈 Drift Detection
drift = abs(original_mean - modified_mean)
Classification:
Stable Data → No change
Minor Drift → Small variation
Critical Drift → Large variation
Copy Failure Detected → Original data modified unexpectedly


🚨 Key Concept
Why does shallow copy cause issues?
Shallow copy copies only the outer structure
Inner objects (like lists inside dictionaries) are shared
Modifying shallow copy → also modifies original
Deep Copy Advantage
Creates a completely independent copy
Ensures original data remains unchanged


🧪 Sample Result
DRIFT: 8.36  
STD: 19.26  
STATUS: Copy Failure Detected  


📚 Technologies Used
Python
NumPy
Pandas
Math module
Random module
Copy module


🎓 Learning Outcomes
Difference between shallow copy and deep copy
Handling nested data structures
Detecting unintended data mutations
Performing statistical analysis in Python
Understanding real-world concept of data drift


📝 Conclusion

This project highlights the importance of proper data copying techniques.
It demonstrates how shallow copying can lead to data inconsistency, while deep copying ensures data integrity.