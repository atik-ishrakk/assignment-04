def take_input(subject):
    while True:
        try:
            return float(input(f"Enter the marks for {subject}: "))
        except ValueError:
            print("Error: Marks should be a valid number between 0 and 100.")

def calculate_average(marks):
    return sum(marks) / len(marks)

def determine_grade(average_marks):
    if average_marks >= 91:
        return 'A+'
    elif average_marks >= 81:
        return 'A'
    elif average_marks >= 71:
        return 'B'
    elif average_marks >= 61:
        return 'C'
    elif average_marks >= 41:
        return 'D'
    else:
        return 'F'


subjects = ["Bengali", "English", "Math", "Science"]
marks = [take_input(subject) for subject in subjects]
average_marks = calculate_average(marks)
grade = determine_grade(average_marks)


print("Subject\t\tMarks")
for subject, mark in zip(subjects, marks):
    print(f"{subject}\t\t{mark}")
print(f"Average Marks: {average_marks}")
print(f"Grade: {grade}")
