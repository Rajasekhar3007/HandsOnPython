Smart Transaction Risk Detector
📌 Project Description

This project is a Python-based system designed to analyze a user’s daily transaction data and detect potential financial risks. The program classifies each transaction into different categories such as normal, large, high-risk, or invalid. After classification, it identifies suspicious patterns like frequent transactions, high total spending, and multiple high-risk transactions.

Based on these patterns, the system generates a final risk level to help in detecting possible fraudulent activity.

⚙️ Features

Accepts multiple transaction inputs from the user

Classifies transactions into:

Normal (1–500)

Large (501–2000)

High Risk (>2000)

Invalid (≤0)

Detects patterns:

Frequent transactions (>5)

Large spending (>5000)

Suspicious activity (≥3 high-risk transactions)

Generates final risk level:

Low Risk

Moderate Risk

High Risk

Uses Python concepts like:

Lists

Loops

Conditional statements

List comprehension

Dictionary

Tuple

🧠 Approach

User inputs transaction amounts which are stored in a list.

Each transaction is classified using conditional statements.

A dictionary is used to store categorized transactions.

List comprehension is used to filter valid transactions.

Patterns are detected based on transaction count, sum, and risk category.

Final risk level is decided based on priority conditions.

Results are displayed along with a summary stored in a tuple.

🧪 Sample Test Case
Input:
5
2500
3000
4000
100
200

Output:
Transaction Categories:
Normal : [100, 200]
Large : []
High Risk : [2500, 3000, 4000]
Invalid : []

Summary:
Total Valid Amount: 9800
Number of Transactions: 5
Risk Level: High Risk

💡 Key Logic Decision

The system prioritizes suspicious activity (high-risk transactions) over other conditions.
If 3 or more high-risk transactions are detected, the system directly classifies the user as High Risk, even if other conditions are normal.

🎯 Learning Outcome

Learned how to process and analyze data using Python

Improved understanding of lists, dictionaries, and tuples

Gained experience in writing logical conditions for real-world problems

Practiced clean and structured coding

📂 How to Run

Open the Python file

Run the program

Enter number of transactions

Enter transaction amounts one by one

View categorized output and final risk level

👨‍💻 Author

Raja Sekhar Reddy Thippireddy