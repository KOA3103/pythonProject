class What_type:
    def __init__(self, any_object):
        self.any_object = any_object
        list_of_types = (int, float, str, list, dict, set, tuple)
        for i in list_of_types:
            if isinstance(any_object, i):
                print(f"Object {any_object} is {i}")

    def __len__(self): # возвращает колличество символов в классе
        return len(self.any_object)

a = What_type(("hi mom"))

print(len(a))


# def determin_class(object):
#     list_of_types = (int, float, str, list, dict, set, tuple)
#     for i in list_of_types:
#         if isinstance(object, i):
#             print(object, 'is', i)