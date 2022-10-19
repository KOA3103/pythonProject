# vector_1 = [0, 1]
# vector_2 = [1, 5]


# def mod_vect(vector: list) -> float:
#     return round((((vector[0]**2)+(vector[1])**2)**0.5), 2)

# \nКоордината z: {vector[2]}


# def get_vector_info(vector: list) -> str:
#     return f"Координата х: {vector[0]} \nКоордината y: {vector[1]}"
#
#
# print(get_vector_info(vector_1))
# print(mod_vect(vector=vector_1))

class Vector2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def mod_vect(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return f"Координата х: {self.x} \nКоордината y: {self.y}"

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        if isinstance(self, Vector2D):
            return Vector2D(x=self.x + other.x, y=self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y


vect_1 = Vector2D(1, 2)
vect_2 = Vector2D(3, 4)
vect_3 = vect_1 + vect_2 + vect_1 + vect_2
print(vect_3)
print(vect_1 == vect_1)
print(vect_3 <= vect_1)



# class Vector3D:
#     def __init__(self, x: int, y: int, z: int):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def mod_vect(self):
#         return ((self.x ** 2) + (self.y ** 2) + (self.z**2)) ** 0.5
#
#     def __str__(self):
#         return f"Координата х: {self.x} \nКоордината y: {self.y} \nКоордината z: {self.z}"
#
# vect_data = [1, 5]
#
# vector2d = Vector2D(x=1, y=5) # создаем экземпляр класса vector с заданными параметпами
#
# прокидываеи методы в параметры
# print(vector2d)
# print(vector2d.mod_vect())
#
# vector3d = Vector3D(1, 2, 3)
#
# print(vector3d)
# print(vector3d.mod_vect())


# v = Vector(*vector_2)
# print(v.get_vector_info())
# print(v.mod_vect())
# print(isinstance(v, Vector))
#

# vect_data = [1, 5]
# vect_data_dict = {"x": 1, "y": 5}
#
# vector = Vector(vect_data[0], vect_data[1])
# vector_1 = Vector(*vect_data)
# vector_2 = Vector(**vect_data_dict)
# # vector = Vector(x=1, y=5)
#
# print(vector.get_vector_info())
#
# print(vector_2.mod_vect())
