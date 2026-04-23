# 📊 Multi-Dimensional Academic Intelligence System

## 🏫 Course Details
- **Course**: Python: Code2Xplore - 60 Days Challenge  
- **Subject**: Hands-on Python (CSE205)  
- **University**: SRM University–AP  
- **Instructor**: Dr. Yasir Afaq  
- **Challenge**: DAY-6  

---

## 📌 Problem Overview

This project analyzes student performance using multiple academic factors such as marks, attendance, and assignment scores.  

Instead of basic data handling, the system uses structured data, statistical analysis, feature engineering, and visualization to generate meaningful academic insights.

---

## 🎯 Objectives

- Generate student data using random values  
- Store data using Python data structures  
- Perform statistical analysis using NumPy and Pandas  
- Classify students into performance categories  
- Detect patterns and generate system insights  
- Visualize marks distribution  

---

## 🧠 Key Features

### 1. Data Generation
- Randomly generates student records  
- Fields:
  - Student ID  
  - Marks (0–100)  
  - Attendance (0–100)  
  - Assignment Score (0–50)  

---

### 2. Data Structures Used
- **List** → store all student records  
- **Tuple** → individual student record  
- **Dictionary** → classification categories  

---

### 3. Feature Engineering

A custom metric called **Performance Index** is calculated:
performance_index = (marks * 0.6 + assignment * 0.4) * log(attendance + 1)


#### Why this works:
- Gives higher importance to marks (60%)  
- Includes assignment performance (40%)  
- Uses logarithmic scaling for attendance:
  - Penalizes low attendance  
  - Avoids extreme growth  

---

### 4. Student Classification

| Condition | Category |
|----------|--------|
| marks < 40 OR attendance < 50 | At Risk |
| marks 40–70 | Average |
| marks 71–90 | Good |
| marks > 90 AND attendance > 80 | Top Performer |

---

### 5. Statistical Analysis

Using **NumPy & Pandas**:
- Mean  
- Median  
- Standard Deviation  
- Correlation (Marks vs Attendance)  

✔ Manual mean calculation included (as per constraints)

---

### 6. Data Normalization

Min-Max Normalization applied:
normalized = (x - min) / (max - min)


---

### 7. Pattern Detection

- **Consistency** → std deviation < 15  
- **Attendance Risk** → more than 3 students below 50%  
- **High Achievement** → at least 2 top performers  

---

### 8. Final Insight Generation

System outputs:
- Stable Academic System  
- Moderate Performance  
- Critical Attention Required  

---

### 9. Visualization (Bonus)

- Histogram of marks distribution using Matplotlib  
- Helps identify:
  - Data spread  
  - Performance trends  

---

## ⚙️ Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- math module  
- random module  

---

## 🧪 Test Cases

Multiple test cases were verified using fixed datasets to ensure:
- Correct classification  
- Accurate statistical calculations  
- Proper insight generation  

---

## 🚀 How to Run

```bash
python your_file_name.py
