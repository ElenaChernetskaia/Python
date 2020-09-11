# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.
def user_info(name, surname, birth_year, city, email, phone):
    print(f"{name}{surname}{birth_year}{city}{email}{phone}")


user_info(name='Елена ', surname='Чернецкая ', birth_year='1990 ', city='Москва ', email='email@email.email ', phone='80000000000 ')
