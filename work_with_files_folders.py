# Показ текущей директории.
import os
print("Current Work Directory =>:", os.getcwd())
from pathlib import Path
print("Current Work Directory:", Path.cwd())

# 1. Создаём новую директорию в текущей.
# os.mkdir("test_folder_0")
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
# for files in range(6):
#     # print(files)
#     file_name = "file_"+str(files) + '.txt'
#     # 2.1 Создание файла.
#     with open(f"test_folder_2/folder2_1/{file_name}", 'w') as f:
#         text_to_write = f"file {file_name} - Hello Files From Writing"
#         f.write(text_to_write)
#         print(f"* After creating file {os.path.exists('test_folder_2/folder2_1/hello3.txt')}")


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

# 5. Перемещение.
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

# 6. Копирование файлов.
# import shutil
#
# source_file = "test_folder_0/5.txt"
# target_file = "test_folder_1/folder1_1/5.txt"
# target_file_path = Path(target_file)
# print("* Before copying, file exists:", target_file_path.exists())
# shutil.copy(source_file, target_file)
# print("* After copying, file exists:", target_file_path.exists())

# 7. Проверка директории или файла
# exists() в модуле os
# print(os.path.exists('test_folder_1/folder1_1/5.txt'))
# 7.1 эта функция доступна в обоих модулях, os и pathlib, но с разными сигнатурами.
# exists() в модуле pathlib
# print(Path('test_folder_1/folder1_1/5.txt').exists())

# 7.2 Проверяем, является ли путь директорией.
# print(os.path.isdir('test_folder_1/folder1_1'))
# print(Path('test_folder_1/folder1_1').is_dir())

# 7.3 Проверяем, является ли путь файлом.
# print(os.path.isfile('test_folder_1/folder1_1'))
# print(Path('test_folder_1/folder1_1/5.txt').is_file())

# 8.1 Получение информации о файле.
# for py_file in Path("test_folder_1/folder1_1").glob('*.txt'):
#     print('Name with extension:', py_file.name)
#     print('Name only:', py_file.stem)
# # 8.2 Узнать расширение файла.
#     file_path = Path(py_file.name)
#     print("File Extension:", file_path.suffix)

# 8.3 Больше информации о файле, его размер и время изменения.
# 8.3.1 Получаем объект st_stat из пути.
# current_file_path = Path('test_folder_1/folder1_1/5.txt')
# file_stat = current_file_path.stat()
# 8.3.2 Получаем информацию о размере файла:
# print("File Size in Bytes:", file_stat.st_size)
# Получаем информацию о времени последнего обращения
# print("When Most Recent Access:", file_stat.st_atime)
# Получаем информацию о времени последнего изменения содержимого
# print("When Most Recent Modification:", file_stat.st_mtime)

# 9 Чтение файлов
# 9.1 Чтение всех текстов
with open("test_folder_1/folder1_1/5.txt", 'r') as file:
    print(file.read())
# 9.2 Чтение построчно
with open("test_folder_1/folder1_1/5.txt", 'r') as file:
    for i, line in enumerate(file, 2):
        print(f"* Reading line № {i}: {line}")