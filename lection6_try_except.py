try: #блок, де може виникнути помилка
    number = int(input("Введіть число: "))
    print("Введене число:", number)
except: #перехоплення та обробка всіх винятків
    print("Перетворення прошло невдало")
    file1=open("result.txt",'a',encoding="UTF-8")
    print("Перетворення прошло невдало",file=file1)

print("Завершення програми")

try:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    print("Результат ділення:", number1/number2)
except ValueError as e:
    print("Перетворення прошло невдало. Info: ",e)
    print(e.__doc__)
except ZeroDivisionError:
    print("Спроба ділення числа на нуль")
except Exception:
    print("Загальне виключення")
    print("Завершення програми")


try:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    if number2 == 0:
        raise Exception(f"Друге число не повинне бути рівним 0. У вас помилка ділення {number1}/{number2}")
    print("Результат ділення двох чисел:", number1 / number2)
except ValueError:
    print("Введено нероректні дані")
except Exception as e:
    print(e)
print("Заврешення програми")