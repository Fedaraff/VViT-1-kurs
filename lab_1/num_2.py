first_count = int(input("Введите первое число: "))
second_count = int(input("Введите второе число: "))
if first_count > second_count:
    print("Большее число: ", first_count)
elif first_count < second_count:
    print("Большее число:", second_count)
else:
    print("Вы указали равные числа...")