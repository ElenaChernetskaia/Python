while True:                                                       # проверка на введение числового значения
    list_length = input('Введите количество элементов в списке >>> ')
    if list_length.isdigit():
        list_length = int(list_length)
        break
    print('Ошибка ввода, это не число')

user_list = []
i = 0
while i < list_length:
    user_list.append(input('Добавьте новый элемент в список >>> '))
    i += 1
item = 0
for el in range(int(len(user_list)/2)):
    user_list[el], user_list[el + 1] = user_list[el + 1], user_list[el]
    item += 2
print(user_list)
