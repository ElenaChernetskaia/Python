my_list = [100, 1.5, -25, 5+6j, 'простая строка', b"some text", True]


def function_type(el):            # вводим и описываем функцию вывода типа каждого элемента
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


print(function_type(my_list))
