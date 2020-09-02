n = int(input("Введите целое положительное число для определения наибольшей цифры в нем >>> "))
max_number = 0
while n > 0:
    if n % 10 > max_number:
        max_number = n % 10
    n = n // 10
print("Наибольшая цифра ", max_number)
