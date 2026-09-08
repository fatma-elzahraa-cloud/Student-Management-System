

def add_grade(student, subject, grade):
    student.grades[subject] = grade
    print("Grade added successfully.")


def update_grade(student, subject, new_grade):
    if subject in student.grades:
        student.grades[subject] = new_grade
        print("Grade updated successfully.")
    else:
        print("Subject not found.")


def calculate_average(student):
    if len(student.grades) == 0:
        return 0

    return sum(student.grades.values()) / len(student.grades)