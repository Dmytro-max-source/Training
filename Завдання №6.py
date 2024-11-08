# 1
'''
Записати у файл числа від 0 до 100
'''
"""
numbers = [*range(101)]
file = open("db2.txt","a")
file.write(str(numbers))
file.close()
"""
# 2
'''
Прочитати текстовий файл назву якого має вказати користувач
'''
'''
while True:
    choice = input("1 Читання: введіть db2.txt q вихід:")
    if choice == "db2.txt":
        file =  open("db2.txt","r") 
        for line in file:
            print(line)
    if choice == "q":
        break
'''
# 3
'''
Прочитати файл із зображення
Записати дані цього файлу під назвою 1.png
'''
"""
import requests
data = requests.get("https://img.freepik.com/free-photo/3d-render-solar-system-background-with-colourful-nebula_1048-12990.jpg").content
with open("1.png","wb") as file:
    file.write(data)
"""
