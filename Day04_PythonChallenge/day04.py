# Security Activity Risk Analyser

# Enter your Registration Number
reg_no = input("Enter your Registration Number: ")

# Extract last digit
D = int(reg_no[-1])

print("Registration Digit(D):", D)

# Input Activity Scores
n = int(input("Enter number of activities scores: "))
scores = []

for i in range(n):
    value = int(input("Enter  activity score: "))
    scores += [value]

# Separate risk category lists
low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

valid_count = 0
ignored_count = 0

# Categorization
for i in range(len(scores)):
    if scores[i] < 0:
        ignored_count += 1
    else:
        valid_count += 1
        if scores[i] <= 30:
            low_risk += [scores[i]]
        elif scores[i] <= 60:
            medium_risk += [scores[i]]
        elif scores[i] <= 100:
            high_risk += [scores[i]]
        else:
            critical_risk += [scores[i]]

removed = 0

print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)
print(" ")

# Personalized Filtering
print("After Personalized Filtering:")
if D % 2 == 0:
    removed = len(low_risk)
    low_risk = []
else:
    removed = len(critical_risk)
    critical_risk = []

# Final Output

print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)
print(" ")
print("Total Valid Entries:", valid_count)
print("Ignored Entries:", ignored_count)
print("Removed Due to Personalization:", removed)