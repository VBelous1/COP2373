# CSV Exercise - Vanessa Belous
# This program will read the custom csv file, displaying the information in a formatted way

import csv

def main():
    with open("grades.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # print formatted header
        formatted_headers = [f'{header:^15}' for header in csv_reader.fieldnames]
        print("|", " | ".join(formatted_headers), "|")

        # print formatted rows
        for row in csv_reader:
            # format the data
            student_number = '{:^15}'.format(row["#"])
            first_name = '{:<15}'.format(row["First Name"])
            last_name = '{:<15}'.format(row["Last Name"])
            exam_1 = '{:^15}'.format(row["Exam 1"])
            exam_2 = '{:^15}'.format(row["Exam 2"])
            exam_3 = '{:^15}'.format(row["Exam 3"])
            # print the data
            print("|", student_number, "|", first_name, "|", last_name, "|", exam_1, "|", exam_2, "|", exam_3, "|")

    csv_file.close()

main()