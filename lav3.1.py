from random import randint
on = 0
op = 0
while on < 3:
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    print(f"{n1} + {n2} = ", end="")
    otv = input()
    if not otv.isdigit() and otv != "stop":
        print("Некорректный ввод, повторите попытку!")
        otv=input()
        if (n1 + n2) != int(otv):
            print("Неверно")
            on += 1
        if (n1 + n2) == int(otv):
            print("Правильно!")
            op += 1
        if on >= 3:
            print("Игра окончена. Правильных ответов: ", op)
    elif otv == "stop":
        print("Игра завершена.")
    else:
        if (n1 + n2) != int(otv):
            print("Неверно")
            on += 1
        if (n1 + n2) == int(otv):
            print("Правильно!")
            op += 1
        if on >= 3:
            print("Игра окончена. Правильных ответов: ", op)