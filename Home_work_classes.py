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

    def av_rating(self):
        sum_grades = 0
        len_rating = 0
        for course in self.grades.values():
            sum_grades += sum(course)
            len_rating += len(course)
            ever_grade = round(sum_grades / len_rating, 2)
        return ever_grade

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
                average_rating = round(sum_rating / len_rating, 2)
                res = average_rating
        return res

    def __str__(self):
        res = f'Студент:\n'f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.av_rating()}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.av_rating() < other.av_rating()


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

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
            ever_grade = round(sum_rating / len_rating, 2)
        return ever_grade

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
                average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        res = f'Лектор:\n'f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.av_rating()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.av_rating() < other.av_rating()


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
        return f'Проверяющий: \n'f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'


student_1 = Student('Женя ', 'Иванов', 'муж.')
student_2 = Student('Андрей', 'Васильев', 'муж.')

student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python']

student_1.courses_attached += ['Python']
student_2.courses_attached += ['Python']

student_1.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lector1 = Lecturer('Анатолий', 'Михайлов')
cool_lector2 = Lecturer('Анна', 'Васильева')

cool_lector1.courses_in_progress += ['Python']
cool_lector2.courses_in_progress += ['Python']

cool_lector1.courses_attached += ['Python']
cool_lector2.courses_attached += ['Python']

cool_reviewer = Reviewer('Аркадий', 'Смирнов')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(student_1, 'Python', 10)
cool_reviewer.rate_hw(student_1, 'Python', 6)

cool_reviewer.rate_hw(student_2, 'Python', 7)
cool_reviewer.rate_hw(student_2, 'Python', 8)

student_1.rate_1(cool_lector1, 'Python', 10)
student_1.rate_1(cool_lector1, 'Python', 8)
student_1.rate_1(cool_lector1, 'Python', 9)

student_1.rate_1(cool_lector2, 'Python', 10)
student_1.rate_1(cool_lector2, 'Python', 8)
student_1.rate_1(cool_lector2, 'Python', 7)

student_2.rate_1(cool_lector1, 'Python', 10)
student_2.rate_1(cool_lector1, 'Python', 8)
student_2.rate_1(cool_lector1, 'Python', 9)

student_2.rate_1(cool_lector2, 'Python', 10)
student_2.rate_1(cool_lector2, 'Python', 8)
student_2.rate_1(cool_lector2, 'Python', 7)

student_list = [student_1, student_2]
lecturer_list = [cool_lector1, cool_lector2]


def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
            average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(cool_reviewer)

print(cool_lector1)
print(cool_lector2)

print(student_1)
print(student_2)

res1 = average_rating_for_course('Python', student_list)
res2 = average_rating_for_course('Python', lecturer_list)
print(f'Средняя оценка за домашние задания по всем студентам: {res1}\n')
print(f'Средняя оценка за лекции всех лекторов: {res2}\n')

print(student_1 < student_2)
print(cool_lector1 < cool_lector2)
