first_count = int(input("Введите первое число: "))
second_count = int(input("Введите второе число: "))
if first_count > second_count:
    print("Большее число: ", first_count) #если первое число больше второго выводится первое
elif first_count < second_count:
    print("Большее число:", second_count) #если второе число больше пеового выводится второе
else:
    print("Вы указали равные числа...") #во всех других случаях выводится сообщения, что числа равны