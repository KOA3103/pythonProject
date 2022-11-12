# Сортировать список с помощью встроенного в sorted() функцию или встроенный в  list.sort() метод.
# Функция sorted() создает новый отсортированный список.



# numbers = [(3, 14), (1, 61), (2, 71)]
# numbers.sort(key=lambda k: k[0])
# print('Sorted list:', numbers)


def custom_key(people):
    return people[1] # second parameter denotes the age

persons = [['Alice', 26, 'F'], ['Trudy', 25, 'M'], ['Bob', 25, 'M'], ['Alexa', 22, 'F']]
print(f'Before sorting: {persons}')
persons.sort(key=custom_key)
print(f'After sorting: {persons}')
