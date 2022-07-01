def get_recipes(recipes_file):
    cook_book = {}
    with open(recipes_file, encoding='utf-8') as receipt_file:
        while True:
            dish = receipt_file.readline().rstrip().lower()
            cook_book[dish] = []
            if not dish:
                break
            n = int(receipt_file.readline().rstrip())
            items = [receipt_file.readline().rstrip().rsplit('|') for _ in range(n)]
            for item in items:
                ingredient_name_1 = item[0].rstrip()
                quantity_1 = int(item[1].replace(' ', ''))
                measure_1 = item[2].replace(' ', '')
                cook_book[dish].append({'ingredient_name': ingredient_name_1, 'quantity': quantity_1, 'measure': measure_1})
            next(receipt_file)
    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)

def res_file(txt_1, txt_2, txt_3, result):
    file_1 = []
    file_2 = []
    file_3 = []
    len_1 = 0
    len_2 = 0
    len_3 = 0
    with open(txt_1, encoding='utf-8') as f_1:
        file_1 += f_1.readlines()
    with open(txt_2, encoding='utf-8') as f_2:
        file_2 += f_2.readlines()
    with open(txt_3, encoding='utf-8') as f_3:
        file_3 += f_3.readlines()
    len_1 += len(file_1)
    len_2 += len(file_2)
    len_3 += len(file_3)
    res_file_1 = ''
    res_file_2 = ''
    res_file_3 = ''
    for i in file_2:
        res_file_2 += i
        # print(res_file_2)
    for g in file_1:
        res_file_1 += g
    for h in file_3:
        res_file_3 += h
    results_file_1 = f"1.txt\n{len_1}\n{res_file_1}\n"
    results_file_2 = f"2.txt\n{len_2}\n{res_file_2}\n"
    results_file_3 = f"3.txt\n{len_3}\n{res_file_3}\n"
    with open(result, 'a', encoding='utf-8') as res:
        if len(file_2) < len(file_1) < len(file_3):
            res.write(results_file_2)
            res.write(results_file_1)
            res.write(results_file_3)
        elif len(file_1) < len(file_2) < len(file_3):
            res.write(results_file_1)
            res.write(results_file_2)
            res.write(results_file_3)
        elif len(file_2) < len(file_3) < len(file_1):
            res.write(results_file_2)
            res.write(results_file_3)
            res.write(results_file_1)
        elif len(file_1) < len(file_3) < len(file_2):
            res.write(results_file_1)
            res.write(results_file_3)
            res.write(results_file_2)
        elif len(file_3) < len(file_2) < len(file_1):
            res.write(results_file_3)
            res.write(results_file_2)
            res.write(results_file_1)
        else:
            res.write(results_file_3)
            res.write(results_file_1)
            res.write(results_file_2)

cook_book = get_recipes('recipes.txt')
create_shop_list(cook_book)

res_file('1.txt', '2.txt', '3.txt', 'result.txt')


