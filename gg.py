with open("names.txt", "r") as f:
    data = f.readlines()

# удаление строк, для которых выполнено условие
data = filter(lambda line: nomer1 not in line, data)

# более сложные условия редактирования стоит вынести в отдельную функцию
def transformation(line):
    if "Kirill" in line:
        return "замещающая строка\n"
    return line.replace("что_заменить", "на_что")

# редактирование строк файла
data = map(transformation, data)

# открытие, запись и закрытие файла
with open("names.txt", "w") as f:
    f.write("".join(data))
