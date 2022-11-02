import os, sys
# -*- coding: utf8 -*-

cook_book = {}
with open('recipes.txt', 'r') as f:
    key_list = ['ingredient_name', 'quantity', 'measure']
    ingredients = {}
    items = []
    len_items = 0
    dish = True
    while dish:
        all_list_ingr_dic = list()
        srt_line = f.readline()
        number = int(f.readline())
        ingredient_item = True
        while ingredient_item:
            line = f.readline().split('|')
            len_items += 1
            for item in line:
                if item == str():
                    break
                elif item == '\n':
                    ingredient_item = False
                    break
                else:
                    items.append(item)
            if ingredient_item == False or item == str():
                break
            else:
                ingredients = zip(key_list, items)
                items.clear()
                all_list_ingr_dic.append(ingredients)
            cook_book[srt_line] = all_list_ingr_dic
        if item == str():
            dish = False


    print(cook_book)


    print('\n', f.readline(30))
