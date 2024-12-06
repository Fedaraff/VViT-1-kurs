count = int(input("Введите число: "))
if count >= 1:
    for item in range(1, count + 1):
        print(item)
else:
    print("Число не положительное")