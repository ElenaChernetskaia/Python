# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    sum_list = []
    max_1 = max(my_list)
    sum_list.append(max_1)
    my_list.remove(max_1)
    max_2 = max(my_list)
    sum_list.append(max_2)
    return sum(sum_list)


a_1 = int(input('Введите первое число >>> '))
a_2 = int(input('Введите второе число >>> '))
a_3 = int(input('Введите третье число >>> '))
print(my_func(a_1, a_2, a_3))

