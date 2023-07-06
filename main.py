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
    print(cook_book)