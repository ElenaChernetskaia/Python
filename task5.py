revenue = int(input("Введите выручку фирмы за год >>> "))
expenses = int(input("Введите издержки фирмы за год >>> "))
profit = revenue - expenses
if profit < 0:
    print("Фирма понесла убытки в размере ", - profit, "руб.")
elif profit == 0:
    print("Фирма не принесла прибыли за год")
else:
    margin = profit / revenue
    print("Фирма получила прибыль в размере ", profit, "руб. Рентабельность составила ", margin)
    employee = int(input("Сколько сотрудников работает в фирме? >>>"))
    cost_per_employee = profit / employee
    print("Прибыль в расчете на сотрудника составила ", cost_per_employee)
