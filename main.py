# Задание 1
with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        recepie_name = line.strip()
        count = f.readline()
        ingredients = []
        for p in range(int(count)):
            recepie = f.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        f.readline()
        cook_book[recepie_name] = ingredients
    # print(cook_book)

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    cook_product = {}
    for name in dishes:
        if name in cook_book:
            for name_2 in cook_book[name]:
                if name_2['product'] in cook_product:
                    cook_product[name_2['product']]['quantity'] += int(name_2['quantity']) * person_count
                else:
                    cook_product[name_2['product']] = {'measure': name_2['measure'], 'quantity': (int(name_2['quantity']) * person_count)}
        else:
            print(f'Блюда с название {name} нету в книге рецептов')
    print(cook_product)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 1)