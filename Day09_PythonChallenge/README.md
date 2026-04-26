# 🧠 Smart Inventory Mutation Tracker

## 📌 Project Overview
This project simulates a warehouse inventory system using Python. Each product contains nested details such as price, stock, and supplier information. The main goal is to analyze how data behaves when copied using **shallow copy** and **deep copy**, and how modifications affect the original data.

---

## 🎯 Objective
- Understand the difference between shallow copy and deep copy
- Track how mutations in copied data impact original data
- Simulate real-world data corruption scenarios
- Apply personalized logic using roll number

---

## 🗂️ Data Structure Used
The inventory is stored as a **list of dictionaries** with nested fields:

```python
{
  "item": "Laptop",
  "details": {"price": 50000, "stock": 10},
  "supplier": {"name": "ABC", "rating": 4.5}
}

---

## ⚙️ Features
- ✅ Uses **nested dictionaries and lists**
- ✅ Implements **functions** for modular design
- ✅ Creates both:
  - Shallow Copy
  - Deep Copy
- ✅ Applies **mutation logic**:
  - 10% price reduction
  - Stock increase/decrease
- ✅ Tracks and compares changes
- ✅ Generates tuple summary: `(changed_items, unchanged_items)`
- ✅ Includes additional nested field (`supplier rating`)

---

## 🔁 Custom Mutation Rule
The item to be modified is selected using:

```python
index = roll_number % length_of_inventory

This ensures:
Personalization for each student
Dynamic and non-hardcoded behavior

🧪 Test Cases Used
Roll Number	Index	Item Modified
24110011528	3	Air Conditioner
24110010967	2	Television
22110011363	3	Air Conditioner

🔍 Key Observations

🔴 Shallow Copy
Copies only the outer list
Inner dictionaries are shared references
Changes in copied data affect the original ❌
🟢 Deep Copy
Creates completely independent copies
No shared references
Original data remains unchanged ✅

📊 Sample Output Summary

Shallow (changed, same): (1, 4)
Deep    (changed, same): (1, 4)


🧠 Learning Outcomes

Learned the difference between shallow and deep copy
Understood how memory references work in Python
Gained experience with nested data structures
Applied real-world logic using roll number
Improved debugging and data comparison skills


🛠️ Technologies Used

Python
Built-in copy module

📌 How to Run
Open the Python file
Run the program
Enter:
Roll number
Operation (inc/dec)
Value
Observe outputs and comparisons

📄 Conclusion

This project demonstrates how shallow copy can unintentionally modify original data due to shared references, while deep copy prevents such issues by creating independent copies. It highlights the importance of proper data handling in real-world applications.