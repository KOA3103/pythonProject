import os

def united_file_write(file_name, file):
    united_file.write(file_name + '\n')
    united_file.write(str(len(file)) + '\n')
    united_file.writelines(file)
    united_file.write('\n')
    return

united_file_name = "rewrite_file.txt"
with open('1.txt', 'r', encoding='utf-8') as f1:
    file1 = f1.readlines()
with open('2.txt', 'r', encoding='utf-8') as f2:
    file2 = f2.readlines()
with open('3.txt', 'r', encoding='utf-8') as f3:
    file3 = f3.readlines()
with open('united_file_name.txt', 'w', encoding='utf-8') as united_file:
    if len(file1) < len(file2) < len(file3):
        united_file_write('1.txt', file1)
        united_file_write('2.txt', file2)
        united_file_write('3.txt', file3)

    elif len(file1) < len(file3) < len(file2):
        united_file_write('1.txt', file1)
        united_file_write('3.txt', file3)
        united_file_write('2.txt', file2)

    elif len(file2) < len(file1) < len(file3):
        united_file_write('2.txt', file2)
        united_file_write('1.txt', file1)
        united_file_write('3.txt', file3)

    elif len(file2) < len(file3) < len(file1):
        united_file_write('2.txt', file2)
        united_file_write('3.txt', file3)
        united_file_write('1.txt', file1)

    elif len(file3) < len(file1) < len(file2):
        united_file_write('3.txt', file3)
        united_file_write('1.txt', file1)
        united_file_write('2.txt', file2)

    elif len(file3) < len(file2) < len(file1):
        united_file_write('3.txt', file3)
        united_file_write('2.txt', file2)
        united_file_write('1.txt', file1)

