'''
Створити декоратор
Який пере виконанням функції яку він доповнює буде виводити
START а після її завершення FINISH
'''

def decorator(func):
    def arguments(step1,step2):
        print("START")
        func(step1,step2)
        print("FINISH")
    return arguments

@decorator
def step(a, b):
    print(a, b)
    
step("start S","finish F")


