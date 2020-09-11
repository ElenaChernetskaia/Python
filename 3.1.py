# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль

def division_func(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
        return f"Результат деления {arg_1} на {arg_2} равен {result}"
    except ZeroDivisionError:
        return "Делитель не может быть равень 0"
    except ValueError:
        return "Делить можно только числовые значения"


a = int(input("Введите делимое >>> "))
b = int(input("Введите делитель >>> "))
print(division_func(a, b))
