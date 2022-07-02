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

def compile_files(files_list):
    data = {}
    for file in files_list:
        with open(file, encoding="utf-8") as f:
            file_data = f.readlines()
            data[len(file_data)] = (file, " ".join(file_data))

    data = dict(sorted(data.items()))

    with open("result.txt", "w", encoding="utf-8") as new_file:
        for key, value in data.items():
            new_file.write(f"{value[0]} \n")
            new_file.write(f"{key} \n")
            new_file.write(f"{value[1]} \n")


files = ["1.txt", "2.txt", "3.txt"]
files = [ (file) for file in files]
compile_files(files)
cook_book = get_recipes('recipes.txt')
create_shop_list(cook_book)

