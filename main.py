import os

# Задание 1
with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        recipes_name = line.strip()
        count = f.readline()
        ingredients = []
        for p in range(int(count)):
            recipes = f.readline().strip().split(' | ')
            product, quantity, word = recipes
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        f.readline()
        cook_book[recipes_name] = ingredients
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
                    cook_product[name_2['product']] = {'measure': name_2['measure'],
                                                       'quantity': (int(name_2['quantity']) * person_count)}
        else:
            print(f'Блюда с название {name} нету в книге рецептов')
    print(cook_product)


# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 1)

# Задание 3

with open('1.txt', encoding='utf-8') as fp1, open('2.txt', encoding='utf-8') as fp2, open('3.txt',
                                                                                          encoding='utf-8') as fp3:
    result = [(len(fp1.readlines()), '1.txt'), (len(fp2.readlines()), '2.txt'), (len(fp3.readlines()), '3.txt')]
    result.sort()
    # print(result)

with open('4.txt', 'a', encoding='utf-8') as fp4:
    for f, file_name in result:
        if file_name in os.path.join(os.getcwd(), file_name):
            fp4.write(f'{file_name}\n')
            fp4.write(str(f'{f}\n'))
            with open(file_name, encoding='utf-8') as fp5:
                for line in fp5:
                    fp4.write(line)
                fp4.write(f'\n')