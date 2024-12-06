def greet(name):
    return f"Привет {name}"


print(greet('Сергей'))


def square(number):
    return (number ** 2)


print(square(20))


def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "Числа равны"


print(max_of_two(5, 7))