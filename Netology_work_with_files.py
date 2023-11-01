cook_book = {}
check_list_int = list(range(10))
check_list_str = [str(i) for i in check_list_int]
with open('recipes.txt', encoding='utf-8') as f:
    while True:
        recipe_dict = {}
        line_ = f.readline()
        line = line_.strip()
        if not line_:
            break
        elif line == '':
            continue
        elif line not in check_list_str and '|' not in line:
            dish = line
            cook_book.setdefault(dish, [])
        elif '|' in line:
            recipe_list = line.split(' | ')
            recipe_dict['ingredient_name'] = recipe_list[0]
            recipe_dict['quantity'] = recipe_list[1]
            recipe_dict['measure'] = recipe_list[2]
            cook_book[dish].append(recipe_dict)
print(cook_book)



# cook_book = {
#     'Омлет': [
#         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#     'Утка по-пекински': [
#         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#     'Запеченный картофель': [
#         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
# }


# Backup
# with open('recipes.txt', encoding='utf-8') as f:
#     while True:
#         line = f.readline()
#         ingredients_line = []
#         if not line:
#             break
#         for number in range(10):
#             print(number, line)
#             if str(number) not in line and '|' not in line and line != '':
#                 dish = line
#                 cook_book.setdefault(line.strip(), [])
#                 break
#             if '|' in line:
#                 ingredients_line = line.strip().split(' | ')
#                 cook_book[dish] = ingredients_line
#             print(ingredients_line)
# print(cook_book)


# Backup
# cook_book = {}
# recipe_dict = {}
# check_list_int = list(range(10))
# check_list_str = []
# for i in check_list_int:
#     i = str(i)
#     check_list_str.append(i)
# with open('recipes.txt', encoding='utf-8') as f:
#     while True:
#         line_ = f.readline()
#         line = line_.strip()
#         if not line_:
#             break
#         elif line == '':
#             continue
#         if line and line not in check_list_str and '|' not in line:
#             dish = line
#             cook_book.setdefault(dish, [])
#             f.readline()
#         elif '|' in line:
#             recipe_list = line.split(' | ')
#             recipe_dict['ingredient_name'] = recipe_list[0]
#             recipe_dict['quantity'] = recipe_list[1]
#             recipe_dict['measure'] = recipe_list[2]
#             cook_book[dish].append(recipe_dict)
#             print(recipe_list)
#             print(recipe_dict)
#             print(line)
# print(cook_book)
