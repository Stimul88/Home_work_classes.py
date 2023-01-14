class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_1(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_attached and course in lector.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for a, b in best_student.grades.items():
            ever_grade = sum(b) / len(b)
            return f'Студенты:\n' f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за домашние задания: {ever_grade}\n' \
                   f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
                   f'Завершенные курсы: {self.finished_courses}\n'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []


class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        for a, b in cool_lector.grades.items():
            ever_grade = sum(b) / len(b)
            return f'Лекторы:\n' f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за лекции {ever_grade}\n'


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
        return f'Проверяющие:\n' f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.courses_attached += ['Python']
best_student.finished_courses += ['Введение в программирование']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lector = Lecturer('Some', 'Buddy')
cool_lector.courses_in_progress += ['Python']
cool_lector.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_1(cool_lector, 'Python', 5)
best_student.rate_1(cool_lector, 'Python', 8)
best_student.rate_1(cool_lector, 'Python', 7)

# print(best_student.grades)
# print(best_student.grades)

print(cool_reviewer)
print(cool_lector)
print(best_student)
