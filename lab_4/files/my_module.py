def is_prime(number):
    count = 0
    for i in range(2, number): #получаем список чисел, которые находятся в промежутке между 1 и самим числом
        if number % i == 0: # проверяем число на делимость, в случае нахождения числа на которое можно разделить к count добавляем 1
            count +=1
    if count == 0: return True # проверяем
    else: return False