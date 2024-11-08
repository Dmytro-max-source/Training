'''
1)Реалізувати функціонал створення читання редагування і видалення товарів
Товар - словник виду title:str description:str price:float

2)Об'єднати реалізовані системи входу та систему керуванням товарами (створення читання оновлення видалення)
'''

#1. Меню.
#2. Створити товар.
#3. Редагувати товар.
#4. Видалити товар.
#5. Попередне меню.
users = []
shops = []
hr = "=" * 40
number_of_try = 3

def login():
    user_login = input("Login:")
    user_password = input("Password:")
    for user in users:
        if user_login == user["login"] and user_password == user["password"]:
            print(f"You are logged in as {user_login}")
            return user

def registration():
    user_login = input("Login:")
    user_password = input("Password:")
    if user_login not in [user["login"] for user in users]:
        user = {"login":user_login,"password":user_password}
        users.append(user)
        print("Registered successfully")

def check_try(user):
   global number_of_try
   if user is None:
       number_of_try -= 1
       print(f"Number of attempts {number_of_try}")
   else:
       print("The number of attempts has been exhausted, please restart the application") 

def create_item():
    item ={"title":
           input("Enter product name:\n"),
            "description":
           input("Enter a description of the product:\n"),
            "price":
           input("Enter the price of the product:\n")}
    return item

def main_menu(user):
    print(f"Welcome user: {user['login']}")
    while True:
        choice = input("q для виходу:")
        if choice == "q":
            break
def shop():
    while True:
        choice = input("""
                            1. Create a product.
                            2. Take a look at the product.
                            3. Product visibility.
                            4. Front menu.
                            ENTER:""")
        if choice == "1":
            shops.append(create_item())
        if choice == "2":
            for number,item in enumerate(shops,1):
                print(hr)
                print(f"{number}) {item['title']}")
                print(hr)
        if choice == "3":
            print(hr)
            item_num = input("Enter num item")
            if item_num.isdigit() and 0 < int(item_num) <=len(shops):
                item_num = int(item_num) - 1
                
            while True:
                new_choice = input("""
                                    1 Read
                                    2 Update
                                    3 Del
                                    4 Front menu.
                                    ENTER:""")
                if new_choice == "1":
                    print(hr)
                    print(shops[item_num])
                if new_choice == "2":
                    item = shops[item_num]
                    item.update(create_item())
                if new_choice == "3":
                    item = 1 - int(input(item_num))
                    shops.pop(item)
                    break
                if new_choice == "4":
                    break
                    
        if choice == "q":
                break

        print(hr)

while True:
    choice = input("""
                      1 Registration
                      2 Login
                      q Exit:
                      ENTER:""")
    if choice == "1":
        registration()
    if choice == "2":
        if number_of_try > 0:
            user = login()
            check_try(user)
            if user:
                shop()
                
    if choice == "q":
        break






