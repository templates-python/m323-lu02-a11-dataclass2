def add_grade(student, grade):
    """
    Returns a new Student instance with the added grade.
    """
    # todo: implement this function
    pass

def calculate_average(student):
    """
    Returns the average of the student's grades.
    """
    # todo: implement this function
    pass


def graduate_student(student):
    """
    Graduates the student if the average grade is 70 or above.
    """
    # todo: implement this function
    pass


if __name__ == '__main__':
    student = Student(name='John Doe')
    student = add_grade(student, 85)
    student = add_grade(student, 75)
    student = add_grade(student, 60)

    print(f'Noten: {student.grades}')
    average = calculate_average(student)
    print(f'Durchschnitt: {average}')

    student = graduate_student(student)
    print(f'Absolviert: {student.graduated}')