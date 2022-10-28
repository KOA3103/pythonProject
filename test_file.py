def mean(numbers):
    if numbers:
        if isinstance(numbers, dict):
            res=[]
            for value in numbers.values():
                res += value
            return sum(res)/len(res)
        else:
            return sum(numbers)/len(numbers)
    else:
        return 0

def courses_rating(persons, course):
    res = 0
    lenth = 0
    for person in persons:
        if course in person.grades:
            if person.grades[course]:
                res += mean(person.grades[course])
                lenth += 1
    if lenth != 0:
        return res/lenth

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
            if isinstance(grade, int) and (0 <= grade <= 10) :
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print("Оценка введена неверно")
        else:
            return 'Ошибка'
    def __str__(self):
        info = str(f"Имя: {self.name}\n"
                   f"Фамилия: {self.surname}\n"
                   f"Средняя оценка: {mean(self.grades)}\n"
                   f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
                   f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
        return info
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {mean(self.grades)}"
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

Students = [Student('Ruoy', 'Eman', 'your_gender'),
            Student('Ron', 'Wuizli', 'your_gender')]
Students[0].courses_in_progress += ['Python']
Students[0].courses_in_progress += ['Git']
Students[0].finished_courses += ['Introduction to the programming']
Students[1].courses_in_progress += ['Python']
Students[1].finished_courses += ['Paint']
Students[1].finished_courses += ['Calculator']

Lecturers = [Lecturer('Leps', 'Grisha'),
             Lecturer('Jigurda', 'Nikita')]
Lecturers[0].courses_attached += ['Python']
Lecturers[0].courses_attached += ['Java']
Lecturers[1].courses_attached += ['JS']

Reviewers = [Reviewer('Nikolaev', 'Igor'),
             Reviewer('Baskov', 'Nikolay')]
Reviewers[0].courses_attached += ['Python']
Reviewers[0].courses_attached += ['Git']
Reviewers[1].courses_attached += ['Python']
Reviewers[1].courses_attached += ['JS']

Reviewers[0].rate_hw(Students[0], 'Python', 8)
Reviewers[0].rate_hw(Students[0], 'Python', 9)
Reviewers[0].rate_hw(Students[0], 'Git', 10)
Reviewers[0].rate_hw(Students[1], 'Python', 10)
Reviewers[1].rate_hw(Students[1], 'Python', 6)

Students[0].rate_lecturer(Lecturers[0], 'Python', 10)
Students[0].rate_lecturer(Lecturers[0], 'Python', 9)
Students[1].rate_lecturer(Lecturers[0], 'Python', 8)
Students[1].rate_lecturer(Lecturers[1], 'JS', 7)

print(f"Reviewers[0]:\n{Reviewers[0]}\n")
print(f"Lecturers[0]:\n{Lecturers[0]}\n")
print(f"Lecturers[1]:\n{Lecturers[1]}\n")
print(f"Students[0]:\n{Students[0]}\n")
print(f"Students[1]:\n{Students[1]}\n")

print("Lecturers[0] < Lecturers[1] ==>", Lecturers[0] > Lecturers[1])
print("Students[0] > Students[1] ==>", Students[0] > Students[1])

print(f"\nСредняя оценка домашних работ по Python: {courses_rating(Students, 'Python')}")
print(f"Средняя оценка лекторов по курсу Python: {courses_rating(Lecturers, 'Python')}")