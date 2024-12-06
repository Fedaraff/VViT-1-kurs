def read_file(filename: str, type: int, num_line = 0):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            if type == 1:
                content = file.read()
                return content
            elif type == 2:
                lst = list()
                for line in file:
                    lst.append(line.rstrip())
                return lst[num_line]
            else:
                return 'Укажите действительный тип вывода'
    except FileNotFoundError:
        return "Вы указали несуществующий файл"

print(read_file('example.txt',2,1))