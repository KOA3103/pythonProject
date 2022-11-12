# Показ текущей директории.
import os
# print("Current Work Directory =>:", os.getcwd())
from pathlib import Path
# print("Current Work Directory:", Path.cwd())

# 1. Создаём новую директорию в текущей.
# os.mkdir("1.txt")
# os.mkdir("2.txt")
# os.mkdir("3.txt")
# print("Is the directory there:", os.path.exists("test_folder"))
# 1.1 Создаём новую директорию в конкретно заданном каталоге
# os.mkdir(r"C:\Users\KOA\Documents\CRYPTO")
# print("Is the directory there:", os.path.exists(r"C:\Users\KOA\Documents\CRYPTO"))
# 1.2 Создать новую директорию с несколькими вложенными уровнями (имеется в виду наличие одной папки внутри другой).
# os.makedirs('test_folder_1/folder1_1')
# print("Is the directory there:", os.path.exists("test_folder_1/folder1_1"))
# 1.3 Используем pathlib.
# Path("test_folder_2/folder2_1").mkdir(parents=True, exist_ok=True)

# 2. Создание и запись новых данных в созданный файл.
# for files in range(3):
    # print(files)
    # file_name = str(files) + '.txt'
#     # 2.1 Создание файла.
#     with open(f"test_folder_2/folder2_1/{file_name}", 'w') as f:
#     with open(file_name, 'w') as f:
#         text_to_write = f"file {file_name} - Hello Files From Writing"
        # f.write(text_to_write)
        # print(f"* After creating file {os.path.exists('test_folder_2/folder2_1/hello3.txt')}")


# 3.1 Удаление файла. При использовании модуля pathlib за удаление файла отвечает метод unlink(),
# а за удаление директории — rmdir(). Обратите внимание, что они оба являются методами экземпляра объекта Path.
# print(f"* Before deleting file {os.path.isfile('test_folder_2/folder2_1/hello3.txt')}")
# os.remove('test_folder_2/folder2_1/hello3.txt')
# os.unlink('test_folder_1/folder1_1/hello3.txt')
# print(f"* After deleting file {os.path.exists('test_folder_1/folder1_1/hello3.txt')}")

# 3.2 Удаление директории
# print(f"* Before deleting directory {os.path.isdir('test_folder_3/folder3_3')}")
# os.rmdir('test_folder_3/folder3_3')
# os.remove('test_folder_2/folder2_1/hello3.txt')
# os.rmdir('test_folder_2/folder2_1')
# print(f"* After deleting directory {os.path.exists('test_folder_3/folder3_3')}")

# 4. Получение списка файлов.
# List_files = list(Path('test_folder_2/folder2_1').glob("*.txt"))
# print("Список файлов: ", List_files)
# Как вариант, также удобно использовать модуль glob напрямую.
# from glob import glob
# files = list(glob('t*'))
# print("Files starting with t:", files)

# upload_folder. Перемещение.
# target_folder = Path("test_folder_0")
# target_folder.mkdir(parents=True,exist_ok=True)
# source_folder = Path('target_folder')
#
# txt_files = source_folder.glob('*.txt')
# for txt_file in txt_files:
#     filename = txt_file.name
#     target_path = target_folder.joinpath(filename)
#     print(f"** Moving file {filename}")
#     print("Target File Exists:", target_path.exists())
#     txt_file.rename(target_path)
#     print("Target File Exists:", target_path.exists(), '\n')
#
# 6. Копирование файлов.
# import shutil
#
# source_file = "test_folder_0/upload_folder"
# target_file = "test_folder_1/folder1_1/upload_folder"
# target_file_path = Path(target_file)
# print("* Before copying, file exists:", target_file_path.exists())
# shutil.copy(source_file, target_file)
# print("* After copying, file exists:", target_file_path.exists())
#
# 7. Проверка директории или файла
# exists() в модуле os
# print(os.path.exists('test_folder_1/folder1_1/upload_folder'))
# 7.1 эта функция доступна в обоих модулях, os и pathlib, но с разными сигнатурами.
# exists() в модуле pathlib
# print(Path('test_folder_1/folder1_1/upload_folder').exists())

# 7.2 Проверяем, является ли путь директорией.
# print(os.path.isdir('test_folder_1/folder1_1'))
# print(Path('test_folder_1/folder1_1').is_dir())

