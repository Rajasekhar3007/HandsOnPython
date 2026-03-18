# Smart Transaction Risk Detector
# Number of transactions
n = int(input("Enter the number of transaction data: "))

transactions = []

for i in range(n):
    t = int(input("Enter the transaction amount: "))
    transactions.append(t)

# Dictionary for classification
categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}

# Classification of transactions
for t in transactions:
    if t <= 0:
        categories["invalid"].append(t)
    elif t <= 500:
        categories["normal"].append(t)
    elif t <= 2000:
        categories["large"].append(t)
    else:
        categories["high_risk"].append(t)

# List Comprehension (Valid transactions only)
valid_transactions = [t for t in transactions if t > 0]
total_valid = sum(valid_transactions)
count = len(transactions)

# Pattern Detection
frequent = count > 5
large_spending = total_valid > 5000
suspicious = len(categories["high_risk"]) >= 3

# Risk Classification
if suspicious:
    risk = "High Risk"
elif frequent or large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

# Tuple Summary
summary = (total_valid, count, risk)

# Output
print("\nTransaction Categories:")
print("Normal :", categories["normal"])
print("Large :", categories["large"])
print("High Risk :", categories["high_risk"])
print("Invalid :", categories["invalid"])

print("\nSummary:")
print("Total Valid Amount:", summary[0])
print("Number of Transactions:", summary[1])
print("Risk Level:", summary[2])
