class Student:
    all_students = []
    courses_in_progress = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def __str__(self):
        return f"Студент\n Имя: {self.name}\n Фамилия: {self.surname}\n " \
               f"Средняя оценка за домашние задания: {self.average_grade_student()}\n " \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n " \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Ошибка! Сравнение двух объектов разных классов!"
        if self.average_grade_student() == other.average_grade_student():
            return f" Средняя оценка студента {self.name} {self.surname} " \
                   f"равна средней оценке студента {other.name} {other.surname}"
        else:
            return f" Средняя оценка студента {self.name} {self.surname} не " \
                   f"равна средней оценке студента {other.name} {other.surname}"

    def __le__(self, other):
        if not isinstance(other, Student):
            return "Ошибка! Сравнение двух объектов разных классов!"
        if self.average_grade_student() <= other.average_grade_student():
            return f" Средняя оценка студента {self.name} {self.surname} " \
                   f"меньше или равна средней оценке студента {other.name} {other.surname}"
        else:
            return f" Средняя оценка студента {self.name} {self.surname} " \
                   f"больше средней оценке студента {other.name} {other.surname}"

    def __gt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка! Сравнение двух объектов разных классов!"
        if self.average_grade_student() > other.average_grade_student():
            return f" Средняя оценка студента {self.name} {self.surname} " \
                   f"больше средней оценке студента {other.name} {other.surname}"
        else:
            return f" Средняя оценка студента {self.name} {self.surname} " \
                   f"меньше или равно средней оценке студента {other.name} {other.surname}"

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)
        Student.courses_in_progress += self.courses_in_progress

    def rate_lecturer(self, lecturer, course, grade_lecturer):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_in_progress:
            if isinstance(grade_lecturer, int) and (0 <= grade_lecturer <= 10):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade_lecturer]
                else:
                    lecturer.grades[course] = [grade_lecturer]
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
    all_lecturer = []
    courses_in_progress = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}
        Lecturer.all_lecturer.append(self)

    def __str__(self):
        return f"Лектор\n Имя: {self.name}\n Фамилия: {self.surname}\n " \
               f"Средняя оценка за курсы: {self.average_grade_lecturs()}\n " \
               f"Препадает на курсах: {', '.join(self.courses_in_progress)}"

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка! Сравнение двух объектов разных классов!"
        if self.average_grade_lecturs() == other.average_grade_lecturs():
            return f" Средняя оценка лектора {self.name} {self.surname} " \
                   f"равна средней оценке лектора {other.name} " \
                   f"{other.surname}"
        else:
            return f" Средняя оценка лектора {self.name} {self.surname}" \
                   f" не равна средней оценке лектора " \
                   f"{other.name} {other.surname}"

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка! Сравнение двух объектов разных классов!"
        if self.average_grade_lecturs() <= other.average_grade_lecturs():
            return f" Средняя оценка лектора {self.name} {self.surname} " \
                   f"меньше или равна средней оценке лектора {other.name} {other.surname}"
        else:
            return f" Средняя оценка лектора {self.name} {self.surname} " \
                   f"больше средней оценке лектора {other.name} {other.surname}"

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка! Сравнение двух объектов разных классов!"
        if self.average_grade_lecturs() > other.average_grade_lecturs():
            return f" Средняя оценка лектора {self.name} {self.surname} " \
                   f"больше или равна средней оценке лектора {other.name} {other.surname}"

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)
        Lecturer.courses_in_progress += self.courses_in_progress

    def average_grade_lecturs(self):
        average_for_lecturs = []
        if not self.grades:
            return 0
        for i in self.grades.values():
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
        if isinstance(student, Student) and course in self.courses_attached and course in Student.courses_in_progress:
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
student_1.add_courses_in_progress("Django")
# Добовляем студенту еще законченый курс.
student_1.add_finished_courses("Введение в программирование")
student_1.add_finished_courses("CSS")

# Создаем экземпляр student_2 класса Student.
student_2 = Student('Саша', 'Александров', 'M')
# Добавляем студенту изучаемый курс.
student_2.add_courses_in_progress("Python")
student_2.add_courses_in_progress("Git")
student_2.add_courses_in_progress("JS")
student_2.add_courses_in_progress("Django")
# Добовляем студенту еще законченый курс.
student_2.add_finished_courses("Введение в программирование")
student_2.add_finished_courses("HTML")

# Создаем экземпляр lecturer_1 класса Lecturer.
lecturer_1 = Lecturer("Николай", "Николаев")
# Добавляем лектору читаемый курс.
lecturer_1.add_courses("Git")
lecturer_1.add_courses("Python")
lecturer_1.add_courses("Django")
lecturer_1.add_courses("JS")

