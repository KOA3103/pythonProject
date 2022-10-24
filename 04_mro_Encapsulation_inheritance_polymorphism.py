class Student:
    list_all_students_grades = []
    list_all_students_courses = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.list_all_students_grades.append(self.grades)

    def __str__(self):
        return f"Студент\n Имя: {self.name}\n Фамилия: {self.surname}\n " \
               f"Средняя оценка за домашние задания: {self.average_grade_student()}\n " \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n " \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)
        Student.list_all_students_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.leads_courses:
            if isinstance(grade_lecturer, int) and (0 <= grade_lecturer <= 10):
                if course in lecturer.grades_from_student:
                    lecturer.grades_from_student[course] += [grade_lecturer]
                else:
                    lecturer.grades_from_student[course] = [grade_lecturer]
            else:
                print("Оценка введена неверно")
        else:
            return 'Ошибка'

    def average_grade_student(self):
        average = []
        if not self.grades:
            return 0
        for i in self.grades.values():
            average.extend(i)
        return round(sum(average) / len(average), 2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Ментор\n Имя: {self.name}\n Фамилия: {self.surname}"


class Lecturer(Mentor):
    list_all_lecturer_grades = []
    list_all_lecturer_courses = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.leads_courses = []
        self.grades_from_student = {}
        Lecturer.list_all_lecturer_grades.append(self.grades_from_student)

    def __str__(self):
        return f"Лектор\n Имя: {self.name}\n Фамилия: {self.surname}\n " \
               f"Средняя оценка за курсы: {self.average_grade_lecturs()}\n " \
               f"Препадает на курсах: {', '.join(self.leads_courses)}"

    def add_courses(self, course_name):
        self.leads_courses.append(course_name)
        Lecturer.list_all_lecturer_courses.append(course_name)

    def average_grade_lecturs(self):
        average_for_lecturs = []
        if not self.grades_from_student:
            return 0
        for i in self.grades_from_student.values():
            average_for_lecturs.extend(i)
        return round(sum(average_for_lecturs) / len(average_for_lecturs), 2)


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"Ревюер\n Имя: {self.name}\n Фамилия: {self.surname}\n " \
               f"Проверяет ДЗ на курсах: {', '.join(self.courses_attached)}"

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if isinstance(grade, int) and (0 <= grade <= 10):
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                print("Оценка введена неверно")
        else:
            print(f"Ревюер не проверяет курс {course}")


# Создаем экземпляр student_1 класса Student.
student_1 = Student('Петя', 'Петров', 'M')
# Добавляем студенту изучаемый курс.
student_1.add_courses_in_progress("Python")
student_1.add_courses_in_progress("Git")
# Добовляем студенту еще законченый курс.
student_1.add_finished_courses("Введение в программирование")
student_1.add_finished_courses("CSS")

# Создаем экземпляр student_2 класса Student.
student_2 = Student('Саша', 'Александров', 'M')
# Добавляем студенту изучаемый курс.
student_2.add_courses_in_progress("Python")
student_2.add_courses_in_progress("Git")
# Добовляем студенту еще законченый курс.
student_2.add_finished_courses("Введение в программирование")
student_2.add_finished_courses("HTML")

# Создаем экземпляр lecturer_1 класса Lecturer.
lecturer_1 = Lecturer("Николай", "Николаев")
# Добавляем лектору читаемый курс.
lecturer_1.add_courses("Git")
lecturer_1.add_courses("Python")

# Создаем экземпляр lecturer_2 класса Lecturer.
lecturer_2 = Lecturer("Олег", "Олегов")
# Добавляем лектору читаемый курс.
lecturer_2.add_courses("Python")

# Создаем экземпляр reviewer_1 класса Reviewer.
reviewer_1 = Reviewer("Виктор", "Викторов")
# Добовляем курсы которые проверяет reviewer_1.
reviewer_1.courses_attached.append("Python")
reviewer_1.courses_attached.append("Git")

# Создаем экземпляр reviewer_2 класса Reviewer.
reviewer_2 = Reviewer("Павел", "Павлов")
# Добовляем курсы которые проверяет reviewer_1.
reviewer_2.courses_attached.append("Git")

# Выбраному студенту student_1 по опр.курсу ставим отметку, от reviewer_1.
reviewer_1.rate_student(student_1, "Python", 10)
reviewer_1.rate_student(student_1, "Git", 5)

# Выбраному студенту student_2 по опр.курсу Python ставим отметку, от reviewer_1.
reviewer_1.rate_student(student_2, "Python", 6)
reviewer_1.rate_student(student_2, "Git", 8)

# Выбраному студенту student_1 по опр.курсу ставим отметку, от reviewer_2.
reviewer_2.rate_student(student_1, "Git", 5)

# Выбраному студенту student_2 по опр.курсу Git ставим отметку, от reviewer_2.
reviewer_2.rate_student(student_2, "Git", 9)

# От student_1 выставляем оценку lecturer_1.
student_1.rate_lecturer(lecturer_1, "Git", 9)
student_1.rate_lecturer(lecturer_1, "Python", 8)
# От student_1 выставляем оценку lecturer_2.
student_1.rate_lecturer(lecturer_2, "Python", 10)
student_1.rate_lecturer(lecturer_2, "Git", 10)

# От student_2 выставляем оценку lecturer_1.
student_2.rate_lecturer(lecturer_1, "Git", 3)
student_2.rate_lecturer(lecturer_1, "Python", 5)
# От student_1 выставляем оценку lecturer_2.
student_2.rate_lecturer(lecturer_2, "Python", 6)

print('-' * 25)
# Ревюер 1.
print(reviewer_1)

print('-' * 25)
# Ревюер 2.
print(reviewer_2)

print('-' * 25)
# Лектор 1.
print(lecturer_1)

print('-' * 25)
# Лектор 2.
print(lecturer_2)

# Студент 1.
print('-' * 25)
print(student_1)

# Студент 2.
print('-' * 25)
print(student_2)


def average_rating(persons, course):
    list_grades = []
    if course in Lecturer.list_all_lecturer_courses and course in Student.list_all_students_courses:
        for person in persons:
            if course in person:
                for i, n in person.items():
                    if course == i:
                        list_grades += n
        if len(list_grades) != 0:
            result = sum(list_grades) / len(list_grades)
            if persons == Lecturer.list_all_lecturer_grades:
                name = "за лекции всех лекторов"
            else:
                name = "за домашние задания по всем студентам"
            return f"Средняя оценка {name} за курс {course}: {result}"
        else:
            return f"По курсу {course} ни у кого оценок нет!"
    else:
        return f"!!! Курс {course} в изучаемых не значится!!!"


print('-' * 25)
# Средняя оценка по всем студентам курса (созданным объектам) за выбранный курс.
print(average_rating(Student.list_all_students_grades, 'Python'))
print(average_rating(Student.list_all_students_grades, 'Git'))
print(average_rating(Student.list_all_students_grades, 'JS'))

print('-' * 25)
# Средняя оценка по всем лекторам курса (созданным объектам) за выбранный курс.
print(average_rating(Lecturer.list_all_lecturer_grades, 'Python'))
print(average_rating(Lecturer.list_all_lecturer_grades, 'Git'))
print(average_rating(Lecturer.list_all_lecturer_grades, 'JS'))
