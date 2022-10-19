class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


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


# создаем экземпляр класса Student с заданными параметрами
student_1 = Student('Mike', 'Broun', 'M')

# прокидываеи методы в параметры
student_1.courses_in_progress += ['Python']
student_1.finished_courses.append("HTML & CSS")

# создаем экземпляр класса Mentor с заданными параметрами
mentor_1 = Mentor('Some', 'Buddy')
# прокидываеи методы в параметры
mentor_1.courses_attached += ['Python']
mentor_1.courses_attached.append('JS')

# Добовляем студенту (экземпляр класса Student) еще один, новый курс, предмет изучения.
student_1.courses_in_progress.append('JS')


# mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_1, 'JS', 9)
mentor_1.rate_hw(student_1, 'Python', 8)

print('-'*25)
print("Оценки по курсам: ", student_1.grades)

print('-'*25)
print("Студент учится на курсах: ", student_1.courses_in_progress)

print('-'*25)
print("Студент закончил курсы: ", student_1.finished_courses)



print('-'*25)
print("Студент учится на курсах: ", student_1.courses_in_progress)

# Добовляем студенту (экземпляр класса Student) еще один законченый курс.
student_1.finished_courses.append("Engish")

print('-'*25)
print("Студент закончил курсы: ", student_1.finished_courses)

print('-'*25)
mentor_1.rate_hw(student_1, 'JS', 10)
print("Оценки по курсам: ", student_1.grades)
