def calc(n ,a, b='' ):
    if a == 2:
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        return b
    if a == 8:
        while n > 0:
            b = str(n % 8) + b
            n = n // 8
        return b
    else:
        return ("Invalid data")
flag = True
while flag:
    try:
        n = int(input("Введите число: "))
        a = int(input("Введите систему исчисления: "))
    except ValueError:
        print('неверный ввод')
    else: 
        flag = False
print(calc(n,a))