# 7.3 Проверяем, является ли путь файлом.
# print(os.path.isfile('test_folder_1/folder1_1'))
# print(Path('test_folder_1/folder1_1/upload_folder').is_file())

# 8.1 Получение информации о файле.
for py_file in Path(r'/pythonProject/upload_folder').glob('*.txt'):
    print('Name with extension:', py_file.name)
    print('Name only:', py_file.stem)
# # 8.2 Узнать расширение файла.
#     file_path = Path(py_file.name)
#     print("File Extension:", file_path.suffix)

# 8.3 Больше информации о файле, его размер и время изменения.
# 8.3.1 Получаем объект st_stat из пути.
# current_file_path = Path('test_folder_1/folder1_1/upload_folder')
# file_stat = current_file_path.stat()
# 8.3.2 Получаем информацию о размере файла:
# print("File Size in Bytes:", file_stat.st_size)
# Получаем информацию о времени последнего обращения
# print("When Most Recent Access:", file_stat.st_atime)
# Получаем информацию о времени последнего изменения содержимого
# print("When Most Recent Modification:", file_stat.st_mtime)

# 9 Чтение файлов
# 9.1 Чтение всего файла, его текстов.
# with open("test_folder_1/folder1_1/upload_folder", 'r') as file:
#     print(file.read())
# 9.2 Чтение построчно
# with open("test_folder_1/folder1_1/upload_folder", 'r') as file:
#     for i, line in enumerate(file, 2):
#         print(f"* Reading line № {i}: {line}")


# Шаг 1 - Открыть файл
# file = open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\upload_folder')
# print(type(file), "\n")

# Шаг 2 - Создем переменную data, читаем файл целиком, метод .read().
# data = file.read()
# print(data)
# print(type(data), "\n")

# Шаг 3 - Закрыть файл
# file.close()

# Проверим остались ли данные в памяти
# print(f"То что у нас в памяти - {data}")


# def is_closed_or_not(file_):
#     """
#     Функция принимает объект файл и проверяет его состояние
#     """
#     if file_.closed:
#         print('Файл закрыт')
#     else:
#         print('Файл открыт')
#

# Эквивалентно
# f = open("data.txt") == with open("data.txt") as f


# Пример 1 - Открыть файл, прочитать, закрыть автоматом - with.
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\upload_folder', encoding="utf-8") as f:
#     print(type(f))
#     data = f.read(10)
#     data_2 = f.read(15)
#     is_closed_or_not(f)
#     print(data)
#     print(data_2)
#     print(data[:9])
#     print(data[2:7])

# is_closed_or_not(f)

# Обработка исключений, ZeroDivisionError: division by zero.
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\upload_folder', encoding="utf-8") as f:
# data = f.read()
# is_closed_or_not(f)
# 1 / 0

# Обработка исключений.
# try:
#     with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\upload_folder', encoding="utf-8") as f:
#         data = f.read()
#         is_closed_or_not(f)
#         1 / 0
# except ZeroDivisionError:
#     is_closed_or_not(f)

# Запись в файл.
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\12.txt', "w", encoding="utf-8") as f:
#     f.write("1. Python is cool!\n")
#     f.write("2. I love Python\n")
#     f.write("3. I'm a reach man.")
#     is_closed_or_not(f)
# is_closed_or_not(f)

# Дополнить файл
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\12.txt', "a", encoding="utf-8") as f:
#     data = "\n123456789\n"
#     data_2 = "!@#$%^&*()_+"
#     f.write(data)
#     f.write(data_2)

# Дополнить файл
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\12.txt', "r", encoding="utf-8") as f:
#     lines = f.readline()
#     print(lines)
#     lines = f.readlines()
#     print(lines)

# Запись в файл спмска построчно.
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\123.txt', "w", encoding="utf-8") as f:
#     lines = ["1.First", "\n2.Second", "\n3.Third"]
#     f.writelines(lines)
#     print(lines)

# Пример 1 - читаем файл целиком
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\12.txt') as f:
#     data = f.read()
#     print(type(data))
#     print(data)


# Пример 2 - читаем построчно
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\12.txt') as f:
    # print(f.readline().strip())
    # print(f.readline().strip())
    # print(f.readline().strip())
    # print(f.readline() != "")
    # print(f.readline() is None)


