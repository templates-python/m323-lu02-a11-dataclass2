"""Immutable Dataclass.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu02/aufgaben/dataclass2
"""

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
    demo_student = Student(name='John Doe')
    demo_student = add_grade(demo_student, 85)
    demo_student = add_grade(demo_student, 75)
    demo_student = add_grade(demo_student, 60)

    print(f'Noten: {demo_student.grades}')
    average = calculate_average(demo_student)
    print(f'Durchschnitt: {average}')

    demo_student = graduate_student(demo_student)
    print(f'Absolviert: {demo_student.graduated}')
