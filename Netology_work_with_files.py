cook_book = {}
check_for_num = [str(i) for i in list(range(10))]
with open('recipes.txt', encoding='utf-8') as f:
    while True:
        recipe_dict = {}
        line_ = f.readline()
        line = line_.strip()
        if not line_:
            break
        elif line == '':
            continue
        elif line not in check_for_num and '|' not in line:
            dish = line
            cook_book.setdefault(dish, [])
        elif '|' in line:
            recipe_list = line.split(' | ')
            recipe_dict['ingredient_name'] = recipe_list[0]
            recipe_dict['quantity'] = int(recipe_list[1])
            recipe_dict['measure'] = recipe_list[2]
            cook_book[dish].append(recipe_dict)


def get_shop_list_by_dishes(dishes, person_count):
    count_dict = {}
    for dish in dishes:
        for num in range(len(cook_book[dish])):
            for key, value in cook_book[dish][num].items():
                if key == 'ingredient_name':
                    count_dict[value] = {'measure': cook_book[dish][num]['measure'], 'quantity':
                        cook_book[dish][num]['quantity'] * person_count + count_dict[value]['quantity']
                        if value in count_dict else cook_book[dish][num]['quantity'] * person_count}
                break
    return print(count_dict)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)