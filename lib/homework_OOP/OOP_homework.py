class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_number = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_number

    def __str__(self):
        return f'Имя: {sel.name}\n Фамилия: {self.surname}\n Средняя оценка за лекцию: {self.avarage_grade()}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'ошибка'

    def average_grade(self):
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_number = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_number

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

def average_students_grade(students, course):
    total_grades = 0
    total_number = 0

    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_number += len(student.grades[course])

    return total_grades / total_number

def average_lecturers_grade(lecturers, course):
    total_grades = 0
    total_number = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_number += len(lecturer.grades[course])

    return total_grades / total_number

reviewer1 = Reviewer("Василий", "Иванов")
reviewer2 = Reviewer("Виктор", "Сергеев")

lecturer1 = Lecturer("Иван", "Михайлов")
lecturer1.courses_attached = ["Python", "Mathematics"]
lecturer2 = Lecturer("Дмитрий", "Немцов")
lecturer2.courses_attached = ["Python", "C++"]

student1 = Student("Марк", "Кочнев", "male")
student1.courses_in_progress = ["Python", "C++"]
student1.finished_courses = ["Basic"]

student2 = Student("Максим", "Мальцев", "male")
student2.courses_in_progress = ["Python"]
student2.finished_courses = ["Design"]

reviewer1.courses_attached.append("Python")
reviewer2.courses_attached.append("C++")

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Python', 10)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'C++', 8)

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Python', 10)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'C++', 8)

print(average_students_grade([student1, student2], 'Python'))
print(average_lecturers_grade([lecturer1, lecturer2], 'Python'))


