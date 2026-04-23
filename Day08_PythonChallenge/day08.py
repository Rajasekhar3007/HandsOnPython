import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_data(n):
    data = []
    for i in range(1, n + 1):
        student_id = f"S{i:03}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)

        data.append((student_id, marks, attendance, assignment, performance_index))

    return data

def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for student in data:
        sid, marks, attendance, assignment, pi = student

        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)

        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)

        elif 71 <= marks <= 90:
            categories["Good"].append(sid)

        else:
            categories["Average"].append(sid)

    return categories

def analyze_data(df):
    marks_array = df["Marks"].values

    mean_marks = np.mean(marks_array)
    median_marks = np.median(marks_array)
    std_dev = np.std(marks_array)

    manual_mean = sum(marks_array) / len(marks_array)

    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0, 1]

    min_val = np.min(marks_array)
    max_val = np.max(marks_array)
    df["Normalized Marks"] = [(x - min_val) / (max_val - min_val) for x in marks_array]

    consistency = "Consistent" if std_dev < 15 else "Inconsistent"
    attendance_risk = len(df[df["Attendance"] < 50]) > 3
    top_performers = len(df[(df["Marks"] > 90) & (df["Attendance"] > 80)]) >= 2

    if consistency == "Consistent" and not attendance_risk and top_performers:
        insight = "Stable Academic System"
    elif attendance_risk or not top_performers:
        insight = "Critical Attention Required"
    else:
        insight = "Moderate Performance"

    summary_tuple = (mean_marks, std_dev, np.max(marks_array))

    return {
        "mean": mean_marks,
        "median": median_marks,
        "std_dev": std_dev,
        "manual_mean": manual_mean,
        "correlation": correlation,
        "consistency": consistency,
        "attendance_risk": attendance_risk,
        "top_performers": top_performers,
        "insight": insight,
        "tuple": summary_tuple,
        "df": df
    }

def plot_marks_distribution(df):
    plt.figure()
    plt.hist(df["Marks"], bins=5)
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.grid()
    plt.show()

if __name__ == "__main__":

    n_students = 8

    student_data = generate_data(n_students)

    df = pd.DataFrame(student_data, columns=[
        "Student_ID", "Marks", "Attendance", "Assignment", "Performance_Index"
    ])

    categories = classify_students(student_data)

    results = analyze_data(df)

    print("\n STUDENT DATAFRAME:")
    print(results["df"])

    print("\n CATEGORIZED STUDENTS:")
    for category, students in categories.items():
        print(f"{category}: {students}")

    print("\n STATISTICAL SUMMARY:")
    print(f"Mean: {results['mean']}")
    print(f"Median: {results['median']}")
    print(f"Standard Deviation: {results['std_dev']}")
    print(f"Manual Mean: {results['manual_mean']}")

    print("\n CORRELATION (Marks vs Attendance):")
    print(results["correlation"])

    print("\n SUMMARY TUPLE (mean, std_dev, max_marks):")
    print(results["tuple"])

    print("\n FINAL SYSTEM INSIGHT:")
    print(results["insight"])

    plot_marks_distribution(results["df"])