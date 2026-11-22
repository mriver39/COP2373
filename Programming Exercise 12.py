import numpy as np


def calculate_exam_statistics(grades):
    """Calculate statistics for each exam."""

    print("\nEXAM STATISTICS")
    print("-" * 40)

    for i in range(grades.shape[1]):
        exam = grades[:, i]

        print(f"\nExam {i + 1}")
        print(f"Mean: {np.mean(exam):.2f}")
        print(f"Median: {np.median(exam):.2f}")
        print(f"Standard Deviation: {np.std(exam):.2f}")
        print(f"Minimum: {np.min(exam)}")
        print(f"Maximum: {np.max(exam)}")

        passed = np.sum(exam >= 60)
        failed = np.sum(exam < 60)

        print(f"Passed: {passed}")
        print(f"Failed: {failed}")


def calculate_overall_statistics(grades):
    """Calculate overall statistics for all exams combined."""

    all_grades = grades.flatten()

    print("\nOVERALL STATISTICS")
    print("-" * 40)

    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Standard Deviation: {np.std(all_grades):.2f}")
    print(f"Minimum: {np.min(all_grades)}")
    print(f"Maximum: {np.max(all_grades)}")

    pass_percentage = (np.sum(all_grades >= 60) / len(all_grades)) * 100

    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")


def main():

    grades = np.genfromtxt(
        "grades.csv",
        delimiter=",",
        skip_header=1,
        usecols=(2, 3, 4)
    )

    print("FIRST FIVE ROWS")
    print("-" * 40)
    print(grades[:5])

    calculate_exam_statistics(grades)

    calculate_overall_statistics(grades)


main()