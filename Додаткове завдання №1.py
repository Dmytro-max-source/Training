weight = int(input('Введіть массу тіла (кг).:'))
height = float(input('Введіть зріст (м).:'))
BMI = weight/height**2

if BMI < 18.5:
    print('Свідчить про недостатню вагу')
elif BMI > 18.5 and BMI < 24.9:
    print('Еквівалент нормальної маси тіла')
elif BMI > 25.0 and BMI < 29.9:
    print('вказує на наявність зайвої ваги')
elif BMI > 30:
    print('Є ознакою ожиріння')
else:
    print('ERROR')
    
#старий варіант
"""
a = int(input('Введіть массу тіла (кг).:'))
b = float(input('Введіть зріст (м).:'))
ab = a/b**2

if ab < 18.5:
    print ('Свідчить про недостатню вагу')
elif ab > 18.5 and ab < 24.9:
    print('Еквівалент нормальної маси тіла')
elif ab > 25.0 and ab < 29.9:
    print('вказує на наявність зайвої ваги')
elif ab > 30:
    print('Є ознакою ожиріння')
else:
    print('ERROR')
    
"""
