
class Number:
    def is_prime(number):
        count = 0
        for i in range(2, number):
            if number % i == 0:
                count += 1
        if count == 0:
            return True
        else:
            return False

    def square(number):
        return (number ** 2)

    def greatest_number(num1, num2):
        if num1 > num2:
            return f"Большее число: {num1}"
        elif num1 < num2:
            return f'Большее число: {num2}'
        else:
            return "Вы указали равные числа..."


class Words:
    def describe_person(name, age=30):
        return f"Меня зовут {name}. Мне {age} лет."

    def greet(name):
        return f"Привет {name}"

    def good_work(name):
        return f"Хорошая работа {name}"

