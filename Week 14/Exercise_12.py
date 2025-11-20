# Exercise 12 - Vanessa Belous

import numpy as np

def col_stats(data):
    # Per Column: Mean (average), Median, Standard Deviation, Minimum, Maximum
    print("\n***Statistics for each exam (columns):")
    # Cols Mean (Average)
    print("Mean (Average)")
    print("\tExam 1:", np.mean(data[:, 3]))
    print("\tExam 2:", np.mean(data[:, 4]))
    print("\tExam 3:", np.mean(data[:, 5]))
    # Cols Median
    print("Medians")
    print("\tExam 1:", np.median(data[:, 3]))
    print("\tExam 2:", np.median(data[:, 4]))
    print("\tExam 3:", np.median(data[:, 5]))
    # Cols Standard Deviation
    print("Standard Deviations")
    print("\tExam 1:", np.std(data[:, 3]))
    print("\tExam 2:", np.std(data[:, 4]))
    print("\tExam 3:", np.std(data[:, 5]))
    # Cols Minimum
    print("Lowest Scores")
    print("\tExam 1:", np.min(data[:, 3]))
    print("\tExam 2:", np.min(data[:, 4]))
    print("\tExam 3:", np.min(data[:, 5]))
    # Cols Maximum
    print("Highest Scores")
    print("\tExam 1:", np.max(data[:, 3]))
    print("\tExam 2:", np.max(data[:, 4]))
    print("\tExam 3:", np.max(data[:, 5]))

def total_stats(data):
    # Mean (average), Median, Standard Deviation, Minimum, Maximum
    print("\n***Total Statistics (across entire dataset):")
    exams = data[:,3:6]
    # Overall Mean
    print("\tTotal Mean:", np.mean(exams))
    # Overall Median
    print("\tTotal Median:", np.median(exams))
    # Total Standard Deviation
    print("\tTotal Standard Deviation:", np.std(exams))
    # Overall Minimum
    print("\tLowest Score of the Year:", np.min(exams))
    # Overall Maximum
    print("\tHighest Score of the Year:", np.max(exams))

def pass_fail(data):
    print("\n***Pass/Fail Statistics:")

    # Exam 1
    print("Exam 1")
    p1 = 0
    f1 = 0
    exam_1 = data[:, 3]
    for score in exam_1:
        if score >= 60:
            p1 += 1
        else:
            f1 += 1
    print("\tStudents Passed:", p1)
    print("\tStudents Failed:", f1)

    # Exam 2
    print("Exam 2")
    p2 = 0
    f2 = 0
    exam_2 = data[:, 4]
    for score in exam_2:
        if score >= 60:
            p2 += 1
        else:
            f2 += 1
    print("\tStudents Passed:", p2)
    print("\tStudents Failed:", f2)

    # Exam 3
    print("Exam 3")
    p3 = 0
    f3 = 0
    exam_3 = data[:, 5]
    for score in exam_3:
        if score >= 60:
            p3 += 1
        else:
            f3 += 1
    print("\tStudents Passed:", p3)
    print("\tStudents Failed:", f3)

    # Pass Percentages
    overall_pass = p1 + p2 + p3
    pass_percent = (overall_pass / 30) * 100
    print("Pass Percentage (Overall): " + f'{pass_percent:.2f}' + " %")


def main():
    # 2. Load data from grades.csv file
    data = np.genfromtxt('grades.csv', delimiter=',')

    # 3. Print first few rows of dataset
    print("First few rows of dataset:")
    print(data[0])
    print(data[1])
    print(data[2])

    # 4. Calculate statistics for each exam
    col_stats(data)

    # 5. Calculate statistics for entire dataset (all exams combined)
    total_stats(data)

    # 6. Number of students who passed/failed each exam & 7. Pass Percentage
    pass_fail(data)

main()