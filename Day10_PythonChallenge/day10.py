import random
import math
import copy
import numpy as np
import pandas as pd

students = []

for i in range(12):
    students.append({
        "id": i + 1,
        "marks": random.randint(40, 100),
        "attendance": random.randint(60, 100),
        "scores": [random.randint(10, 30), random.randint(20, 50)]
    })

original_backup = copy.deepcopy(students)

marks_set = set()
att_set = set()

for i in students:
    marks_set.add(i["marks"])
    att_set.add(i["attendance"])

print("Unique Marks:", marks_set)
print("Unique Attendance:", att_set)

shallow = copy.copy(students)
deep = copy.deepcopy(students)

roll = int(input("Enter roll number: "))
r = roll % 3
if r == 0:
    r = 1

choice = input("Enter inc or dec: ")
value = int(input("Enter value: "))

for i in range(len(shallow)):
    if i % r == 0:
        shallow[i]["marks"] = shallow[i]["marks"] + math.sqrt(shallow[i]["marks"])
        shallow[i]["scores"][0] += 2

        if choice == "inc":
            shallow[i]["attendance"] += value
        else:
            shallow[i]["attendance"] -= value

for i in range(len(deep)):
    if i % r == 0:
        deep[i]["marks"] = deep[i]["marks"] + math.sqrt(deep[i]["marks"])
        deep[i]["scores"][0] += 2

        if choice == "inc":
            deep[i]["attendance"] += value
        else:
            deep[i]["attendance"] -= value

df1 = pd.DataFrame(original_backup)
df2 = pd.DataFrame(shallow)
df3 = pd.DataFrame(deep)

print("\nORIGINAL")
print(df1)

print("\nSHALLOW")
print(df2)

print("\nDEEP")
print(df3)

orig_marks = [i["marks"] for i in original_backup]
deep_marks = [i["marks"] for i in deep]

mean_orig = np.mean(orig_marks)
mean_deep = np.mean(deep_marks)
std = np.std(deep_marks)

manual_mean = sum(deep_marks) / len(deep_marks)

drift = abs(mean_orig - mean_deep)

threshold = 6

copy_failure = False
if students != original_backup:
    copy_failure = True

if copy_failure:
    status = "Copy Failure Detected"
elif drift == 0:
    status = "Stable Data"
elif drift <= threshold:
    status = "Minor Drift"
else:
    status = "Critical Drift"

result = (mean_deep, drift, std)

print("\nDRIFT:", drift)
print("STD:", std)
print("MANUAL MEAN:", manual_mean)
print("TUPLE:", result)
print("STATUS:", status)

print("\nEXPLANATION:")
print("Shallow copy shares nested objects, so modifying it affects original data.")
print("Deep copy creates independent data, so original remains unchanged.")