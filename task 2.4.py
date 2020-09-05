user_str = input('Введите несколько слов через пробел >>> ')
new_line = []       # сюда будем записывать каждое слово с номером новой строки
str_number = 1      # номер строки
for el in range(user_str.count(' ')+1):
    new_line = user_str.split()
    if len(str(new_line)) <= 10:
        print(f"{str_number} {new_line[el]}")
        str_number += 1
    else:
        print(f"{str_number} {new_line[el][0:10]}")
        str_number += 1
