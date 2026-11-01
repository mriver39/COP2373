# Programming Exercise CSV
# COP 2373
# Creates a CSV file containing student grades
# Then reads and displays the data in tabular format

import csv


def create_csv_file():

    # Creates grades.csv and stores student information.
    num_students = int(input("How many students would you like to enter? "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow([
            "First Name",
            "Last Name",
            "Exam 1",
            "Exam 2",
            "Exam 3"
        ])

        # Enter student data
        for student in range(num_students):
            print(f"\nStudent {student + 1}")

            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            exam1 = int(input("Exam 1 Grade: "))
            exam2 = int(input("Exam 2 Grade: "))
            exam3 = int(input("Exam 3 Grade: "))

            writer.writerow([
                first_name,
                last_name,
                exam1,
                exam2,
                exam3
            ])

    print("\ngrades.csv has been created successfully.")


def display_csv_file():

    # Reads grades.csv and displays the contents.
    print("\nStudent Grade Report")
    print("-" * 65)

    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(
                f"{row[0]:<15}"
                f"{row[1]:<15}"
                f"{row[2]:<10}"
                f"{row[3]:<10}"
                f"{row[4]:<10}"
            )


def main():

    # Controls program execution.

    create_csv_file()
    display_csv_file()


# Start program
main()