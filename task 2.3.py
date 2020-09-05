season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
while True:                                                       # проверка на введение числового значения
    user_month = input('Введите номер месяца от 1 до 12 для определения времени года >>> ')
    if user_month.isdigit():
        user_month = int(user_month)
        break
    print('Ошибка ввода, это не число')

if user_month == 1 or user_month == 2 or user_month == 12:         # Зима/Winter
    print(season_list[0])
    print(season_dict.get(1))
elif user_month == 3 or user_month == 4 or user_month == 5:        # Весна/Spring
    print(season_list[1])
    print(season_dict.get(2))
elif user_month == 6 or user_month == 7 or user_month == 8:        # Лето/Summer
    print(season_list[2])
    print(season_dict.get(3))
elif user_month == 9 or user_month == 10 or user_month == 11:      # Осень/Fall
    print(season_list[3])
    print(season_dict.get(4))
else:
    print('В году не может быть месяца с номером не от 1 до 12')       # Ошибка, если ввод числа больше не от 1 до 12
