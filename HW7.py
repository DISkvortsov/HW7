from pprint import pprint

with open('Recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    cook_book_keys = ['ingredient_name', 'quantity', 'measure']
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())
        dish_ingr_list = []
        for item in range(counter):
            ingr = file.readline().strip().split('|')
            ingr_dict = dict(zip(cook_book_keys, ingr))
            dish_ingr_list.append(ingr_dict)
        file.readline()
        cook_book[dish_name] = dish_ingr_list

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            ingr_name = ingr['ingredient_name']
            if ingr_name not in shop_dict:
                shop_dict[ingr_name] = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
            else:
                shop_dict[ingr_name]['quantity'] += int(ingr['quantity']) * person_count
    return shop_dict

#pprint(cook_book)
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Селедка под шубой'], 3))