# Практическое задание «ООП: наследование, инкапсуляция и полиморфизм»

# Задание № 1. Наследование

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, courses_name):
        self.finished_courses.append(courses_name)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    pass


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []


# Задание № 2. Атрибуты и взаимодействие классов.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, courses_name):
        self.finished_courses.append(courses_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    pass




lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алехина', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}


#Задание № 3. Полиморфизм и магические методы

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, courses_name):
        self.finished_courses.append(courses_name)

    def __str__(self):
        mean_stud = []
        for i in self.grades.values():
            mean_stud += i
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {sum(mean_stud)/len(mean_stud)} \n'
                    f'Курсы в процессе обучения: {', '.join(self.courses_in_progress)} \n'
                    f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __str__(self):
        mean_lect = []
        for v in self.grades.values():
            mean_lect += v
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {sum(mean_lect)/len(mean_lect)}'

class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алехина', 'Ж')
#
student.finished_courses += ['C++']
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))
print(reviewer.rate_hw(student, 'Python', 7)) # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(reviewer.rate_hw(student, 'Python', 6))

print(reviewer)  # {'Python': [7]}
print('_______________________________________________________')
print(lecturer)
print('_______________________________________________________')
print(student)

# Задание № 4. Полевые испытания

student_1 = Student('Ольга', 'Алехина', 'Ж')
student_2 = Student('Амадей', 'Сидоров', 'М')
mentor_1 = Mentor('Екатерина', 'Пупкина')
mentor_2 = Mentor('Кристина', 'Петрова')
lecturer_1 = Lecturer('Александр', 'Достоевский')
lecturer_2 = Lecturer('Вячеслав', 'Тютчев')
reviewer_1 = Reviewer('Ирина', 'Иванова')
reviewer_2 = Reviewer('Татьяна', 'Егорова')

student_1.finished_courses += ['C++']
student_2.finished_courses += ['Java']
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Javascript', 'C++']
lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Javascript', 'Java']
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Javascript', 'Java']

student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_2, 'Java', 8)
student_2.rate_lecture(lecturer_1, 'С++', 8)
student_2.rate_lecture(lecturer_2, 'Javascript', 6)
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Javascript', 6)
reviewer_2.rate_hw(student_2, 'C++', 7)



print(reviewer_1)
print('_______________________________________________________')
print(reviewer_2)
print('_______________________________________________________')
print(lecturer_1)
print('_______________________________________________________')
print(lecturer_2)
print('_______________________________________________________')
print(student_1)
print('_______________________________________________________')
print(student_2)
print('_______________________________________________________')
print(mentor_1)
print('_______________________________________________________')
print(mentor_2)


