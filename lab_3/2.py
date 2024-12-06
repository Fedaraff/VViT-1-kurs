def new_file(text: str):
    with open('user_input.txt', 'a+', encoding="utf-8") as file:
        file.write(text)
    return print("Данные записаны")


new_file('Привет')