# Создаем экземпляр lecturer_2 класса Lecturer.
lecturer_2 = Lecturer("Олег", "Олегов")
# Добавляем лектору читаемый курс.
lecturer_2.add_courses("Python")
lecturer_2.add_courses("Django")
lecturer_2.add_courses("Git")
lecturer_2.add_courses("JS")

# Создаем экземпляр reviewer_1 класса Reviewer.
reviewer_1 = Reviewer("Виктор", "Викторов")
# Добовляем курсы которые проверяет reviewer_1.
reviewer_1.courses_attached.append("Python")
reviewer_1.courses_attached.append("Git")
reviewer_1.courses_attached.append("Django")
reviewer_1.courses_attached.append("JS")

# Создаем экземпляр reviewer_2 класса Reviewer.
reviewer_2 = Reviewer("Павел", "Павлов")
# Добовляем курсы которые проверяет reviewer_1.
reviewer_2.courses_attached.append("Git")
reviewer_2.courses_attached.append("JS")
reviewer_2.courses_attached.append("Django")

# От reviewer_1 студенту student_1 по опр.курсу ставим отметку.
reviewer_1.rate_student(student_1, "JS", 10)
reviewer_1.rate_student(student_1, "Git", 4)
reviewer_1.rate_student(student_1, "Python", 5)
# От reviewer_1 студенту student_2 по опр.курсу Python ставим отметку.
reviewer_1.rate_student(student_2, "JS", 6)
reviewer_1.rate_student(student_2, "Git", 8)
# От reviewer_2 студенту student_1 по опр.курсу ставим отметку.
reviewer_2.rate_student(student_1, "Django", 5)
# От reviewer_2 студенту student_2 по опр.курсу Git ставим отметку.
reviewer_2.rate_student(student_2, "Django", 10)

# От student_1 выставляем оценку lecturer_1.
student_1.rate_lecturer(lecturer_1, "Git", 10)
student_2.rate_lecturer(lecturer_1, "Django", 10)
student_1.rate_lecturer(lecturer_1, "Python", 10)
# От student_1 выставляем оценку lecturer_2.
student_1.rate_lecturer(lecturer_2, "Django", 5)
student_1.rate_lecturer(lecturer_2, "Git", 10)
# От student_2 выставляем оценку lecturer_1.
student_2.rate_lecturer(lecturer_1, "Git", 7)
student_2.rate_lecturer(lecturer_1, "Django", 2)
# От student_1 выставляем оценку lecturer_2.
student_2.rate_lecturer(lecturer_2, "Python", 5)

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
    existence_course = 0
    name_1 = ""
    result = 0
    if not isinstance(persons, list):
        return "Not list"
    if course in Student.courses_in_progress and course in Lecturer.courses_in_progress:
        existence_course += 1
        for person in persons:
            if course in person.grades:
                for key_dic, Value_dic in person.grades.items():
                    if course == key_dic:
                        list_grades += Value_dic
            if isinstance(person, Student):
                name_1 = "за домашние задания по всем студентам"
            else:
                name_1 = "за лекции всех лекторов"
        if len(list_grades) != 0:
            result = round(sum(list_grades) / len(list_grades), 2)
            return f"Средняя оценка {name_1} за курс {course}: {result}"
        else:
            # result == 0 and existence_course == 1:
            return f"По курсу {course} ни у кого оценок нет!"
    else:
        return f"Курс {course} не найден!!!"


print('-' * 25)
# Средняя оценка по всем студентам курса (созданным объектам) за выбранный курс.
print(average_rating(Student.all_students, 'Python'))
print(average_rating(Student.all_students, 'Git'))
print(average_rating(Student.all_students, 'JS'))
print(average_rating(Student.all_students, 'Django'))
print(average_rating(Student.all_students, 'WEB3'))

print('-' * 25)
# Средняя оценка по всем лекторам курса (созданным объектам) за выбранный курс.
print(average_rating(Lecturer.all_lecturer, 'Django'))
print(average_rating(Lecturer.all_lecturer, 'Python'))
print(average_rating(Lecturer.all_lecturer, 'Git'))
print(average_rating(Lecturer.all_lecturer, 'WEB4'))
#
print('-' * 25)
# Проверка на равенства между собой студентов по средней оценке за домашние задания.
print(student_1 == student_2)
print(student_1 <= student_2)
print(student_1 > student_1)

print('-' * 25)
# Проверка на равенства между собой лекторов по средней оценке за лекции.
print(lecturer_1 == lecturer_2)
print(lecturer_1 <= lecturer_2)
print(lecturer_1 > lecturer_2)
