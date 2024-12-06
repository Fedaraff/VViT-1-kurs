def read_file(type : int, num_line = 0):
    with open('example.txt', 'r', encoding="utf-8") as file:
        if type == 1:
            content = file.read()
            return content
        elif type == 2:
            lst = list()
            for line in file:
                lst.append(line.rstrip())
            return lst[num_line-1]
        else:
            return 'Укажите действительный тип вывода'

print(read_file(2,1))