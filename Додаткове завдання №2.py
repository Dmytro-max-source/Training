'''
Реалізувати функціонал створення читання редагування і видалення товарів
Товар - словник виду title:str description:str price:float
'''

#1. Меню.
#2. Створити товар.
#3. Редагувати товар.
#4. Видалити товар.
#5. Попередне меню.

shop = []
menu = ("=" * 40)

while True:
    choice = input("""
                        1. Create a product.
                        2. Take a look at the product.
                        3. Product visibility.
                        4. Front menu.
                        ENTER:""")
    if choice == "1":
        shop.append({"title":input("Enter product name:\n"),
                      "description":input("Enter a description of the product:\n"),
                      "price":input("Enter the price of the product:\n")})
    if choice == "2":
        for number,item in enumerate(shop,1):
            print(menu)
            print(f"{number}) {item['title']}")
            print(menu)
    if choice == "3":
        print(menu)
        item_num = input("Enter num item")
        if item_num.isdigit() and 0 < int(item_num) <=len(shop):
            item_num = int(item_num) - 1
            
        while True:
            new_choice = input("""
                                1 Read
                                2 Update
                                3 Del
                                4 Front menu.
                                ENTER:""")
            if new_choice == "1":
                print(menu)
                print(shop[item_num])
            if new_choice == "2":
                item = shop[item_num]
                item.update({"title":input("New name:"),
                                "descripion":input("New description:"),
                                "text":input("New price:")})
            if new_choice == "3":
                item = 1 - int(input(item_num))
                shop.pop(item)
                break
            if new_choice == "4":
                break
                
    if choice == "q":
            break

    print("="*45)
            
        
    
