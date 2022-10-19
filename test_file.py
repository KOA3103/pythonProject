from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_grade()}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}"

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecturer(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.leads_courses:
            if course in lecturer.grades_from_student:
                lecturer.grades_from_student[course] += [grade_lecturer]
            else:
                lecturer.grades_from_student[course] = [grade_lecturer]
        else:
            return 'Ошибка'

    def average_grade(self):
        average = 0
        for i in self.grades.values():
            average += mean(i)
        return average / len(self.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.leads_courses = []
        self.grades_from_student = {}

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции:{self.grades_from_student.values()}"

    def add_courses(self, course_name):
        self.leads_courses.append(course_name)

    def average_mark_for_lecturs(self):
        for i in self.grades_from_student.values():
            return i



class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

print('-'*25)
# Создаем экземпляр класса Student.
student_1 = Student('Петя', 'Петров', 'M')
# Добавляем студенту изучаемый курс.
student_1.add_courses_in_progress("Python")
student_1.add_courses_in_progress("Git")
# Добовляем студенту еще законченый курс.
student_1.add_finished_courses("Введение в программирование")

# print(f"Курсы в процессе изучения: {student_1.courses_in_progress}")
# print(f"Завершенные курсы: {student_1.finished_courses}")


print('-'*25)
# Создаем экземпляр класса Lecturer.
lecturer_1 = Lecturer("Иавн", "Иванов")
# Добавляем лектору читаемый курс.
lecturer_1.add_courses("Python")
lecturer_1.add_courses("Git")
# print(lecturer_1)
# print(lecturer_1.average_mark_for_lecturs())

print('-'*25)
# Создаем экземпляр класса Reviewer.
reviewer_1 = Reviewer("Виктор", "Викторов")
# Добовляем курсы которые проверяет reviewer_1.
reviewer_1.courses_attached.append("Python")
reviewer_1.courses_attached.append("Git")

# Выбраному студенту по опр.курсу ставим отметку.
reviewer_1.rate_student(student_1, "Python", 2)
reviewer_1.rate_student(student_1, "Python", 4)
reviewer_1.rate_student(student_1, "Python", 6)
reviewer_1.rate_student(student_1, "Git", 8)
reviewer_1.rate_student(student_1, "Git", 4)


# Создаем экземпляр класса Mentor.
# mentor_1 = Mentor("Roman", "Petrov")
# print(mentor_1)

# Выбраному студенту выводим все оценки по всем курсам.
# print("-"*35,f"\n Студент\n{student_1}\n Оценки по курсам: {student_1.grades}")

# От student выставляем оценку lecturer.
student_1.rate_lecturer(lecturer_1, "Python", 7)


# Выбраному lecturer_1 выводим все оценки за все курсы.
# print("-"*35,f"\n Лектор\n{lecturer_1}\n Оценки за курсы: {lecturer_1.grades_from_student}")


# print(student_1.grades)
print(student_1)

