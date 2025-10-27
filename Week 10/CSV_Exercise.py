# CSV Exercise - Vanessa Belous
# This program lets an instructor create a custom csv file to track their students' exam grads

import csv

# this function writes the users data to the csv file
def write_csv(total):
    filename = 'grades.csv'
    header = ["#", "First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # write header to file
        csv_writer.writerow(header)

        counter = 1

        # this while loop runs until the counter matches how many students the user says they have
        while True:
            if counter <= total:
                # accepts user input
                print("\nStudent #", counter)
                first_name = str(input("Enter first name: "))
                last_name = str(input("Enter last name: "))
                exam1 = int(input("Enter Exam 1 Grade: "))
                exam2 = int(input("Enter Exam 2 Grade: "))
                exam3 = int(input("Enter Exam 3 Grade: "))
                # writes data to csv file
                student_data = [counter, first_name, last_name, exam1, exam2, exam3]
                csv_writer.writerow(student_data)
                counter += 1
            else:
                break

        csv_file.close()

def main():
    total_students = int(input("Please enter how many students you have: "))
    write_csv(total_students)

main()