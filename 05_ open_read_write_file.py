import os, sys
# -*- coding: utf8 -*-

cook_book = {}
with open('recipes.txt', 'r') as f:
    key_list = ['ingredient_name', 'quantity', 'measure']
    srt_line = f.readline()
    print(srt_line)
    number = int(f.readline())
    # print(number)
    ingredients = {}
    items = []
    all_list_ingr_dic = list()
    len_items = 0
    a = True
    while a:
        line = f.readline().split('|')
        len_items += 1
        for item in line:
            if item != ''+'\n':
                # print(item)
                items.append(item)
            else:
                # break
                a = False
        if items == []:
            # break
            a = False
        else:
            ingredients = zip(key_list, items)
            items.clear()
            all_list_ingr_dic.append(ingredients)

    cook_book[srt_line] = all_list_ingr_dic


    # print(items)
    # print(len_items)


    print(ingredients)
    print(all_list_ingr_dic)
    print(cook_book)



    # for srt_line in f.readline():
    #     dish_name = srt_line
    #     print(dish_name)

#
#
#
#
#         print(dish_name)
#         ingredients = srt_line.split(sep='|')
#
#         for i in srt_line:
#             # print(i)
#             all_list_ingr_dic = zip(key_list, i)
# print(dict(all_list_ingr_dic))


        # if f.readline() == int():
        #     pass

        # if f.readline() == '\n':
        #     a = False
        # else:
        #     name = f.readline(30)
        #     print(name)
        #     length = f.readline(5)
        #     a = False

            # def ingredient():
            #     ingredients = {}
            #     string = f.readline()
            #     if string == '\n':
            #         a = False
            #     else:
            #         list_ing = string.split(sep='|')
            #         for i in list_ing:
            #             ingredients = zip(key_list, list_ing)
            #     return ingredients


            # ingredient()
            # print(ingredient())

    # string = f.readline()
    # if string == '\n':
    #     a = False
    # else:
    #     list_ing = string.split(sep='|')
    #     for i in list_ing:
    #         ingredients = zip(key_list, list_ing)
    # print(dict(ingredients))

# all_list_dic[name] = ingredients
# print(dict(all_list_dic))


# print('\n', f.readline(30))
