count = int(input("Введите число: "))
if count >= 1:
    for item in range(1, count + 1): # к count прибавляем 1, поскольку в range диапазон не включает указанную границу
        print(item)
else:
    print("Число не положительное")