# Пример 3 - читаем строки (все) - читается все,  но записывается в список
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\12.txt') as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(len(lines))
#     print(lines[1])


# Пример 4 - читаем итеративно
# with open(r'C:\Users\KOA\PycharmProjects\pythonProject\test_folder_1\folder1_1\12.txt') as f:
#     for line in f:
#         print(line.strip())

# Пример 1 - попытка записать в файл который открыт только на чтение (io.UnsupportedOperation: not writable).
# with open('test_folder_1/folder1_1/hello3.txt') as f:
#     f.write('Привет, мир!')

# Пример 2 - попытка записать в файл который открыт на запись
# with open('test_folder_1/folder1_1/hello3.txt', "w") as f:
#     f.write('Привет, мир!')

# Пример 3 - попытка прочитать в файл который открыт на запись (io.UnsupportedOperation: not readable).
# with open('test_folder_1/folder1_1/hello3.txt', 'w') as f:
#     print(f.read())

# Пример 4 - попытка прочитать в файл который открыт на запись И чтение. wr
# with open('data_3.txt', 'wr') as f:
#     # Ошибка (ValueError: must have exactly one of create/read/write/append mode).
#     print(f.read())

# Пример upload_folder - попытка записать две строки но в разных сессиях в файл который открыт на запись.
# with open('test_folder_1/folder1_1/hello3.txt', 'w') as f:
#     f.write('Первая строка!')
# with open('test_folder_1/folder1_1/hello3.txt', 'w') as f:
#     f.write('Вторая строка!')

#  Пример 6 - Дозапись файла
# with open('test_folder_1/folder1_1/hello3.txt', 'a') as f:
#     f.write('Первая строка! \n')
# with open('test_folder_1/folder1_1/hello3.txt', 'a') as f:
#     f.write('Вторая строка! \n')

# Пример upload_folder - Битовое чтение
# with open('test_folder_1/folder1_1/hello3.txt', 'rb') as f:
#     data = f.read()
#     print(type(data))
#     print(data)


# Пример 6 - Битовая чтение строки
# with open('test_folder_1/folder1_1/hello3.txt', 'rb') as f:
#     print(f.readline())


# Пример 1 - получение пути от корня файловой системы к текущему каталогу
# print("\nПример 1 - получение пути от корня файловой системы к текущему каталогу")
# print("==> ", os.getcwd())

# Пример 2 - построение пути к файлу
# print("\nПример 2 - построение пути к файлу")
# file_path = os.path.join(os.getcwd(), 'd%^^^^^^H')
# print("==> ", file_path)

# # Пример 3 - Запись и чтение в файл без указания пути (относительный путь - т.к. относительно текущей директории)
# with open('test.txt', 'w') as f:
#     f.write(f'{time.time()}')
# with open('test.txt', 'r') as f:
#     print(f.read())

# Пример 4 - Запись и чтение в файл с указание пути (абсолютный путь)
# file_path = os.path.join(os.ge

# Пример upload_folder - Вложенный with, пока менеджер контекста не закрыт, мы не может получить результат работы над файлом
# with open('file.txt', 'w') as f:
#     f.write('898-999-998-223')
#     with open('file.txt') as f1:
#         print(f1.read())
# with open('file.txt') as f1:
#     print(f1.read())

# Пример 1 - Записываем файл в кодировке utf-8 (linux)
# with open('utf.txt', 'w', encoding='utf-8') as f:
#     f.write('Привет, мир!')

# Пример 2 - Записываем файл в кодировке cp1251 (windows)
# with open('cp.txt', 'w', encoding='cp1251') as f:
#     f.write('Привет, мир!')

# Пример 3 - Читаем файлы в байтах чтобы показать разницу в кодировках
# with open('cp.txt', 'rb') as f:
#     print("cp1251 ==> ", f.read())
# with open('utf.txt', 'rb') as f:
#     print("utf-8 ==> ", f.read())

# Пример 4 - Чтение файла с указанием неверной кодировки
# with open('cp.txt', 'r') as f:
#     print(f.read())

# Пример upload_folder - Чтение файла с указанием верной кодировки
# with open('cp.txt', 'r', encoding='cp1251') as f:
# print(f.read())
