def make_eggs():
    print("Яичница пожарена")


def make_bacon():
    print("Бекон пожарен")

# print(make_eggs())
# make_eggs()
# print(make_bacon)

# my_functions = {
#     "eggs": make_eggs,
#     "bacon": make_bacon
# }
#
# answer = input("Введите команду: ")
# my_functions[answer]()


# class Crate:
#     def __init__(self, stuff):
#         self.stuff = stuff
#
#     def get_stuff(self):
#         return self.stuff


crate_1 = [1, 2, 3]
crate_2 = ["a", "b", "c"]


class Locket:

    total_created_lockets = 0

    def __init__(self, height, length, depth, color, crate_collection):
        """Инициализируем поля экземпляра класса"""
        self.height = height
        self.length = length
        self.depth = depth
        self.color = color
        self.crate_collection = crate_collection
        Locket.total_created_lockets += 1

    def get_volume(self):
        """Это метод класса, который работает с конкретным экземпляром этого класса"""
        return self.height * self.length * self.depth

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def set_color(self, color):
        prev_color = self.color
        self.color = color
        print(f"Новый цвет задан: {color}. Предыдущий цвет: {prev_color}")

    def show_all_crates(self):
        for crate in self.crate_collection:
            print(crate.get_stuff())


# crate_1 = Crate([1, 2, 3, 4])
# crate_2 = Crate(["a", "b", "c", "d"])
# locket_1 = Locket(height=100, length=10, depth=50, color="red", crate_collection=[crate_1, crate_2])
# locket_1.show_all_crates()
#


# print(locket_1.color)
# locket_2 = Locket(height=10, length=10, depth=10)

# print(Locket)
# print(locket_1)
# print(locket_1.depth, locket_1.length, locket_1.height)
# print(locket_1.get_volume())
# print(locket_2.get_volume())

# from random import randint
#
# locket_collection = [Locket(height=randint(1, 15),
#                             length=randint(1, 15),
#                             depth=randint(1, 15)) for locket in range(randint(0, 15))]


# def get_total_locket_cnt():
#     print("Общее количество созданных шкатулок за всё время работы программы:", Locket.total_created_lockets)
#
#
# for locket in locket_collection:
#     print("Объем очередной шкатулки равен:", locket.get_volume())
#
# get_total_locket_cnt()
