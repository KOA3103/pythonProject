# -*- coding: utf-8 -*-
import os
import time
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = {}
with open(file_path, 'r') as f:
  key_list = ['ingredient_name', 'quantity', 'measure']
  items = []
  dish = True
  while dish:
    all_list_ingr_dic = list()
    dish_name = ''
    str_line = f.readline()
    for name in str_line:
      if name == '\n':
        break
      else:
        dish_name += name
    number = int(f.readline())
    ingredient_item = True
    while ingredient_item:
      ingredients = {}
      line = f.readline().split('|')
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
        ingredients['ingredient_name'], ingredients['quantity'], ingredients[
          'measure'] = items
        ingredients['quantity'] = int(ingredients['quantity'])
        items.clear()
        all_list_ingr_dic.append(ingredients)
      cook_book[dish_name] = all_list_ingr_dic
    if item == str():
      dish = False

pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
  ingredient_list = dict()
  for dish_name in dishes:
    if dish_name in cook_book:
      for ingredient in cook_book[dish_name]:
        measure_quantity = dict()
        if ingredient['ingredient_name'] not in ingredient_list:
          measure_quantity['measure'] = ingredient['measure']
          measure_quantity['quantity'] = ingredient['quantity'] * person_count
          ingredient_list[ingredient['ingredient_name']] = measure_quantity
        else:
          ingredient_list[ingredient['ingredient_name']]['quantity'] = \
          ingredient_list[ingredient['ingredient_name']]['quantity'] + \
          ingredient['quantity'] * person_count

    else:
      return f'{dish_name} нет в списке блюд!'
  return ingredient_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
