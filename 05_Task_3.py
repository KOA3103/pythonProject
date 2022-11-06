import os
from pathlib import Path

# Берем файлы из директории.
source_path = os.path.join(Path.cwd())
# Созданный файл помещаем в дирекиторию, под именем 'united_file_name.txt'.
target_path = os.path.join(Path.cwd(), 'united_file_name.txt')


def gets_files_for_analysis(source_path=Path.cwd()):
    list_all_files = list()
    files_in_queue = list(Path(source_path).glob('?.txt'))  # '*'-все файлы, '?'-файл с названием в один символ.
    for file_name in files_in_queue:
        list_file = list()
        with open(file_name.name, 'r', encoding='utf-8') as file:
            file = file.readlines()
            list_file.append(len(file))
            list_file.append([file_name.name])
            list_file.append(file)
            list_all_files.append(list_file)
    list_all_files = sorted(list_all_files)
    return list_all_files


with open(target_path, 'w', encoding='utf-8') as united_file:
    for _ in gets_files_for_analysis(source_path):
        articles = ''
        file_name = _[1][0]
        quantity_of_strings = _[0]
        for _i in _[2]:
            articles += _i
        united_file.write(f'\n{file_name}\n{quantity_of_strings}\n{articles}\n')
        print(f'\n{file_name}\n{quantity_of_strings}\n{articles}')

print(f'Файлы были взяты из директории => {source_path}')
print(f'Созданный файл был помещен в дирекиторию => {target_path}')
